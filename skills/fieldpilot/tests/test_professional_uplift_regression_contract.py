from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")

class ProfessionalUpliftRegressionContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.brief = read("references/delivery/CLIENT_DECISION_BRIEF.md")
        cls.plan = read("references/delivery/EVIDENCE_PLAN_AND_COVERAGE_AUDIT.md")
        cls.envelope = read("references/delivery/PROFESSIONAL_DELIVERY_ENVELOPE.md")
        cls.exec_layer = read("references/delivery/EXECUTIVE_DECISION_AND_IMPACT_LAYER.md")
        cls.deliv = read("references/modules/MARKET_RESEARCH_DELIVERABLES.md")
        cls.sample = read("references/core/SAMPLE_AND_FIELDWORK.md")

    def test_p0_1_client_decision_brief_survives(self):
        for marker in (
            "decision_to_be_made",
            "decision_owner_or_primary_user",
            "decision_horizon_or_deadline",
            "stakes_or_cost_of_wrong_decision",
            "primary_research_objective",
            "secondary_research_questions",
            "scope_in",
            "scope_out",
            "what_evidence_would_change_the_decision",
            "intended_action_or_choice_set",
            "desired_decision_effect",
            "STATED",
            "INFERRED",
            "ASSUMED",
            "UNRESOLVED",
            "ask only decision-changing questions",
            "frozen",
        ):
            self.assertIn(marker.lower(), self.brief.lower())

    def test_p0_2_evidence_plan_and_coverage_audit_survive(self):
        for marker in (
            "uncertainty_to_resolve",
            "method_or_source_class",
            "why_fit_for_purpose",
            "target_population_or_source_universe",
            "coverage_segment",
            "coverage_geography",
            "coverage_time_period",
            "evidence_independence",
            "known_weakness_or_bias",
            "triangulation_partner",
            "alternative_explanation_check",
            "sufficiency_rule",
            "stop_rule",
            "ANSWERED",
            "PARTIAL",
            "UNKNOWN",
            "No arbitrary minimum source counts",
            "Source count is not coverage",
        ):
            self.assertIn(marker.lower(), self.plan.lower())

    def test_p0_3_professional_delivery_envelope_survives(self):
        for marker in (
            "agreed brief",
            "scope",
            "exclusions",
            "assumptions",
            "method-selection rationale",
            "source-selection rationale",
            "coverage rationale",
            "provenance register",
            "limitations",
            "unknowns",
            "causal boundaries",
            "AI / synthetic / tool disclosure",
            "human oversight & accountability",
            "freshness QA",
            "dedup QA",
            "inclusion / exclusion QA",
            "verification QA",
            "sample QC",
            "fieldwork QC",
            "ethics boundary",
            "privacy boundary",
            "confidentiality boundary",
            "reproducibility notes",
            "traceability notes",
            "Never fabricate",
            "NONE",
            "FINDINGS",
            "INTERPRETATION",
            "RECOMMENDATIONS",
        ):
            self.assertIn(marker.lower(), self.envelope.lower())

    def test_p1_1_executive_decision_layer_survives(self):
        for marker in (
            "DECISION",
            "DIRECT ANSWER",
            "DECISIVE INSIGHTS",
            "RECOMMENDATIONS",
            "CONFIDENCE",
            "COUNTEREVIDENCE",
            "LIMITATIONS",
            "NEXT VERIFICATION",
            "blind reader",
        ):
            self.assertIn(marker.lower(), self.exec_layer.lower())

    def test_p1_2_impact_verification_chain_survives(self):
        for marker in (
            "ACTION",
            "MECHANISM",
            "OBSERVABLE METRIC",
            "MEASUREMENT CONTEXT",
            "DECISION CHECK",
            "CAUSAL CAVEAT",
            "No invented thresholds",
        ):
            self.assertIn(marker.lower(), self.exec_layer.lower())
        self.assertIn(
            "ACTION -> MECHANISM -> OBSERVABLE METRIC/STATE -> MEASUREMENT CONTEXT -> DECISION CHECK -> CAUSAL CAVEAT",
            self.deliv,
        )

    def test_p1_3_negative_evidence_and_falsifier_are_regression_protected(self):
        for marker in (
            "negative evidence",
            "why this may not need to exist",
            "general AI",
            "manual workarounds",
            "do-nothing",
            "falsifier",
            "reversal conditions",
            "STOP",
            "HOLD",
            "PIVOT",
            "preserved behavior governs",
        ):
            self.assertIn(marker.lower(), self.exec_layer.lower())

    def test_p1_4_direct_research_design_and_qc_survive(self):
        combined = (self.deliv + "\n" + self.sample + "\n" + self.envelope).lower()
        for marker in (
            "target population",
            "eligibility",
            "exclusions",
            "sampling frame",
            "saturation",
            "consent",
            "privacy",
            "fieldwork qc",
            "invalid-response",
            "deviation log",
            "analysis",
            "generalization",
            "skip",
        ):
            self.assertIn(marker, combined)
        self.assertTrue(\n            "sample-size" in combined or "sample size" in combined or "n or saturation rationale" in combined,\n            "direct-research QC must preserve a sample-size or saturation rationale",\n        )\n\n    def test_professional_controls_are_wired_into_current_deliverable(self):
        for marker in (
            "references/delivery/CLIENT_DECISION_BRIEF.md",
            "references/delivery/EVIDENCE_PLAN_AND_COVERAGE_AUDIT.md",
            "PROFESSIONAL_DELIVERY_ENVELOPE",
            "Executive Decision Layer",
            "Coverage Audit",
        ):
            self.assertIn(marker.lower(), self.deliv.lower())

if __name__ == "__main__":
    unittest.main()
