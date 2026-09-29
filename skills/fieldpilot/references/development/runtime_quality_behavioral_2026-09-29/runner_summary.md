# FieldPilot Runtime Quality Behavioral Runner 01

RUN: RUN-P007-20260929-FIELDPILOT-RUNTIME-BEHAVIOR-RUNNER01
CLAIM: CLAIM-P007-FIELDPILOT-RUNTIME-BEHAVIOR-RUNNER01
ROLE: capture-only runner; no behavioral promotion verdict
CANDIDATE_COMMIT: f3dc869b032091d611dfa016007d2612bdd2fb03
PR: #6
EVIDENCE_BRANCH: evidence/runtime-quality-behavior01

## Baseline and isolation

- PR #6 was verified open / draft / unmerged / mergeable before execution.
- Base was feat/locale-first-market-anchor @ c59dc56c6765cdaf3d69bf4b5398486bb96cfa06.
- Head was worker/fieldpilot-runtime-quality-floor01 @ f3dc869b032091d611dfa016007d2612bdd2fb03.
- GitHub Actions artifact 11027757355 from run 36556191121 was tied to exact head f3dc869b032091d611dfa016007d2612bdd2fb03.
- The packaged FieldPilot ZIP SHA-256 was 6299987546ed93b7124af5b8bdbba6f2e9623ffd82f393085381a5f700737216.
- GitHub compare f3dc869... -> merge-test e66559f... reported zero changed files.
- Local isolated candidate reconstruction verified 136 expected files / 136 staged files / 0 SHA-256 mismatches.
- Project-local skill path: C:\Users\rlagu\AppData\Local\Temp\fieldpilot-runtime-behavior01\project\.claude\skills\fieldpilot\SKILL.md
- runtime_quality_extension_revision: runtime-quality-floor-01
- market_anchor_extension_revision: market-anchor-01

## Mechanical execution record

| Case | Model observed | Runtime | Runner state |
|---|---|---|---|
| RQ1_STRONG_LIVE_KO | claude-sonnet-5-5 | live web | CAPTURED |
| RQ2_WEAK_LIVE_KO | claude-haiku-4-5-20251001 | live web | CONTAMINATED — do not count |
| RQ3_NARROW_OFFICIAL | — | — | NOT_RUN after blocking contamination |
| RQ4_NO_WEB | — | — | NOT_RUN after blocking contamination |
| RQ5_SOURCE_BOUND | — | — | NOT_RUN after blocking contamination |
| RQ6_LOCALE_KO_NO_COUNTRY | — | — | NOT_RUN after blocking contamination |
| RQ7A_EXPLICIT_US_OVERRIDE | — | — | NOT_RUN after blocking contamination |
| RQ7B_EXPLICIT_KR_OVERRIDE | — | — | NOT_RUN after blocking contamination |

RQ1 raw reply SHA-256: ffc51ab3e0fbca951f8411ad39a846abf755b162a053bbfbe78d48828a607d40

RQ2 raw reply SHA-256: b52d75c3a0914ef56973471a1923423148c39a82c9e7c0e162ef011b980774f8

## Blocking contamination-control event

RQ2 returned exit code 0 from genuine Haiku, but its first complete reply did not emit the required SELF_CHECK. The durable manifest therefore has loaded_skill_path = null, runtime_quality_extension_revision = null, market_anchor_extension_revision = null, and contaminated = true. The first complete reply is preserved verbatim and is not rerun or hand-edited.

Because this runner is capture-only and the frozen protocol requires a fresh first reply, the run stopped instead of retrying RQ2 to obtain a more favorable output.

## Harness note

An earlier Sonnet preflight attempt was invalid because WebSearch was denied by the harness permission mode. That invalid attempt was discarded and is not counted as behavioral evidence. The corrected harness explicitly allowed Read/Glob/Grep/WebSearch/WebFetch; the valid RQ1 manifest records actual WebSearch/WebFetch activity.

## Scope preserved

No FieldPilot implementation, tests, SKILL.md, public copy, PR #5, or PR #6 code was edited.
No merge, release, listing, purchase, top-up, auto-reload, or publication occurred.
No behavioral promotion verdict is made here.
