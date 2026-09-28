"""Check finite-source adoption coverage and file wiring, not semantic feature parity.

Offline and read-only. Does not fetch URLs, execute agents, assert vendor quality,
or certify that instructions produce good research. Use behavioral review separately.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys

LEVELS = {"EXISTING_METHOD", "NEW_METHOD", "SOURCE_CANDIDATE",
          "UNVERIFIED_REFERENCE", "OUT_OF_SCOPE_EXAMPLE", "SPECIALIST_HANDOFF"}
NEW_ROUTES = ("PRODUCT_ANALYTICS_EXECUTION.md", "SPECIALIST_ANALYSIS_EXECUTION.md",
              "SEARCH_AND_COMMERCE_EVIDENCE.md", "LOCAL_AND_EXPERT_RESEARCH.md")


def parse_inventory_markdown(content):
    """Read the approved source table directly; no duplicate JSON export needed."""
    rows, aliases = [], {}
    for number, line in enumerate(content.splitlines(), 1):
        if not line.lstrip().startswith("|"):
            if re.match(r"\s*(?:[`_*]+|<[^>]+>|\[)*[ECMX]\d", line):
                raise ValueError(f"Inventory line {number}: item requires a table row")
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 2 and re.fullmatch(r"[A-Z]+", cells[0]) and "references/" in cells[1]:
            aliases[cells[0]] = cells[1].strip("`")
        if not cells:
            continue
        match = re.match(r"([ECMX]\d{3})(?:<br>|:)", cells[0])
        if not match:
            if re.search(r"[ECMX]\d", cells[0]):
                raise ValueError(f"Inventory line {number}: unsupported or malformed item ID")
            continue
        ident = match.group(1)
        if len(cells) < 2:
            raise ValueError(f"Inventory line {number}: incomplete item row")
        if ident.startswith("E"):
            parts = cells[0].split("<br>", 2)
            if len(parts) != 3 or not all(part.strip() for part in parts):
                raise ValueError(f"Inventory line {number}: missing kind or name")
            kind, name = parts[1:]
        else:
            if ":" not in cells[0]:
                raise ValueError(f"Inventory line {number}: missing method/name separator")
            name = cells[0].split(":", 1)[1].split("<br>")[0].strip()
            kind = {"C": "additional_provider", "M": "method", "X": "context_only"}[ident[0]]
        if not name.strip() or not cells[1].strip():
            raise ValueError(f"Inventory line {number}: empty name or strength description")
        atoms = re.findall(r"\b" + ident + r"\.[a-z]\b", cells[1])
        if not atoms and not ident.startswith("X"):
            atoms = [ident + ".a"]
        rows.append({"id": ident, "name": name, "kind": kind, "atoms": atoms, "cells": cells})
    return {"rows": rows, "aliases": aliases}


def parse_adoption_markdown(content, inventory):
    match = re.search(r"inventory_sha256: ([0-9a-f]{64})", content)
    master = {r["id"]: r for r in inventory["rows"]}
    rows = []
    for number, line in enumerate(content.splitlines(), 1):
        if not line.lstrip().startswith("|"):
            if re.match(r"\s*(?:[`_*]+|<[^>]+>|\[)*[ECMX]\d", line):
                raise ValueError(f"Adoption line {number}: item requires a table row")
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 8 or not re.fullmatch(r"[ECMX]\d{3}", cells[0]):
            if cells and re.search(r"[ECMX]\d", cells[0]):
                raise ValueError(f"Adoption line {number}: malformed item row")
            continue
        ident, level, targets, atoms, decision, limit, verification, claims = cells
        rows.append({"id": ident, "name": master.get(ident, {}).get("name", "UNKNOWN"),
                     "adoption_level": level, "targets": [v.strip().strip("`") for v in targets.split("<br>") if v.strip() != "-"],
                     "atoms": [v.strip() for v in atoms.split(",") if v.strip() != "-"],
                     "decision": decision, "limitation": limit, "verification": verification,
                     "claims_full_equivalence": False if claims == "NO_EQUIVALENCE_NO_LIVE_INTEGRATION" else None,
                     "live_integration_verified": False if claims == "NO_EQUIVALENCE_NO_LIVE_INTEGRATION" else None})
    return {"inventory_sha256": match.group(1) if match else None, "rows": rows}


def validate(root, inventory, manifest, inventory_bytes):
    root = Path(root).resolve()
    errors = []
    inventory_rows = inventory.get("rows", [])
    rows = manifest.get("rows", [])
    if not inventory_rows or not rows:
        errors.append("Inventory and adoption rows must both be nonempty")
    for label, values in (("inventory", inventory_rows), ("adoption", rows)):
        ids = [r.get("id") for r in values]
        if any(not isinstance(i, str) or not i.strip() for i in ids):
            errors.append(f"{label}: missing/invalid ID")
        if len(set(map(str, ids))) != len(ids):
            errors.append(f"{label}: duplicate IDs")
    master = {r.get("id"): r for r in inventory_rows}
    actual = {r.get("id"): r for r in rows}
    if set(master) != set(actual):
        errors.append(f"ID coverage mismatch: missing={sorted(set(master)-set(actual), key=str)}, "
                      f"extra={sorted(set(actual)-set(master), key=str)}")
    digest = hashlib.sha256(inventory_bytes).hexdigest()
    if manifest.get("inventory_sha256") != digest:
        errors.append("Inventory hash changed: re-review source scope before adoption")
    for row in rows:
        ident = row.get("id", "?")
        if row.get("adoption_level") not in LEVELS:
            errors.append(f"{ident}: invalid adoption_level")
        for key in ("name", "decision", "limitation", "verification"):
            if not isinstance(row.get(key), str) or not row[key].strip():
                errors.append(f"{ident}: missing {key}")
        if ident in master and row.get("name") != master[ident].get("name"):
            errors.append(f"{ident}: name differs from supplied inventory")
        if ident in master and "atoms" in master[ident]:
            if sorted(row.get("atoms", [])) != sorted(master[ident]["atoms"]):
                errors.append(f"{ident}: atomic strength coverage mismatch")
        if row.get("claims_full_equivalence") is not False:
            errors.append(f"{ident}: cannot certify full commercial equivalence")
        if row.get("live_integration_verified") is not False:
            errors.append(f"{ident}: this candidate has no verified new live integration")
        targets = row.get("targets", [])
        if row.get("adoption_level") in {"EXISTING_METHOD", "NEW_METHOD", "SPECIALIST_HANDOFF"} and not targets:
            errors.append(f"{ident}: adopted method has no implementation target")
        for target in targets:
            if not isinstance(target, str):
                errors.append(f"{ident}: target is not a path")
                continue
            path = (root / target).resolve()
            if not path.is_relative_to(root):
                errors.append(f"{ident}: target escapes package")
            elif not path.is_file() or path.stat().st_size == 0:
                errors.append(f"{ident}: target missing/empty: {target}")
    kernel = root / "SKILL.md"
    skill = kernel.read_text(encoding="utf-8") if kernel.is_file() else ""
    for name in NEW_ROUTES:
        relative = "references/modules/" + name
        if relative not in skill or not (root / relative).is_file():
            errors.append(f"Conditional entry route not wired: {relative}")
    return {"status": "FAIL" if errors else "PASS", "inventory_sha256": digest,
            "inventory_rows": len(inventory_rows), "adoption_rows": len(rows),
            "atomic_strengths": sum(len(r.get("atoms", [])) for r in inventory_rows),
            "by_level": dict(sorted(Counter(r.get("adoption_level", "MISSING") for r in rows).items())),
            "errors": errors,
            "scope": "Supplied-item coverage and declared file wiring only; not feature equality, source truth, or customer-effect validation."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    args = parser.parse_args()
    try:
        raw = args.inventory.read_bytes()
        inventory_text = raw.decode("utf-8-sig")
        inventory = parse_inventory_markdown(inventory_text) if args.inventory.suffix.lower() == ".md" else json.loads(inventory_text)
        manifest_text = args.manifest.read_text(encoding="utf-8-sig")
        manifest = parse_adoption_markdown(manifest_text, inventory) if args.manifest.suffix.lower() == ".md" else json.loads(manifest_text)
        result = validate(args.root, inventory, manifest, raw)
    except (OSError, ValueError, TypeError, AttributeError) as exc:
        print(json.dumps({"status": "FAIL", "errors": [str(exc)]}, ensure_ascii=False))
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
