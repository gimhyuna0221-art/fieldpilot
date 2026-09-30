from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")

class DecisionDirectionContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = read("SKILL.md")
        cls.mod = read("references/modules/MARKET_DIRECTION_SYNTHESIS.md")
        cls.surfaces = read("references/modules/DECISION_SURFACES.md")
        cls.support = read("references/modules/DECISION_SUPPORT.md")
        cls.deliv = read("references/modules/MARKET_RESEARCH_DELIVERABLES.md")

    def test_revision_and_runtime_wiring(self):
        self.assertIn('direction_extension_revision: "decision-direction-01"', self.skill)
        self.assertIn("references/modules/MARKET_DIRECTION_SYNTHESIS.md", self.skill)
        self.assertIn("DECISION-DIRECTION-01", self.skill)

    def test_reuses_existing_decision_and_professional_controls(self):
        for marker in (
            "CLIENT_DECISION_BRIEF",
            "EVIDENCE_PLAN + COVERAGE_AUDIT",
            "EVIDENCE_TRACE",
            "COMPETITIVE_ALTERNATIVES",
            "PRODUCT_STATE",
            "CHANGE_OPTIONS",
            "COMPARE_VARIANTS",
            "DECISION_SUPPORT",
        ):
            self.assertIn(marker, self.mod)

    def test_direction_surface_is_decision_useful(self):
        for marker in (
            "MARKET_REALITY",
            "FEASIBLE_DIRECTIONS",
            "PRIMARY_DIRECTION",
            "WHY_PRIMARY_NOW",
            "ALTERNATIVE_DIRECTION",
            "AVOID_OR_DEFER",
            "REVERSAL_CONDITIONS",
            "NEXT_DISCRIMINATING_ACTION",
            "CLAIM_CEILING",
            "DIRECTION_UNRESOLVED",
        ):
            self.assertIn(marker, self.mod)

    def test_no_option_quota_or_synthetic_winner_score(self):
        for marker in (
            "There is no required option count",
            "Do not invent three directions",
            "No success probability",
            "viability score",
            "market score",
            "Do not force a winner",
        ):
            self.assertIn(marker.lower(), self.mod.lower())

    def test_direction_and_next_action_are_separate(self):
        self.assertIn("MARKET_DIRECTION", self.mod)
        self.assertIn("NEXT_DISCRIMINATING_ACTION", self.mod)
        self.assertIn("IMPACT_VERIFICATION", self.mod)

    def test_preserves_existing_change_and_alternative_logic(self):
        self.assertIn("CHANGE_OPTIONS", self.surfaces)
        self.assertIn("COMPARE_VARIANTS", self.surfaces)
        self.assertIn("ALTERNATIVE_DIRECTION_WORTH_TESTING", self.support)

    def test_full_report_has_direction_synthesis_slot(self):
        self.assertIn("Market Direction Synthesis", self.deliv)
        self.assertIn("primary direction", self.deliv.lower())
        self.assertIn("reversal", self.deliv.lower())

if __name__ == "__main__":
    unittest.main()
