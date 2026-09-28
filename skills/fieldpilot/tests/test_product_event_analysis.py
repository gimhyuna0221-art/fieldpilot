"""Deterministic calculator tests, not a blind LLM or provider comparison."""

import importlib.util
import csv
import io
import json
from pathlib import Path
import subprocess
import sys
import unittest
from contextlib import redirect_stdout, redirect_stderr
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "product_event_analysis.py"
FIXTURES = ROOT / "tests" / "competitor_coverage"
SPEC = importlib.util.spec_from_file_location("product_event_analysis", SCRIPT)
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)


def event(key, name, at, unit="U"):
    return {"event_id": key, "unit_id": unit, "event": name, "timestamp": at}


def config(**updates):
    value = {"steps": ["signup", "checkout", "pay"], "window_hours": 24,
             "cutoff": "2026-01-05T00:00:00Z", "retention_event": "return", "retention_day": 1}
    value.update(updates)
    return value


class EventAnalysisTests(unittest.TestCase):
    def setUp(self):
        self.start = event("s", "signup", "2026-01-01T00:00:00Z")

    def run_rows(self, rows, **updates):
        return mod.analyze(rows, config(**updates))

    def test_fixture_expected_counts(self):
        result = mod.analyze(mod.read_events(FIXTURES / "event_fixture.csv"),
                             json.loads((FIXTURES / "event_config.json").read_text()))
        self.assertEqual(result["raw_counts"], {
            "input_records": 27, "unique_events": 26, "duplicate_records_removed": 1,
            "events_after_cutoff": 1, "observed_events": 25, "units_in_unique_input": 7,
            "units_with_observed_events": 7, "observed_units_without_entry": 1})
        self.assertEqual(result["funnel"]["entry_cohort_units"], 6)
        self.assertEqual(result["funnel"]["fully_observed_units"], 5)
        self.assertEqual(result["funnel"]["right_censored_units"], 1)
        self.assertEqual([r["observed_reached_units"] for r in result["funnel"]["stages"]], [6, 5, 3])
        self.assertEqual([r["fully_observed_reached_units"] for r in result["funnel"]["stages"]], [5, 4, 2])
        self.assertEqual(result["funnel"]["completion"], {"numerator": 2, "denominator": 5, "rate": .4})
        self.assertEqual(result["funnel"]["stages"][2]["from_previous_stage"], {"numerator": 2, "denominator": 4, "rate": .5})
        self.assertEqual(result["retention"]["return"], {"numerator": 3, "denominator": 5, "rate": .6})

    def test_valid_sequence(self):
        result = self.run_rows([self.start, event("c", "checkout", "2026-01-01T01:00:00Z"),
                               event("p", "pay", "2026-01-01T02:00:00Z")])
        self.assertEqual(result["funnel"]["completion"], {"numerator": 1, "denominator": 1, "rate": 1.0})

    def test_wrong_order_does_not_convert(self):
        result = self.run_rows([event("p", "pay", "2025-12-31T23:00:00Z"), self.start,
                               event("c", "checkout", "2026-01-01T01:00:00Z")])
        self.assertEqual(result["unit_audit"][0]["reached_stage_count"], 2)
        self.assertEqual(result["funnel"]["completion"]["numerator"], 0)

    def test_late_valid_payment_after_early_wrong_order_counts(self):
        result = self.run_rows([self.start, event("p0", "pay", "2026-01-01T01:00:00Z"),
                               event("c", "checkout", "2026-01-01T02:00:00Z"),
                               event("p1", "pay", "2026-01-01T03:00:00Z")])
        self.assertEqual(result["unit_audit"][0]["reached_event_ids"], ["s", "c", "p1"])
        self.assertEqual(result["funnel"]["completion"]["numerator"], 1)

    def test_repeated_entry_never_resets_window(self):
        result = self.run_rows([self.start, event("s2", "signup", "2026-01-01T23:00:00Z"),
                               event("c", "checkout", "2026-01-02T01:00:00Z")])
        self.assertEqual(result["unit_audit"][0]["reached_stage_count"], 1)
        self.assertEqual(result["funnel"]["stages"][1]["from_entry"]["rate"], 0.0)

    def test_window_end_included_and_microsecond_late_excluded(self):
        for stamp, expected in [("2026-01-02T00:00:00Z", 1), ("2026-01-02T00:00:00.000001Z", 0)]:
            with self.subTest(stamp=stamp):
                result = self.run_rows([self.start, event("p", "pay", stamp)], steps=["signup", "pay"])
                self.assertEqual(result["funnel"]["completion"]["numerator"], expected)

    def test_simultaneous_events_do_not_establish_order(self):
        result = self.run_rows([self.start, event("c", "checkout", "2026-01-01T00:00:00Z"),
                               event("p", "pay", "2026-01-01T01:00:00Z")])
        self.assertEqual(result["unit_audit"][0]["reached_stage_count"], 1)

    def test_unsorted_rows_are_ordered_by_timestamp(self):
        result = self.run_rows([event("p", "pay", "2026-01-01T02:00:00Z"),
                               event("c", "checkout", "2026-01-01T01:00:00Z"), self.start])
        self.assertEqual(result["unit_audit"][0]["reached_event_ids"], ["s", "c", "p"])

    def test_timezone_offsets_and_elapsed_day_not_calendar_day(self):
        result = self.run_rows([event("s", "signup", "2026-01-01T23:00:00-05:00"),
                               event("r0", "return", "2026-01-02T12:00:00-05:00"),
                               event("r1", "return", "2026-01-03T13:00:00+09:00")])
        self.assertEqual(result["unit_audit"][0]["entry_at"], "2026-01-02T04:00:00Z")
        self.assertEqual(result["unit_audit"][0]["observed_return_event_ids"], ["r1"])
        self.assertEqual(result["retention"]["return"]["numerator"], 1)

    def test_retention_lower_inclusive_upper_exclusive(self):
        for at, expected in [("2026-01-01T23:59:59Z", 0), ("2026-01-02T00:00:00Z", 1),
                             ("2026-01-02T23:59:59.999999Z", 1), ("2026-01-03T00:00:00Z", 0)]:
            with self.subTest(at=at):
                result = self.run_rows([self.start, event("r", "return", at)])
                self.assertEqual(result["retention"]["return"]["numerator"], expected)

    def test_return_event_name_is_not_any_activity(self):
        rows = [self.start, event("r", "page_view", "2026-01-02T12:00:00Z")]
        self.assertEqual(self.run_rows(rows)["retention"]["return"]["numerator"], 0)
        self.assertEqual(self.run_rows(rows, retention_event="page_view")["retention"]["return"]["numerator"], 1)

    def test_day_zero_entry_is_not_itself_a_return(self):
        self.assertEqual(self.run_rows([self.start], retention_day=0, retention_event="signup")["retention"]["return"]["numerator"], 0)
        rows = [self.start, event("s2", "signup", "2026-01-01T00:00:01Z")]
        self.assertEqual(self.run_rows(rows, retention_day=0, retention_event="signup")["retention"]["return"]["numerator"], 1)

    def test_recent_completed_unit_still_censored(self):
        rows = [self.start, event("p", "pay", "2026-01-01T01:00:00Z")]
        result = self.run_rows(rows, steps=["signup", "pay"], cutoff="2026-01-01T12:00:00Z")
        self.assertEqual(result["funnel"]["stages"][1]["observed_reached_units"], 1)
        self.assertEqual(result["funnel"]["completion"], {"numerator": 0, "denominator": 0, "rate": None})
        self.assertEqual(result["retention"]["return"]["denominator"], 0)
        self.assertIsNone(result["unit_audit"][0]["retained"])

    def test_retention_censored_even_with_observed_return(self):
        result = self.run_rows([self.start, event("r", "return", "2026-01-02T01:00:00Z")],
                               cutoff="2026-01-02T12:00:00Z")
        self.assertEqual(result["funnel"]["fully_observed_units"], 1)
        self.assertEqual(result["retention"]["return"], {"numerator": 0, "denominator": 0, "rate": None})
        self.assertEqual(result["unit_audit"][0]["observed_return_event_ids"], ["r"])

    def test_maturity_exact_boundary(self):
        result = self.run_rows([self.start], cutoff="2026-01-03T00:00:00Z")
        self.assertEqual(result["retention"]["fully_observed_units"], 1)
        result = self.run_rows([self.start], cutoff="2026-01-02T23:59:59.999999Z")
        self.assertEqual(result["retention"]["fully_observed_units"], 0)

    def test_cutoff_inclusive_future_excluded_with_warning(self):
        result = self.run_rows([self.start, event("p", "pay", "2026-01-02T00:00:00Z"),
                               event("f", "pay", "2026-01-02T00:00:00.000001Z")],
                              steps=["signup", "pay"], cutoff="2026-01-02T00:00:00Z")
        self.assertEqual(result["raw_counts"]["observed_events"], 2)
        self.assertEqual(result["raw_counts"]["events_after_cutoff"], 1)
        self.assertEqual(result["funnel"]["completion"]["numerator"], 1)
        self.assertEqual(result["warnings"][0]["event_ids"], ["f"])

    def test_identical_and_equivalent_offset_duplicates(self):
        equivalent = dict(self.start, timestamp="2026-01-01T09:00:00+09:00")
        result = self.run_rows([self.start, dict(self.start), equivalent])
        self.assertEqual(result["raw_counts"]["duplicate_records_removed"], 2)
        self.assertEqual(result["raw_counts"]["unique_events"], 1)
        self.assertEqual(result["reconciliation"]["duplicate_records"][1]["kept_record"], 1)

    def test_conflicting_duplicates_error_even_after_cutoff(self):
        for key, value in [("event", "pay"), ("unit_id", "other"), ("timestamp", "2030-01-01T00:00:00Z")]:
            with self.subTest(key=key):
                with self.assertRaisesRegex(mod.InputError, "conflicting duplicate"):
                    self.run_rows([self.start, dict(self.start, **{key: value})])

    def test_missing_fields_and_naive_or_invalid_timestamp(self):
        for key in ["event_id", "unit_id", "event", "timestamp"]:
            with self.subTest(key=key), self.assertRaises(mod.InputError):
                self.run_rows([dict(self.start, **{key: ""})])
        for stamp in ["2026-01-01T00:00:00", "2026-13-01T00:00:00Z", "2026-01-01T00:00:00+00:99", "bad"]:
            with self.subTest(stamp=stamp), self.assertRaises(mod.InputError):
                self.run_rows([dict(self.start, timestamp=stamp)])

    def test_invalid_config(self):
        for update in [{"window_hours": -1}, {"window_hours": float("nan")}, {"window_hours": float("inf")},
                       {"window_hours": True}, {"retention_day": -1}, {"retention_day": 1.5},
                       {"retention_day": True}, {"retention_event": ""}, {"steps": []},
                       {"cutoff": "2026-01-01T00:00:00"}, {"window_hours": 1e-100}, {"unexpected": 1}]:
            with self.subTest(update=update), self.assertRaises(mod.InputError):
                self.run_rows([self.start], **update)

    def test_repeated_step_names_require_distinct_later_events(self):
        rows = [self.start, event("s2", "signup", "2026-01-01T01:00:00Z")]
        result = self.run_rows(rows, steps=["signup", "signup", "signup"])
        self.assertEqual([r["fully_observed_reached_units"] for r in result["funnel"]["stages"]], [1, 1, 0])

    def test_zero_window_single_step_and_empty_data(self):
        result = self.run_rows([self.start], steps=["signup"], window_hours=0)
        self.assertEqual(result["funnel"]["completion"]["rate"], 1.0)
        empty = self.run_rows([])
        self.assertEqual(empty["funnel"]["completion"], {"numerator": 0, "denominator": 0, "rate": None})
        self.assertEqual(empty["raw_counts"]["input_records"], 0)

    def test_nonentry_and_only_future_unit_excluded(self):
        result = self.run_rows([event("p", "pay", "2026-01-01T01:00:00Z"),
                               event("s", "signup", "2026-01-06T00:00:00Z", "future")])
        self.assertEqual(result["funnel"]["entry_cohort_units"], 0)
        self.assertEqual(result["raw_counts"]["units_in_unique_input"], 2)
        self.assertEqual(result["reconciliation"]["observed_units_without_entry"], ["U"])

    def test_csv_schema_and_missing_cell_errors(self):
        for content in ["event_id,unit_id,event\na,U,signup\n",
                        "event_id,unit_id,event,timestamp\na,U,signup\n",
                        "event_id,unit_id,event,event\na,U,signup,x\n"]:
            with patch.object(Path, "open", return_value=io.StringIO(content)):
                with self.assertRaises(mod.InputError):
                    mod.read_events("not-written.csv")

    def test_cli_stdout_and_explicit_output(self):
        command = [sys.executable, "-B", str(SCRIPT), "--events", str(FIXTURES / "event_fixture.csv"),
                   "--config", str(FIXTURES / "event_config.json")]
        completed = subprocess.run(command, capture_output=True, text=True, check=True)
        self.assertEqual(json.loads(completed.stdout)["funnel"]["completion"]["numerator"], 2)
        # Exercise the explicit-output code path without requiring temp filesystem permissions.
        buffer = io.StringIO()
        with patch.object(Path, "write_text") as write, redirect_stdout(buffer):
            code = mod.main(command[3:] + ["--out", str(ROOT / "not-written-result.json")])
            self.assertEqual(code, 0)
            self.assertEqual(buffer.getvalue(), "")
            self.assertEqual(write.call_count, 1)
            self.assertEqual(json.loads(write.call_args.args[0])["retention"]["return"]["numerator"], 3)

    def test_cli_prevents_input_overwrite_and_reports_json_error(self):
        command = [sys.executable, "-B", str(SCRIPT), "--events", str(FIXTURES / "event_fixture.csv"),
                   "--config", str(FIXTURES / "event_config.json"), "--out", str(FIXTURES / "event_config.json")]
        before = (FIXTURES / "event_config.json").read_bytes()
        completed = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(completed.returncode, 2)
        self.assertEqual(json.loads(completed.stderr)["status"], "error")
        self.assertEqual((FIXTURES / "event_config.json").read_bytes(), before)

    def test_duplicate_config_keys_are_errors(self):
        with self.assertRaisesRegex(mod.InputError, "duplicate config key"):
            json.loads('{"steps": ["a"], "steps": ["b"]}', object_pairs_hook=mod.reject_duplicate_json_keys)

    def test_unterminated_csv_quote_is_rejected(self):
        content = 'event_id,unit_id,event,timestamp\ne1,u1,signup,"2026-01-01T00:00:00Z'
        with patch.object(Path, "open", return_value=io.StringIO(content)):
            with self.assertRaises(csv.Error):
                mod.read_events("not-written.csv")

    def test_valid_quoted_csv_still_works(self):
        content = 'event_id,unit_id,event,timestamp\n"e1","u1","signup","2026-01-01T00:00:00Z"\n'
        with patch.object(Path, "open", return_value=io.StringIO(content)):
            self.assertEqual(mod.read_events("not-written.csv")[0]["event_id"], "e1")

    def test_file_identity_alias_is_rejected_before_any_write(self):
        # Memory-level regression: no real hardlinks or source modifications.
        with patch.object(Path, "exists", return_value=True), patch.object(Path, "samefile", return_value=True), \
             patch.object(Path, "read_text") as read, patch.object(Path, "write_text") as write, redirect_stderr(io.StringIO()):
            code = mod.main(["--events", "events.csv", "--config", "config.json", "--out", "alias.json"])
        self.assertEqual(code, 2)
        read.assert_not_called()
        write.assert_not_called()


if __name__ == "__main__":
    unittest.main()
