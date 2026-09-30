from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")

class EvidenceOpportunityContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = read("SKILL.md")
        cls.source = read("references/modules/SOURCE_DISCOVERY_AND_SELECTION.md")
        cls.continuity = read("references/modules/DECISION_CONTINUITY.md")
        cls.competitors = read("references/methods/secondary-and-competitors.md")
        cls.trend = read("references/modules/LIVE_TREND_AND_FRESHNESS_RADAR.md")
        cls.direction = read("references/modules/MARKET_DIRECTION_SYNTHESIS.md")
        cls.reference = read("references/modules/REFERENCE_FIRST_VALUE.md")

    def test_revision_and_kernel_wiring(self):
        self.assertIn('evidence_opportunity_extension_revision: "evidence-opportunity-01"', self.skill)
        self.assertIn("## EVIDENCE-OPPORTUNITY-01", self.skill)
        for marker in (
            "decision-value triage",
            "DIY_WITH_AI",
            "MARKET_DISPLACEMENT_TRIGGER",
            "no persistent crawler/database",
        ):
            self.assertIn(marker.lower(), self.skill.lower())

    def test_evidence_triage_preserves_recall_and_receipt_ceiling(self):
        for marker in (
            "DISCOVERED_CANDIDATE",
            "QUICK_SCREENED",
            "DEEP_READ_REQUIRED",
            "EXCLUDED_DUPLICATE",
            "EXCLUDED_OUT_OF_SCOPE",
            "EXCLUDED_LOW_DECISION_VALUE",
            "ADMITTED_EVIDENCE",
            "Quick-screen material is discovery evidence only",
            "Recall safeguard",
            "new alternative",
            "counterevidence",
            "primary source",
            "displacement event",
        ):
            self.assertIn(marker.lower(), self.source.lower())
        self.assertIn("decision-value triage", self.continuity.lower())
        self.assertIn("quick-screen", self.continuity.lower())
        self.assertIn("deep-read", self.continuity.lower())

    def test_diy_with_ai_is_distinct_substitute_not_magic_code_generation(self):
        for marker in (
            "DIY_WITH_AI",
            "coding/building agents",
            "setup/specification/prompting burden",
            "build/debug/QA",
            "maintenance",
            "hosting/infrastructure",
            "support burden",
            "data, integration, security",
            "generated prototype",
            "plausible/UNVERIFIED",
        ):
            self.assertIn(marker.lower(), self.competitors.lower())
        self.assertIn("DIY_WITH_AI", self.continuity)
        self.assertIn("DIY_WITH_AI", self.reference)
        self.assertIn("DIY_WITH_AI", self.direction)

    def test_market_displacement_trigger_is_bounded_signal(self):
        for marker in (
            "MARKET_DISPLACEMENT_TRIGGER",
            "PRODUCT_RETIREMENT_OR_SHUTDOWN",
            "FEATURE_REMOVAL",
            "PRICE_INCREASE",
            "FREE_TO_PAID",
            "PLAN_LIMIT_TIGHTENING",
            "API_DEPRECATION_OR_ACCESS_RESTRICTION",
            "POLICY_OR_REGULATORY_CHANGE",
            "announced",
            "effective",
            "completed",
            "not that users want the user's product",
            "will pay",
            "current substitutes",
            "WHY_NOW",
            "MARKET_DIRECTION_SYNTHESIS",
        ):
            self.assertIn(marker.lower(), self.trend.lower())

    def test_direction_synthesis_consumes_but_does_not_overclaim_new_signals(self):
        for marker in (
            "DIY_WITH_AI",
            "MARKET_DISPLACEMENT_TRIGGER",
            "retirement",
            "feature/price/plan/API/policy change",
            "does not prove demand or payment",
        ):
            self.assertIn(marker.lower(), self.direction.lower())

    def test_no_efficiency_regression_to_fixed_quotas_or_always_on_monitoring(self):
        self.assertIn("No minimum source count", self.source)
        self.assertIn("This triage is an efficiency control only", self.source)
        self.assertIn("do not create an always-on monitor", self.trend.lower())
        self.assertIn("no persistent crawler/database", self.skill.lower())

if __name__ == "__main__":
    unittest.main()
