from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class NarrowScopeCompletionContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        cls.cont = (ROOT / "references/modules/DECISION_CONTINUITY.md").read_text(encoding="utf-8")
        cls.prompt = (ROOT / "references/modules/PROMPT_SKILL_INDEPENDENCE.md").read_text(encoding="utf-8")

    def test_scope_lock_and_field_closure_are_paired(self):
        self.assertIn("Explicit scope lock + requested-field closure", self.skill)
        self.assertIn("REQUESTED_FIELD_CLOSURE", self.cont)
        self.assertIn("every literal requested field/entity pair", self.prompt)

    def test_unknown_is_not_early_stop_when_official_route_remains(self):
        for marker in [
            "current primary/official source route remains",
            "official help/billing/release documentation",
            "avoidable UNKNOWN is incomplete",
        ]:
            self.assertIn(marker, self.skill + self.prompt)

    def test_repair_does_not_widen_narrow_scope(self):
        for marker in [
            "Do not add adjacent market analysis",
            "total-cost scenarios",
            "upgrade-path advice",
            "Never compensate for a missing field by widening the answer",
        ]:
            self.assertIn(marker, self.cont)


if __name__ == "__main__":
    unittest.main()
