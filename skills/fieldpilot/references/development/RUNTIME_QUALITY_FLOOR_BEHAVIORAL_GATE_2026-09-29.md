# Runtime Quality Floor Behavioral Gate — 2026-09-29

RUN: RUN-P007-20260929-FIELDPILOT-RUNTIME-QUALITY-FLOOR01
CLAIM: CLAIM-P007-FIELDPILOT-RUNTIME-QUALITY-FLOOR01
CANDIDATE_BRANCH: worker/fieldpilot-runtime-quality-floor01
IMPLEMENTATION_BASE: c59dc56c6765cdaf3d69bf4b5398486bb96cfa06
STATIC_VALIDATED_HEAD_BEFORE_THIS_NOTE: 8b36e8e0910133cc69ff9d9ef30c9ffb699a1146
DRAFT_PR: #6 -> feat/locale-first-market-anchor

## What is durable

Frozen behavioral inputs:
- `tests/runtime_quality/cases.json`
- `tests/runtime_quality/README.md`

Required protocol explicitly forbids simulating a weaker model with the same model and requires fresh sessions with verbatim raw outputs.

Raw outputs:
- NONE.
- No model output file was fabricated or hand-authored to satisfy the gate.

## Static evidence already passed

GitHub Actions run: 36556034967
Job: 109365288049

- git diff --check: PASS
- targeted runtime-quality and required regression contracts: 112 tests, PASS
- full unittest discovery: 252 tests, PASS
- package step: PASS
- artifact manifest on the PR merge test commit reported quality_policy MAXIMIZE_QUALITY_BEFORE_USAGE and behavioral_external_comparison NOT_RUN_ON_THIS_REVISION.

Static PASS does not satisfy the behavioral gate.

## Mandatory behavioral matrix

| case | required environment | status | reason |
|---|---|---|---|
| RQ1_STRONG_LIVE_KO | fresh strong model + live web | NOT_RUN | no clean independent model-session runner is exposed in this execution environment |
| RQ2_WEAK_LIVE_KO | fresh genuinely weaker model + live web | NOT_RUN | no genuine weaker-model runner is exposed; same-model role-play is prohibited |
| RQ3_NARROW_OFFICIAL | fresh live-web session | NOT_RUN | implementation conversation is not a fresh behavioral session and cannot be counted |
| RQ4_NO_WEB | fresh no-web session | NOT_RUN | no isolated session/tool-disable harness is exposed |
| RQ5_SOURCE_BOUND | fresh source-bound session | NOT_RUN | no isolated source-bound session harness is exposed |
| RQ6_LOCALE_KO_NO_COUNTRY | fresh live-web session | NOT_RUN | no isolated fresh-session model runner is exposed |
| RQ7A_EXPLICIT_US_OVERRIDE | fresh live-web session | NOT_RUN | no isolated fresh-session model runner is exposed |
| RQ7B_EXPLICIT_KR_OVERRIDE | fresh live-web session | NOT_RUN | no isolated fresh-session model runner is exposed |

## Gate outcome

BLOCKED_TOOL_OR_ACCESS.

The candidate implementation and static contract evidence are available for CENTRAL review, but this RUN must not claim RUNTIME_QUALITY_CANDIDATE_READY because the mandatory strong/weak/live/no-web/source-bound/narrow/locale behavior matrix has not actually executed.

No merge, release, listing, paid purchase, or Remote Desktop Commander use occurred.
