"""Small offline event calculator, not a GA4/Mixpanel/Amplitude implementation.

CSV schema is exactly event_id,unit_id,event,timestamp. Input must already be
authorized and eligibility-filtered. unit_id is opaque; it is NOT necessarily a
person. No identity joins, bot/consent inference, attribution, sessions, revenue,
statistical inference, or instrumentation validation are implemented.

Closed sequential funnel: first observed occurrence of steps[0] per unit;
earliest qualifying subsequent event strictly AFTER the preceding stage, and
at or BEFORE entry + window_hours. Intervening events are allowed. Repeated
entries never restart the window. Equal timestamps do not establish order.
Only units observed through the full window enter conversion denominators.

Exact elapsed-day retention: configured retention_event in
[entry + day*24h, entry + (day+1)*24h), strictly after entry. An entire return
interval must be observable at cutoff for that unit to enter the denominator.
This is not calendar-day, rolling, or unbounded retention.

All instants are normalized to UTC, including duplicate comparison. The first
identical event_id wins; any conflicting payload is an error, even after cutoff.
Events exactly at cutoff are observed; later events are excluded and listed.
Missing behavior can be missing telemetry, not a behavioral failure.

Run: python -B tools/product_event_analysis.py --events events.csv --config config.json
Optional --out writes JSON to an explicitly selected path instead of stdout.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path


COLUMNS = ("event_id", "unit_id", "event", "timestamp")
CONFIG_KEYS = {"steps", "window_hours", "cutoff", "retention_event", "retention_day"}
ISO_PATTERN = re.compile(
    r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(?::\d{2}(?:\.\d{1,6})?)?(?:Z|[+-]\d{2}:\d{2})"
)


class InputError(ValueError):
    """Input cannot be safely interpreted under the fixed contract."""


def text_field(value, name):
    if not isinstance(value, str) or not value or value != value.strip():
        raise InputError(f"{name} must be a nonempty string without outer whitespace")
    return value


def instant(value, name):
    """Accept extended ISO 8601 with T, explicit Z/offset and microsecond precision."""
    text_field(value, name)
    if not ISO_PATTERN.fullmatch(value):
        raise InputError(f"{name} must be an aware extended ISO8601 timestamp")
    if value[-1] != "Z" and (int(value[-5:-3]) > 23 or int(value[-2:]) > 59):
        raise InputError(f"invalid timezone offset in {name}: {value}")
    try:
        result = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if result.tzinfo is None or result.utcoffset() is None:
            raise ValueError("missing offset")
        return result.astimezone(timezone.utc)
    except (ValueError, OverflowError) as exc:
        raise InputError(f"invalid {name}: {value}") from exc


def iso(value):
    return value.isoformat().replace("+00:00", "Z")


def validate_config(config):
    if not isinstance(config, dict) or set(config) != CONFIG_KEYS:
        raise InputError("config must contain exactly: " + ", ".join(sorted(CONFIG_KEYS)))
    steps = config["steps"]
    if not isinstance(steps, list) or not steps:
        raise InputError("steps must be a nonempty list")
    steps = [text_field(step, "step") for step in steps]
    hours = config["window_hours"]
    if isinstance(hours, bool) or not isinstance(hours, (int, float)):
        raise InputError("window_hours must be a finite nonnegative number")
    try:
        if not math.isfinite(hours) or hours < 0:
            raise ValueError("invalid window")
        window = timedelta(hours=hours)
        if hours > 0 and not window:
            raise ValueError("window below supported microsecond resolution")
    except (ValueError, OverflowError) as exc:
        raise InputError("window_hours must fit a finite nonnegative timedelta") from exc
    day = config["retention_day"]
    if isinstance(day, bool) or not isinstance(day, int) or day < 0:
        raise InputError("retention_day must be a nonnegative integer")
    try:
        return_start = timedelta(days=day)
        return_end = timedelta(days=day + 1)
    except OverflowError as exc:
        raise InputError("retention_day is too large") from exc
    return {
        "steps": steps,
        "window_hours": hours,
        "window": window,
        "cutoff": instant(config["cutoff"], "cutoff"),
        "retention_event": text_field(config["retention_event"], "retention_event"),
        "retention_day": day,
        "return_start": return_start,
        "return_end": return_end,
    }


def read_events(path):
    with Path(path).open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream, strict=True)
        if reader.fieldnames is None or len(reader.fieldnames) != 4 or set(reader.fieldnames) != set(COLUMNS):
            raise InputError("CSV must have exactly these unique columns: " + ",".join(COLUMNS))
        rows = []
        for row in reader:
            if None in row or any(value is None for value in row.values()):
                raise InputError(f"CSV line {reader.line_num}: missing or extra fields")
            rows.append(row)
        return rows


def reject_duplicate_json_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise InputError(f"duplicate config key: {key}")
        result[key] = value
    return result


def fraction(numerator, denominator):
    return {"numerator": numerator, "denominator": denominator,
            "rate": numerator / denominator if denominator else None}


def analyze(rows, config):
    cfg = validate_config(config)
    unique = {}
    duplicates = []
    raw_count = 0
    for number, row in enumerate(rows, 1):
        raw_count += 1
        if not isinstance(row, dict) or set(row) != set(COLUMNS):
            raise InputError(f"record {number}: expected exactly {COLUMNS}")
        event_id = text_field(row["event_id"], f"record {number} event_id")
        unit_id = text_field(row["unit_id"], f"record {number} unit_id")
        name = text_field(row["event"], f"record {number} event")
        at = instant(row["timestamp"], f"record {number} timestamp")
        payload = (unit_id, name, at)
        if event_id in unique:
            if unique[event_id]["payload"] != payload:
                raise InputError(f"conflicting duplicate event_id: {event_id}")
            duplicates.append({"event_id": event_id, "kept_record": unique[event_id]["record"],
                               "excluded_record": number})
        else:
            unique[event_id] = {"event_id": event_id, "unit_id": unit_id, "event": name,
                                "at": at, "record": number, "payload": payload}
    observed = [event for event in unique.values() if event["at"] <= cfg["cutoff"]]
    after_cutoff = [event for event in unique.values() if event["at"] > cfg["cutoff"]]
    grouped = {}
    for event in observed:
        grouped.setdefault(event["unit_id"], []).append(event)
    audits = []
    non_entry_units = []
    for unit_id in sorted(grouped):
        events = sorted(grouped[unit_id], key=lambda event: (event["at"], event["record"]))
        entry = next((event for event in events if event["event"] == cfg["steps"][0]), None)
        if entry is None:
            non_entry_units.append(unit_id)
            continue
        try:
            funnel_end = entry["at"] + cfg["window"]
            return_start = entry["at"] + cfg["return_start"]
            return_end = entry["at"] + cfg["return_end"]
        except OverflowError as exc:
            raise InputError(f"analysis window overflows datetime for unit: {unit_id}") from exc
        reached = [entry]
        for step in cfg["steps"][1:]:
            following = next((event for event in events
                              if event["event"] == step and reached[-1]["at"] < event["at"] <= funnel_end), None)
            if following is None:
                break
            reached.append(following)
        returns = [event["event_id"] for event in events
                   if event["event"] == cfg["retention_event"]
                   and return_start <= event["at"] < return_end and event["at"] > entry["at"]]
        retention_mature = return_end <= cfg["cutoff"]
        audits.append({
            "unit_id": unit_id, "entry_event_id": entry["event_id"], "entry_at": iso(entry["at"]),
            "funnel_window_end": iso(funnel_end), "funnel_fully_observed": funnel_end <= cfg["cutoff"],
            "reached_stage_count": len(reached),
            "reached_event_ids": [event["event_id"] for event in reached],
            "reached_at": [iso(event["at"]) for event in reached],
            "retention_interval_start_inclusive": iso(return_start),
            "retention_interval_end_exclusive": iso(return_end),
            "retention_fully_observed": retention_mature,
            "observed_return_event_ids": returns,
            "retained": bool(returns) if retention_mature else None,
        })
    mature_funnel = [unit for unit in audits if unit["funnel_fully_observed"]]
    mature_retention = [unit for unit in audits if unit["retention_fully_observed"]]
    stages = []
    previous = len(mature_funnel)
    for position, step in enumerate(cfg["steps"], 1):
        n = sum(unit["reached_stage_count"] >= position for unit in mature_funnel)
        stages.append({"stage": position, "event": step,
                       "observed_reached_units": sum(unit["reached_stage_count"] >= position for unit in audits),
                       "fully_observed_reached_units": n,
                       "from_entry": fraction(n, len(mature_funnel)),
                       "from_previous_stage": fraction(n, previous)})
        previous = n
    warnings = []
    if after_cutoff:
        warnings.append({"code": "EVENTS_AFTER_CUTOFF_EXCLUDED", "count": len(after_cutoff),
                         "event_ids": [event["event_id"] for event in after_cutoff]})
    names = {event["event"] for event in observed}
    missing = sorted((set(cfg["steps"]) | {cfg["retention_event"]}) - names)
    if missing:
        warnings.append({"code": "CONFIGURED_EVENTS_NOT_OBSERVED", "events": missing,
                         "meaning": "Check event definitions and telemetry; not proof of absent behavior."})
    for kind, mature in (("FUNNEL", mature_funnel), ("RETENTION", mature_retention)):
        censored = len(audits) - len(mature)
        if censored:
            warnings.append({"code": kind + "_RIGHT_CENSORED_UNITS_EXCLUDED_FROM_DENOMINATOR", "count": censored})
    return {
        "status": "ok", "calculator_version": 1,
        "scope": {
            "unit": "opaque supplied unit_id; no identity stitching or population inference",
            "eligibility": "all supplied records; caller must filter eligibility and verify authorization upstream",
            "funnel": "closed first-entry sequential; strict later timestamps; inclusive entry-based window end; no restart",
            "retention": "exact elapsed-day [entry+day*24h, entry+(day+1)*24h); strictly after entry",
            "maturity": "cutoff must reach the entire respective window end, even if outcome already observed",
            "duplicates": "first event_id retained; payload comparison uses UTC-normalized instants",
            "time": "UTC elapsed durations, not local calendar days; cutoff inclusive",
            "not_supported": ["platform metric compatibility", "causal inference", "instrumentation validation",
                              "automatic eligibility/bot/consent filtering", "revenue", "sessions", "population estimates"],
        },
        "config": {key: iso(cfg[key]) if key == "cutoff" else cfg[key] for key in sorted(CONFIG_KEYS)},
        "raw_counts": {"input_records": raw_count, "unique_events": len(unique),
                       "duplicate_records_removed": len(duplicates), "events_after_cutoff": len(after_cutoff),
                       "observed_events": len(observed), "units_in_unique_input": len({event["unit_id"] for event in unique.values()}),
                       "units_with_observed_events": len(grouped), "observed_units_without_entry": len(non_entry_units)},
        "funnel": {"entry_cohort_units": len(audits), "fully_observed_units": len(mature_funnel),
                   "right_censored_units": len(audits) - len(mature_funnel), "stages": stages,
                   "completion": fraction(previous, len(mature_funnel)),
                   "fully_observed_units_without_recorded_completion": len(mature_funnel) - previous},
        "retention": {"event": cfg["retention_event"], "elapsed_day": cfg["retention_day"],
                      "entry_cohort_units": len(audits), "fully_observed_units": len(mature_retention),
                      "right_censored_units": len(audits) - len(mature_retention),
                      "return": fraction(sum(unit["retained"] for unit in mature_retention), len(mature_retention))},
        "reconciliation": {"duplicate_records": duplicates,
                           "after_cutoff_events": [{"event_id": event["event_id"], "unit_id": event["unit_id"],
                                                   "timestamp": iso(event["at"]), "record": event["record"]} for event in after_cutoff],
                           "observed_units_without_entry": non_entry_units},
        "unit_audit": audits, "warnings": warnings,
        "limitations": ["Counts describe supplied recorded events only; missing events may mean missing telemetry.",
                        "No statistical significance, motive, business failure, market adoption, or causal claims are calculated."],
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--events", type=Path, required=True)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--out", type=Path, help="Explicit JSON output path; otherwise stdout")
    args = parser.parse_args(argv)
    try:
        if args.out and args.out.resolve() in (args.events.resolve(), args.config.resolve()):
            raise InputError("output must not overwrite an input file")
        if args.out and args.out.exists() and any(args.out.samefile(path) for path in (args.events, args.config)):
            raise InputError("output must not overwrite an input file through a file alias")
        config = json.loads(args.config.read_text(encoding="utf-8-sig"), object_pairs_hook=reject_duplicate_json_keys)
        result = analyze(read_events(args.events), config)
        encoded = json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
        if args.out:
            args.out.write_text(encoded, encoding="utf-8")
        else:
            sys.stdout.write(encoded)
    except (InputError, OSError, UnicodeError, json.JSONDecodeError, csv.Error) as exc:
        sys.stderr.write(json.dumps({"status": "error", "error": str(exc)}, ensure_ascii=False) + "\n")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
