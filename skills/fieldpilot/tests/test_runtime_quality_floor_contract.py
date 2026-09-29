from pathlib import Path
import json
import unittest

ROOT = Path(__file__).resolve().parents[1]


class RuntimeQualityFloorContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
        cls.mod = (ROOT / 'references/modules/RUNTIME_QUALITY_FLOOR.md').read_text(encoding='utf-8')
        cls.prop = (ROOT / 'references/core/PROPOSITION_AND_EVIDENCE.md').read_text(encoding='utf-8')
        cls.cases = json.loads((ROOT / 'tests/runtime_quality/cases.json').read_text(encoding='utf-8'))

    def test_revision_and_wiring(self):
        self.assertIn('runtime_quality_extension_revision: "runtime-quality-floor-01"', self.skill)
        self.assertIn('RUNTIME_QUALITY_FLOOR.md', self.skill)
        self.assertIn('RUNTIME-QUALITY-FLOOR-01', self.skill)

    def test_access_states_are_host_neutral(self):
        for marker in ('LIVE_FULL', 'LIVE_PARTIAL', 'SOURCE_BOUND', 'OFFLINE_REASONING'):
            self.assertIn(marker, self.mod)
        self.assertIn('decision-material source class is unreachable', self.mod)
        self.assertIn('Do not ask the user which model, subscription, plan or host', self.mod)
        self.assertIn('never from the model/provider name', self.skill)

    def test_source_receipt_classes_and_ceiling(self):
        for marker in ('READ_ORIGINAL', 'SEARCH_GROUNDED_SNIPPET',
                       'VERIFIED_REUSED_OR_USER_SUPPLIED', 'MEMORY_ONLY_OR_NOT_RETRIEVED'):
            self.assertIn(marker, self.mod)
        for marker in ('A plausible URL is never READ_ORIGINAL', 'Search discovery is not content retrieval',
                       'do not call the claim fully verified from search-only evidence',
                       'research_receipts.py', 'CLIENT_VISIBLE_EVIDENCE_PROVENANCE',
                       'PROPOSITION_AND_EVIDENCE'):
            self.assertIn(marker, self.mod)

    def test_sellability_rungs_do_not_promote_wtp(self):
        for marker in ('MARKET_EXISTENCE', 'THIS_PRODUCT_DEMAND', 'ACTUAL_PAYMENT_OR_WTP'):
            self.assertIn(marker, self.mod)
        for marker in ('market size', 'CAGR', 'problem severity', 'ROI', 'stated interest'):
            self.assertIn(marker, self.mod)
        self.assertIn('without eligible observed payment, ACTUAL_PAYMENT_OR_WTP remains UNVERIFIED', self.mod)
        self.assertIn('STATED_WTP remains stated evidence', self.mod)

    def test_no_synthetic_business_score(self):
        for marker in ('build/recommendation percentage', 'success probability', 'market score out of 10',
                       'actual observed metric', 'denominator'):
            self.assertIn(marker, self.mod)

    def test_no_homework_before_accessible_evidence(self):
        for marker in ('official/public sources', 'accessible reviews/community evidence',
                       'lawful product-trial evidence', 'Never impose a universal interview threshold',
                       '5–10 interviews'):
            self.assertIn(marker, self.mod)

    def test_narrow_scope_suppresses_adjacent_analysis(self):
        narrow = self.mod.split('## 7. Narrow-scope protection')[1].split('## 8.')[0]
        for marker in ('requested-field closure', 'PRESENT / BLOCKED / UNKNOWN', 'sellability', 'WTP',
                       'strategy', 'follow-up questions', 'full-report offer'):
            self.assertIn(marker, narrow)

    def test_graceful_degradation_is_compact(self):
        for marker in ('state the access limitation once', 'answer supported parts normally',
                       'wall of UNKNOWN', 'hypotheses', 'open-ended rewrite loop'):
            self.assertIn(marker, self.mod)

    def test_public_copy_does_not_claim_model_equivalence(self):
        for marker in ('same essential checks and claim limits', 'Stronger models can still search, compare and reason better',
                       'FORBIDDEN_PUBLIC_CLAIMS', 'guaranteed same quality across models',
                       'guaranteed token, cost or time savings'):
            self.assertIn(marker, self.mod)

    def test_locale_prior_is_not_confirmed_geography(self):
        prop_flat = ' '.join(self.prop.lower().split())
        self.assertIn('conversation language may supply only the provisional search prior', prop_flat)
        self.assertIn('never confirms proposition geography, jurisdiction, customer location, or launch market', prop_flat)
        self.assertIn('Explicit market overrides language', self.mod)
        self.assertIn('Language remains a search prior, never jurisdiction proof', self.mod)

    def test_behavioral_matrix_is_frozen_and_complete(self):
        ids = {c['id'] for c in self.cases['cases']}
        required = {'RQ1_STRONG_LIVE_KO', 'RQ2_WEAK_LIVE_KO', 'RQ3_NARROW_OFFICIAL',
                    'RQ4_NO_WEB', 'RQ5_SOURCE_BOUND', 'RQ6_LOCALE_KO_NO_COUNTRY',
                    'RQ7A_EXPLICIT_US_OVERRIDE', 'RQ7B_EXPLICIT_KR_OVERRIDE'}
        self.assertEqual(ids, required)
        self.assertEqual(self.cases['skill_revision'], 'runtime-quality-floor-01')


if __name__ == '__main__':
    unittest.main()
