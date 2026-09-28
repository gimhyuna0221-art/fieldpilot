import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("coverage_check", ROOT / "tools/competitor_coverage_check.py")
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class CoverageHarnessTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        modules = self.root / "references/modules"
        modules.mkdir(parents=True)
        for name in checker.NEW_ROUTES:
            (modules / name).write_text("Scoped method", encoding="utf-8")
        (self.root / "SKILL.md").write_text("\n".join("references/modules/" + n for n in checker.NEW_ROUTES), encoding="utf-8")
        self.inventory = {"rows": [{"id": "E001", "name": "Example provider"}]}
        self.raw = json.dumps(self.inventory).encode()
        self.manifest = {"inventory_sha256": hashlib.sha256(self.raw).hexdigest(), "rows": [{
            "id": "E001", "name": "Example provider", "adoption_level": "NEW_METHOD",
            "decision": "Reuse a bounded method", "limitation": "No live account",
            "verification": "Separate behavioral review required", "claims_full_equivalence": False,
            "live_integration_verified": False, "targets": ["references/modules/PRODUCT_ANALYTICS_EXECUTION.md"]}]}

    def result(self):
        return checker.validate(self.root, self.inventory, self.manifest, self.raw)

    def test_valid_declared_coverage(self):
        self.assertEqual(self.result()["status"], "PASS")

    def test_missing_item_fails(self):
        self.manifest["rows"] = []
        self.assertEqual(self.result()["status"], "FAIL")

    def test_duplicate_item_fails(self):
        self.manifest["rows"].append(copy.deepcopy(self.manifest["rows"][0]))
        self.assertEqual(self.result()["status"], "FAIL")

    def test_unlisted_extra_item_fails(self):
        row = copy.deepcopy(self.manifest["rows"][0]); row["id"] = "E999"
        self.manifest["rows"].append(row)
        self.assertEqual(self.result()["status"], "FAIL")

    def test_inventory_revision_fails(self):
        self.raw += b"\n"
        self.assertEqual(self.result()["status"], "FAIL")

    def test_missing_target_fails(self):
        self.manifest["rows"][0]["targets"] = ["references/missing.md"]
        self.assertEqual(self.result()["status"], "FAIL")

    def test_path_escape_fails(self):
        self.manifest["rows"][0]["targets"] = ["../outside.md"]
        self.assertTrue(any("escapes" in e for e in self.result()["errors"]))

    def test_unwired_route_fails(self):
        (self.root / "SKILL.md").write_text("No entry route", encoding="utf-8")
        self.assertEqual(self.result()["status"], "FAIL")

    def test_parity_claim_fails(self):
        self.manifest["rows"][0]["claims_full_equivalence"] = True
        self.assertEqual(self.result()["status"], "FAIL")

    def test_renamed_scope_fails(self):
        self.manifest["rows"][0]["name"] = "Another provider"
        self.assertEqual(self.result()["status"], "FAIL")

    def test_wrong_status_fails(self):
        self.manifest["rows"][0]["adoption_level"] = "EVERYTHING_IMPLEMENTED"
        self.assertEqual(self.result()["status"], "FAIL")

    def test_markdown_inventory_keeps_types_atoms_and_paths(self):
        data = checker.parse_inventory_markdown(
            "| E001<br>provider<br>Provider | E001.a: first<br>E001.b: second | A | gap | A:1 | P |\n"
            "| M001: Method | useful | A | gap | B:1 | U |\n"
            "| X001: Example | example | A:2 | context |\n"
            "| A | `references/modules/RESEARCH_ANALYSIS_COMPILER.md` |\n")
        self.assertEqual([r["id"] for r in data["rows"]], ["E001", "M001", "X001"])
        self.assertEqual(data["rows"][0]["atoms"], ["E001.a", "E001.b"])
        self.assertEqual(data["rows"][1]["atoms"], ["M001.a"])
        self.assertEqual(data["rows"][2]["atoms"], [])
        self.assertEqual(data["aliases"]["A"], "references/modules/RESEARCH_ANALYSIS_COMPILER.md")

    def test_atomic_omission_fails_even_when_parent_present(self):
        self.inventory["rows"][0]["atoms"] = ["E001.a", "E001.b"]
        self.manifest["rows"][0]["atoms"] = ["E001.a"]
        self.assertTrue(any("atomic strength" in e for e in self.result()["errors"]))

    def test_atomic_duplicate_fails(self):
        self.inventory["rows"][0]["atoms"] = ["E001.a"]
        self.manifest["rows"][0]["atoms"] = ["E001.a", "E001.a"]
        self.assertEqual(self.result()["status"], "FAIL")

    def test_live_integration_claim_fails(self):
        self.manifest["rows"][0]["live_integration_verified"] = True
        self.assertEqual(self.result()["status"], "FAIL")

    def test_decorated_inventory_id_cannot_silently_disappear(self):
        for decorated in ["`E002`", "__E002__", "**E002**", "<code>E002</code>", "[E002](#)"]:
            content = f"| E001<br>provider<br>Alpha | E001.a: strength |\n| {decorated}<br>provider<br>Beta | E002.a: strength |"
            with self.subTest(decorated=decorated), self.assertRaisesRegex(ValueError, "line 2"):
                checker.parse_inventory_markdown(content)

    def test_incomplete_inventory_items_fail_closed(self):
        for line in ["| E001<br>provider | strength |", "| E001<br>provider<br>Name |",
                     "| M001: | strength |", "| M1: Method | strength |", "| C001<br>Name | strength |"]:
            with self.subTest(line=line), self.assertRaises(ValueError):
                checker.parse_inventory_markdown(line)

    def test_malformed_adoption_row_cannot_silently_disappear(self):
        with self.assertRaisesRegex(ValueError, "Adoption line 1"):
            checker.parse_adoption_markdown("| `E001` | NEW_METHOD | too few cells |", self.inventory)

    def test_missing_table_delimiter_does_not_hide_item(self):
        with self.assertRaisesRegex(ValueError, "table row"):
            checker.parse_inventory_markdown("__E002__<br>provider<br>Beta | E002.a: strength |")
        with self.assertRaisesRegex(ValueError, "table row"):
            checker.parse_adoption_markdown("E002 | NEW_METHOD | incomplete |", self.inventory)


if __name__ == "__main__":
    unittest.main()
