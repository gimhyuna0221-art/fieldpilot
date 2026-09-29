from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]


class IndustryDepthBackstopContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        cls.mod = (ROOT / "references/modules/INDUSTRY_DEPTH_BACKSTOP.md").read_text(encoding="utf-8")
        cls.cont = (ROOT / "references/modules/DECISION_CONTINUITY.md").read_text(encoding="utf-8")
        cls.dev = (
            ROOT / "references/development/GENERAL_RESEARCH_VS_FIELDPILOT_2026-09-29.md"
        ).read_text(encoding="utf-8")

    def test_revision_and_wiring(self):
        self.assertIn(
            'industry_depth_extension_revision: "industry-depth-backstop-01"',
            self.skill,
        )
        self.assertIn("INDUSTRY_DEPTH_BACKSTOP.md", self.skill)
        self.assertIn("INDUSTRY_DEPTH_BACKSTOP.md", self.cont)
    def test_three_depth_states(self):
        for marker in [
            "NOT_NEEDED",
            "COMPACT_BACKSTOP",
            "DEEP_ESCALATION",
        ]:
            self.assertIn(marker, self.mod)

    def test_general_deep_research_strengths_are_covered(self):
        for marker in [
            "MARKET_BOUNDARY_AND_STRUCTURE",
            "MAGNITUDE_AND_GROWTH",
            "VENDOR_AND_PRICE_LADDER",
            "ENTERPRISE_OR_INFRASTRUCTURE_ALTERNATIVES",
            "SECURITY_REGULATORY_TECH_SHIFT",
            "LOCAL_GLOBAL_CONTEXT",
            "INDUSTRY_COUNTEREVIDENCE",
        ]:
            self.assertIn(marker, self.mod)

    def test_deep_escalation_is_conditional(self):
        self.assertIn("Deep-escalation triggers", self.mod)
        self.assertIn("capable of reversing the current decision", self.mod)
        self.assertIn("Narrow facts stay narrow", self.skill)
    def test_reuses_existing_methods_instead_of_second_methodology(self):
        for marker in [
            "sizing-and-segmentation.md",
            "secondary-and-competitors.md",
            "MARKET_PRIOR_AND_BASE_RATES.md",
            "LOCAL_AND_EXPERT_RESEARCH.md",
            "LIVE_TREND_AND_FRESHNESS_RADAR.md",
            "REGULATORY_CONTEXT_CHECK.md",
        ]:
            self.assertIn(marker, self.mod)
        self.assertIn("does not create a second research methodology", self.dev)

    def test_market_breadth_does_not_raise_commercial_claims(self):
        for marker in [
            "parent-market size → this product's market size",
            "category CAGR → demand for this product",
            "competitor absence → confirmed whitespace",
            "review/interest → purchase or WTP",
        ]:
            self.assertIn(marker, self.mod)

    def test_decision_first_surface_is_preserved(self):
        for marker in [
            "CURRENT_DECISION",
            "DECISIVE_EVIDENCE",
            "COUNTEREVIDENCE",
            "UNKNOWNS",
            "BUILD_CHANGE_OR_HOLD",
            "ONE_NEXT_ACTION",
        ]:
            self.assertIn(marker, self.mod)
    def test_general_ai_quality_check_is_bidirectional(self):
        self.assertIn("strong general deep-research report", self.mod)
        self.assertIn("Did the extra industry research actually change", self.mod)
        self.assertIn("do not dump the extra material", self.mod)

    def test_single_case_evidence_boundary(self):
        self.assertIn("controlled model benchmark", self.dev)
        self.assertIn("does not prove", self.dev)
        self.assertIn("Clean-session multi-task comparison", (ROOT / "CHANGELOG.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
