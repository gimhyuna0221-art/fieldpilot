from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]

class KoreaLocalCoverageContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        cls.korea = (ROOT / "references/modules/KOREA_LOCAL_DISTRIBUTION.md").read_text(encoding="utf-8")
        cls.reg = (ROOT / "references/modules/REGULATORY_CONTEXT_CHECK.md").read_text(encoding="utf-8")
        cls.comp = (ROOT / "references/methods/secondary-and-competitors.md").read_text(encoding="utf-8")
        cls.anchor = (ROOT / "references/modules/MARKET_ANCHOR_AND_EXPANSION.md").read_text(encoding="utf-8")

    def test_runtime_version_and_route(self):
        self.assertIn('version: "1.9.9-rc04"', self.skill)
        self.assertIn('market_anchor_extension_revision: "market-anchor-01"', self.skill)
        self.assertIn("Market anchor before geography questions", self.skill)
        self.assertIn("MARKET_ANCHOR_AND_EXPANSION.md", self.skill)
        self.assertIn("KOREA_LOCAL_DISTRIBUTION.md", self.skill)
        self.assertIn("REGULATORY_CONTEXT_CHECK.md", self.skill)

    def test_korean_language_is_provisional_search_prior_not_jurisdiction(self):
        self.assertIn("PROVISIONAL_KOREA_FIRST_PASS", self.korea)
        self.assertIn("search-order prior, not proof that Korea is the launch market", self.korea)
        self.assertIn("Do **not** treat Korean language alone as proof of", self.korea)
        self.assertIn("owner's current physical/device/account location", self.korea)
        self.assertIn("Korean with no contrary case evidence -> provisional South Korea", self.anchor)

    def test_local_competitor_classes_are_forced_when_korea_known(self):
        for marker in [
            "KOREA_LOCAL_DIRECT",
            "KOREA_LOCAL_ADJACENT_OR_BUNDLED",
            "KOREA_LOCAL_MANUAL_OR_INTERNAL",
            "KOREA_LOCAL_DO_NOTHING",
            "LOCAL_DIRECT_SEARCHED_NOT_FOUND",
        ]:
            self.assertIn(marker, self.korea)
        self.assertIn("LOCAL_GEOGRAPHY_CLOSURE", self.comp)
        self.assertIn("LOCAL_DIRECT_SEARCHED_NOT_FOUND", self.comp)

    def test_korea_channels_are_conditional_not_demand_proof(self):
        self.assertIn("Naver Search / DataLab / Ads Keyword Tool / Blog / Cafe", self.korea)
        self.assertIn("Kakao communities / Open Chat / local messaging networks", self.korea)
        self.assertIn("separate access from demand", self.korea)

    def test_korea_privacy_route_uses_official_sources_and_claim_ceiling(self):
        for marker in [
            "KOREA_DATA_FACT_PATTERN",
            "KOREA_PROCESSING_OR_ENTRUSTMENT",
            "KOREA_OVERSEAS_TRANSFER",
            "국가법령정보센터",
            "개인정보보호위원회",
            "law.go.kr",
            "pipc.go.kr",
        ]:
            self.assertIn(marker, self.reg)
        self.assertIn("not legal advice", self.reg.lower())
        self.assertIn("freshness anchors, not permanent memory", self.reg)

    def test_no_language_to_confirmed_korea_assumption(self):
        bad = re.compile(r"한국(어)?(?:\s*사용자|\s*대화).{0,30}(?:따라서|이므로).{0,30}(?:확정|confirmed|법적|관할).*한국", re.S | re.I)
        self.assertIsNone(bad.search(self.skill + "\n" + self.korea))
        self.assertIn("Language is a search prior, never geography proof", self.skill)

if __name__ == "__main__":
    unittest.main()
