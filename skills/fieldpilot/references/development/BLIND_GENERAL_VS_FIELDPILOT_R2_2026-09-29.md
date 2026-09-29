# Blind General Claude vs FieldPilot R2 — 2026-09-29

## Status

R2 materially improved broad-market performance but **failed the frozen promotion gate** because the narrow-control case lost one of two blind judgments.

Do not merge PR #4 on R2 alone.

## Setup

- Frozen R1 baseline reused; no baseline regeneration.
- Treatment: `industry-depth-backstop-02`.
- Same Claude Sonnet / high-effort / fresh non-persistent generation setup.
- Four treatment outputs completed without API error.
- A/B randomized independently per case.
- Mapping hidden until all scores were durably written.
- Judge 1: Claude Sonnet safe mode, skills disabled, no tools.
- Judge 2: GPT-5.6 Sol in this orchestration session, scored blind packets before mapping decode.
- Codex judge was unavailable because its usage limit was exhausted; no failed Codex score was used.
## Decoded results

All four R2 packets happened to randomize FieldPilot as Candidate A.

| Case | Claude judge | Judge 2 | Result |
|---|---:|---:|---|
| 1 beauty no-show | FieldPilot 89 vs baseline 80 | FieldPilot 86 vs baseline 81 | FieldPilot wins 2/2 |
| 2 3D/game outsourcing SaaS | FieldPilot 93 vs baseline 72 | FieldPilot 92 vs baseline 83 | FieldPilot wins 2/2 |
| 3 family outage IoT | FieldPilot 86 vs baseline 83 | FieldPilot 91 vs baseline 82 | FieldPilot wins 2/2 |
| 4 narrow Notion/ClickUp | FieldPilot 79 vs baseline 75 | FieldPilot 92 vs baseline 93 | split; FieldPilot loses 1 judge |

Broad-case judge votes: **6/6 FieldPilot**.

Overall mean across the eight judge/case score comparisons:
- FieldPilot: 88.5
- Baseline: 81.125

The broad-case material-loss gate passed. The narrow no-loss gate failed.
## What improved

### Current competitor capability closure worked

Case 2 now caught Frame.io's current 3D review capability and documented official-source conflicts instead of leaving the feature unknown.

### Industry breadth improved

Cases 1–3 gained stronger local market structure, platform/infrastructure substitutes, current product changes, regulation/security context and counterevidence.

### Business next action improved

Case 3 moved from a one-household technical plug test to a price-bearing reservation/paid-intent test, better matching the sellability question.

### Claim discipline improved

The treatment more consistently kept market size, population, search absence and payment evidence on separate claim rungs.
## Remaining failure — requested-field closure

Case 4 successfully removed the R1 bloat: no total-cost model, no broad strategy, no unrelated market research.

However, FieldPilot left the Notion Plus guest limit as UNKNOWN.

Independent official-source verification after the blind score showed that current Notion help material can close this field: the paid Plus-class comparison permits an unlimited number of guests.

The failure is therefore not "be less cautious." The failure is:

> Do not stop at UNKNOWN for an explicitly requested narrow field while a current official source route remains accessible.

Repair should preserve the explicit scope lock while adding a requested-field completion gate.

## Bounded repair target

For explicit narrow/source-constrained requests:

1. create an internal checklist of every requested field;
2. mark each `PRESENT / BLOCKED / UNKNOWN`;
3. when UNKNOWN and an allowed official source route remains, continue within that field only;
4. use official help/release/billing docs to resolve ambiguity in a pricing page when available;
5. stop when requested fields are closed or honestly blocked;
6. do not compensate for a missing field with extra analysis or advice.

Only Case 4 needs behavioral rerun after this repair; broad R2 evidence remains frozen.
