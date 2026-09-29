# Blind General Claude vs FieldPilot R1 — 2026-09-29

## Purpose

Evaluate whether industry-depth-backstop-01 actually combined the strongest observed general deep-research breadth with FieldPilot's decision-first strengths.

This was a development regression test, not proof of universal model superiority.

## Isolation design

- Same host: Claude Code 2.1.284
- Same model: Sonnet
- Same reasoning effort: high
- Fresh non-persistent sessions
- Baseline generated first with every active FieldPilot skill copy physically removed from `~/.claude/skills`
- A second synced FieldPilot copy was also quarantined; zero active `name: fieldpilot` SKILL.md remained
- Treatment used only the PR branch FieldPilot copy
- Outputs randomized independently as Candidate A/B per case
- Judge 1: GPT/Codex
- Judge 2: Claude Sonnet in safe mode, skills disabled, no tools
## Cases

1. Korea beauty-salon / nail-shop no-show deposit + reminder service
2. Korea 1–10 person 3D/game outsourcing review/version/approval SaaS
3. Korea family remote internet-outage / power-outage watchdog IoT device
4. Narrow control: Notion Plus vs ClickUp Unlimited — price, AI inclusion, guest limit only; explicitly no other market research

## Blind verdicts

| Case | GPT judge | Claude judge | Actual outcome |
|---|---|---|---|
| 1 | FieldPilot 71 vs baseline 68 | baseline 86 vs FieldPilot 80 | split |
| 2 | baseline 77 vs FieldPilot 66 | baseline 86 vs FieldPilot 79 | baseline wins both |
| 3 | baseline 73 vs FieldPilot 68 | baseline 85 vs FieldPilot 76 | baseline wins both |
| 4 | baseline 81 vs FieldPilot 67 | baseline 86 vs FieldPilot 68 | baseline wins both |

R1 therefore **failed promotion**. Do not merge the first backstop revision on this evidence.
## Failure mechanisms found

### 1. Industry breadth was advisory, not a completion gate

FieldPilot often mapped substitutes well but finalized before the industry layer was closed.

Repair:
- make COMPACT_BACKSTOP the minimum for broad market/commercial questions;
- require internal state for every applicable slot;
- block finalization while a decision-flipping accessible slot remains UNKNOWN.

### 2. Current competitor capability delta was not closed

Case 2 FieldPilot said Frame.io 3D support was unconfirmed. The baseline found the 2026 Frame.io 3D asset review launch, which directly changed the competitive threat.

Repair:
- add CURRENT_CAPABILITY_DELTA;
- for the strongest 3–5 alternatives defining a gap/threat, inspect current official release/product/pricing material;
- old comparison pages cannot close a time-sensitive feature claim.
### 3. Narrow-scope obedience regressed

Case 4 explicitly asked for only price, AI inclusion and guest limits. FieldPilot added total-cost calculations, upgrade advice and extra analysis.

Repair:
- explicit scope lock becomes kernel-level;
- no adjacent market analysis, total-cost modeling, strategy, end questions or fuller-report offer under an explicit narrow restriction.

### 4. Next action sometimes tested technology, not the business decision

Case 3's one-household smart-plug test was technically useful but weak for the active "will people pay 50,000 KRW?" decision.

Repair:
- ONE_NEXT_ACTION must target the highest residual business uncertainty;
- a technical prototype alone is insufficient for a sellability decision unless feasibility is the blocker;
- paid proof requires real payment and a defined exposure denominator.

### 5. Low COGS was overinterpreted

Case 1 used cheap message delivery as evidence that charging would be hard.

Repair:
- low marginal delivery/input cost never implies low WTP;
- WTP needs value, alternatives, switching or observed payment evidence.

## Revision

These failures drive industry-depth-backstop-02. R2 must be rerun against the same frozen baseline prompts before merge.
