from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class MarketAnchorContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        cls.anchor = (
            ROOT / "references/modules/MARKET_ANCHOR_AND_EXPANSION.md"
        ).read_text(encoding="utf-8")
        cls.prompt = (
            ROOT / "references/modules/PROMPT_SKILL_INDEPENDENCE.md"
        ).read_text(encoding="utf-8")
        cls.korea = (
            ROOT / "references/modules/KOREA_LOCAL_DISTRIBUTION.md"
        ).read_text(encoding="utf-8")
        cls.comp = (
            ROOT / "references/methods/secondary-and-competitors.md"
        ).read_text(encoding="utf-8")

    def test_revision_and_wiring(self):
        self.assertIn('market_anchor_extension_revision: "market-anchor-01"', self.skill)
        self.assertIn("MARKET_ANCHOR_AND_EXPANSION.md", self.skill)
        self.assertIn("LOCAL-FIRST → GLOBAL-BEST → LOCAL-TRANSFER", self.skill)
    def test_anchor_precedence(self):
        for marker in [
            "EXPLICIT_MARKET",
            "VERIFIED_CASE_MARKET",
            "STRONG_LOCAL_SIGNAL",
            "PROVISIONAL_LANGUAGE_MARKET",
            "LANGUAGE_CLUSTER",
            "GLOBAL_UNRESOLVED",
            "Higher-precedence evidence always overrides lower-precedence priors",
        ]:
            self.assertIn(marker, self.anchor)

    def test_language_is_prior_not_geography_proof(self):
        self.assertIn("Language is a search prior, not geography proof", self.anchor)
        self.assertIn("Korean with no contrary case evidence -> provisional South Korea", self.anchor)
        self.assertIn("Japanese with no contrary case evidence -> provisional Japan", self.anchor)
        self.assertIn("English -> English-speaking/global cluster", self.anchor)
        self.assertIn("never default to the United States", self.anchor)
        self.assertIn("Spanish -> Spanish-speaking cluster", self.anchor)

    def test_private_or_incidental_location_is_not_used(self):
        for marker in [
            "account country",
            "device/physical location",
            "remembered owner location",
            "IP-derived location",
        ]:
            self.assertIn(marker, self.anchor)
    def test_local_global_transfer_chain(self):
        for marker in [
            "## 3. Local-first research",
            "## 4. Global-best expansion",
            "## 5. Local-transfer gate",
            "LOCAL_PRICE_PURCHASING_CONTEXT",
            "LOCAL_PLATFORM_DISTRIBUTION_MATCH",
            "LOCAL_REGULATORY_CERTIFICATION_MATCH",
            "TRANSFER_STATE = DIRECT / PLAUSIBLE_WITH_CAVEATS / WEAK_PROXY / NOT_TRANSFERABLE / UNKNOWN",
        ]:
            self.assertIn(marker, self.anchor)

    def test_foreign_evidence_cannot_become_local_fact(self):
        for marker in [
            "a US $50 product does not establish a Korean ₩70,000 market",
            "US adoption does not establish Korean demand",
            "foreign price -> local WTP",
            "foreign market size -> local market size",
        ]:
            self.assertIn(marker, self.anchor)

    def test_geography_question_is_deferred_until_after_useful_research(self):
        self.assertIn('Do not ask "which country?" merely because geography was not explicitly stated', self.anchor)
        self.assertIn("perform the useful first-pass research", self.anchor)
        self.assertIn("ask a geography question only if", self.anchor)
        self.assertIn("Do useful local/language-first research", self.prompt)
    def test_korea_has_full_and_provisional_modes(self):
        for marker in [
            "FULL_KOREA_CLOSURE",
            "PROVISIONAL_KOREA_FIRST_PASS",
            "search-order prior, not proof that Korea is the launch market",
            "Do **not** treat Korean language alone as proof of",
        ]:
            self.assertIn(marker, self.korea)

    def test_competitor_method_routes_unresolved_geography_through_anchor(self):
        self.assertIn("MARKET_ANCHOR_AND_EXPANSION.md", self.comp)
        self.assertIn("English and other multinational languages use a language cluster", self.comp)
        self.assertIn("PROVISIONAL_MARKET_ANCHOR", self.comp)


if __name__ == "__main__":
    unittest.main()
