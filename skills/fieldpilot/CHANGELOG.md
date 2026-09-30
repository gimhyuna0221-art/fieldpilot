# FieldPilot Changelog

## decision-direction-01 — Market Evidence to Recommended Direction

This bounded extension turns researched market evidence into a direction recommendation without adding a new research engine.

- Added `references/modules/MARKET_DIRECTION_SYNTHESIS.md`.
- Added `direction_extension_revision: "decision-direction-01"` to the kernel.
- Reuses the existing client decision brief, evidence plan/coverage audit, evidence trace, competitor/substitute map, product state, `CHANGE_OPTIONS`, `COMPARE_VARIANTS`, commitment boundary and commercial claim ceilings.
- Adds `PRIMARY_DIRECTION`, a material alternative when one exists, supported `AVOID_OR_DEFER` boundaries, mandatory reversal conditions, and the smallest discriminating next action.
- Adds `DIRECTION_UNRESOLVED` when evidence cannot separate live directions; no forced winner, option quota, success probability or synthetic market score.
- Keeps market direction distinct from next action. The next action tests whether the direction should keep its rank.
- Adds a professional-report `Market Direction Synthesis` slot when direction is decision-material.
- Restored explicit regression tests for the August professional-grade P0/P1 controls so decision-direction work cannot silently delete the client brief, evidence/coverage plan, professional delivery envelope, executive decision/impact verification, negative-evidence/falsifier protection, or direct-research QC.
- Added the direction and professional-uplift regression contracts to targeted CI.

This is a decision-synthesis improvement. It does not establish that FieldPilot chooses the objectively correct strategy, guarantees outcomes, or replaces real payment/customer evidence.

## runtime-quality-floor-01 — Shared Process Floor, Honest Degradation

This bounded continuation adds a host-neutral runtime quality floor without claiming model equivalence.

- Added `references/modules/RUNTIME_QUALITY_FLOOR.md` and `runtime_quality_extension_revision: "runtime-quality-floor-01"`.
- Added task-level access states `LIVE_FULL / LIVE_PARTIAL / SOURCE_BOUND / OFFLINE_REASONING`; they are inferred from actual retrieval capability, never the model/provider name.
- Added source-receipt classes `READ_ORIGINAL / SEARCH_GROUNDED_SNIPPET / VERIFIED_REUSED_OR_USER_SUPPLIED / MEMORY_ONLY_OR_NOT_RETRIEVED` as a rendering/decision layer over the existing provenance and evidence records, not a parallel evidence database.
- Search discovery, a plausible URL or a grounded snippet never becomes original-page verification. Current price, feature, plan-limit, release and regulation claims keep a lower ceiling when the original is retrievable but not read.
- Added a sellability separation: `MARKET_EXISTENCE / THIS_PRODUCT_DEMAND / ACTUAL_PAYMENT_OR_WTP`. Market size, CAGR, competitor/category spend, problem severity, ROI and stated interest do not prove this product's actual WTP.
- Added a no-synthetic-business-score guard for invented build percentages, success probabilities and market scores.
- Strengthened AI-first/no-homework sequencing: exhaust accessible public/official/review/community/product evidence that can reduce the same uncertainty before making new interviews, surveys, recruitment or manual outreach a completion dependency. No universal interview-count threshold is added.
- Explicit narrow factual requests suppress adjacent WTP/strategy/report-offer output and preserve requested-field closure.
- Source-bound/offline runs degrade compactly instead of fabricating current facts or printing a wall of internal UNKNOWN states.
- Public copy is limited to a shared process/claim-discipline floor. It does not claim equal intelligence, guaranteed same quality, always-current results, lower token/cost/time usage, or that strong models are unnecessary.
- Aligned `PROPOSITION_AND_EVIDENCE.md` with `market-anchor-01`: conversation language can be a provisional search prior, never confirmed geography/jurisdiction.

This is a runtime-contract change. Static contract coverage and behavioral validation are separate gates; neither alone proves universal quality.

## market-anchor-01 — Local-First, Global-Best, Local-Transfer

User friction found: requiring the user to repeatedly state "한국 시장" is unnecessary, while allowing search engines/models to default toward abundant English/US material creates a different bias.

- Added `references/modules/MARKET_ANCHOR_AND_EXPANSION.md`.
- Added `market_anchor_extension_revision: "market-anchor-01"` to the kernel.
- Added market-anchor precedence: explicit market → verified case market → strong local signal → provisional language market → language cluster → global unresolved.
- Language is now a **search prior, not geography proof**.
- Korean can trigger a provisional South Korea first-pass search when no stronger contradictory signal exists.
- English never defaults to the United States; English, Spanish, Portuguese, French and Arabic use language-market clusters unless stronger market evidence exists.
- Added `LOCAL-FIRST → GLOBAL-BEST → LOCAL-TRANSFER`: inspect likely local alternatives first, then global best references, then test price/platform/regulatory/workflow transferability.
- Added a provisional Korea mode distinct from full confirmed Korea closure.
- Device/account/physical/IP/remembered-owner location are forbidden market anchors.
- Geography questions move later: research first, ask only if the remaining ambiguity can still materially reverse the recommendation.
- Added contract tests for market-anchor precedence, language priors, US-default prevention, local-transfer gates and Korea provisional/full modes.

This change reduces user input burden and US/English-source defaulting without claiming that conversation language identifies the user's actual target market.

## industry-depth-backstop-02 — Blind-Test Repair of Industry Breadth

Added after a same-topic comparison showed a useful asymmetry: the general deep-research output covered industry structure, market-size ranges, vendor tiers, enterprise alternatives and security/technology context more deeply, while FieldPilot produced stronger substitute logic, user-specific HOLD discipline and next-action compression.

- Added `references/modules/INDUSTRY_DEPTH_BACKSTOP.md`.
- Added `industry_depth_extension_revision: "industry-depth-backstop-02"` to the kernel.
- Added three depth states: `NOT_NEEDED / COMPACT_BACKSTOP / DEEP_ESCALATION`.
- R1 clean-session blind testing failed promotion: baseline won both judges in cases 2–4 and split case 1. The failure record is `references/development/BLIND_GENERAL_VS_FIELDPILOT_R1_2026-09-29.md`.
- Broad category/commercialization/viability work now uses `COMPACT_BACKSTOP` as a minimum internal floor and checks:
  - market boundary and industry structure;
  - supportable market magnitude/growth when decision-relevant;
  - vendor and price ladder;
  - enterprise/infrastructure/open-source/bundled alternatives;
  - material security, regulatory and technology shifts;
  - local/global differences and industry counterevidence;
  - `CURRENT_CAPABILITY_DELTA` for the strongest alternatives defining the claimed gap/threat.
- Added `BACKSTOP_COMPLETION_GATE`: accessible decision-flipping UNKNOWN slots block finalization until searched or honestly closed.
- Added kernel `EXPLICIT_SCOPE_LOCK`: explicit narrow requests forbid adjacent analysis, total-cost modeling, strategy, end questions and fuller-report offers.
- Added `Cost is not value`: low marginal input/delivery cost cannot be used as low-WTP evidence.
- Strengthened `FIRST_PAID_PROOF`: next action targets the highest residual business uncertainty; technical prototype tests do not substitute for payment evidence when sellability is the active decision.
- The compact pass escalates only when a structural contradiction can change the recommendation; narrow fact questions remain narrow.
- Existing sizing, competitor, market-prior, local/expert, trend and regulatory modules are reused rather than duplicated.
- Market size/CAGR/vendor count remain bounded evidence and never become product demand or WTP proof.
- Added `references/development/GENERAL_RESEARCH_VS_FIELDPILOT_2026-09-29.md` with a strict single-case claim ceiling.
- Added a static contract test for wiring, activation, escalation and claim ceilings.

R2 clean-session blind testing materially improved broad-market performance: FieldPilot won all 6/6 broad-case judge votes and had a higher overall mean score than the frozen baseline. The first R2 pass still failed because the narrow-control case split 1–1: one judge penalized FieldPilot for leaving the Notion Plus guest limit UNKNOWN even though an official Notion help route could close it. After the bounded R2.1 requested-field-closure repair, the affected narrow case was rerun only; FieldPilot won both blind judgments (82–77 and 97–91), so the frozen promotion gate passed.

Bounded R2.1 repair:
- explicit scope lock is now paired with `REQUESTED_FIELD_CLOSURE`;
- every literal requested field/entity pair must be `PRESENT / BLOCKED / UNKNOWN`;
- an UNKNOWN requested field cannot ship while a lawful allowed current official/primary route remains;
- ambiguous pricing/product pages may be resolved through current official help/billing/plan-change/role-limit/release docs for that same field;
- the repair may not widen the user's requested scope.

The exact R2 result and failure mechanism are recorded in `references/development/BLIND_GENERAL_VS_FIELDPILOT_R2_2026-09-29.md`.

This change is a product-design improvement, not evidence that FieldPilot universally outperforms general deep research.

## quality-max-01 — Quality Before Usage

Based on convergent external pilot feedback, FieldPilot no longer treats usage/output reduction as a primary success target.

- Added `references/modules/QUALITY_MAXIMUM_PERFORMANCE.md`.
- Added `quality_extension_revision: "quality-max-01"` to the kernel metadata.
- Quality priority is now: truth/provenance → decision-critical coverage → high-recall competitor/substitute/reference discovery → comparison specificity → decision usefulness → efficiency.
- Efficiency removes duplicate searches, repeated entities, unchanged rereads and empty prose, but may not remove material competitors, overlap dimensions, contradictions, representative references or decision-changing detail.
- Added overlap decomposition across job, workflow, mechanic/behavior, genre/category, aesthetic/tone, progression/retention, price/model, channel/platform and other task-fit dimensions.
- Added representative-reference mapping for direct competitors, substitutes, adjacent references, component analogues and cross-category references.
- Expanded discovery facets beyond direct category/substitute/adjacent to component/mechanic analogues, cross-category references and marketplace/community vocabulary.
- Changed ordinary output from "compression" to a decision-first architecture that preserves useful competitor/reference comparisons and non-obvious discoveries.
- Added a customer-visible differentiation check: when broad findings look like a generic general-AI first pass, improve the investigation rather than add decorative framework prose.
- Recorded the external pilot signal in `references/development/HUMAN_PILOT_QUALITY_VS_USAGE_2026-09-29.md` with a strict claim ceiling.

This change does not establish commercial superiority, WTP, market-wide preference, or exact token savings. External clean-session comparison remains required.

## v1.9.9-rc04 — Prompt-Skill Independence (candidate)

Product requirement: a buyer who does not know research vocabulary or prompt writing must not get a shallower investigation, weaker evidence, a worse judgment, more questions or more homework than a buyer who does. "개떡같이 말해도 찰떡같이 알아듣습니다" is now a runtime contract.

- Added `references/modules/PROMPT_SKILL_INDEPENDENCE.md`, loaded first in every route:
  - `CASE_FRAME` request restoration: typos, spacing, slang, banmal, fragments, mixed languages, vague referents, several questions in one message, worried questions, and solution questions whose premise must be checked (the XY problem).
  - `COVERAGE_FLOOR` set by the case state, not by vocabulary, with a universal decision floor and case rows (alternatives, product state, money, post-launch causes, payment, channel, local, delta, narrow, full).
  - `QUESTION_GATE` — one deterministic rule for asking: FINDABLE → look it up; INFERABLE → labeled assumption; USER_OWNED → `ASK_AFTER` a complete answer by default, `ASK_FIRST` only when no useful bounded answer is possible; ≤2 questions; never ask for modes, formats, permission to research, findable facts or research-brief definitions.
  - `FRIENDLY_EXPERT` delivery as the default register: direct answer first, one-line restored case, plain headings, no internal tokens as main text, protective distinctions kept in plain words.
  - `EXPERT_TWIN` equivalence check before sending.
- Kernel (`SKILL.md`): new STEP 0 and invariants 16–18; invariant 15 geography timing fixed (bounded answer first, geography question at the end — no guessing, no blocking); plain-language delivery is the default rather than opt-in; Route B selection follows an explicit research/report request in any wording, research vocabulary alone does not select it, and broad Route A answers offer the full report in one line.
- Aligned the scattered question rules to the gate: lifecycle stage, geography (kernel, Korea-local, regulatory, competitor method), product-fact gaps, monetization facts, Route B intake (the user is no longer asked to formulate the decision/owner/deadline), provisional scope, market prior, analysis/reporting, runtime-core novice rules, channel prerequisites, and direct-research method choice (post-answer option only).
- Lifecycle router routes by the restored case; "should I advertise?" gets a premise check before channel advice.
- Description adds everyday trigger phrases so casual asks activate the skill without `/fieldpilot`.
- Worked example card rewritten plain-first with identifiers in parentheses.
- Added static contract + policy lint tests and a behavioral prompt-robustness eval suite (same intent / different language, missing context, user burden, friendly delivery, hard cases) with graders and a runner.

Unchanged: truth before fluency, UNKNOWN, provenance, counterevidence, competitor recall and gap safeguards, commercial/WTP ceilings, product-state and coverage honesty, geography no-guessing, Korea-local coverage, demand-vs-distribution diagnosis, signal integrity, first-paid-proof discipline, returning-evidence continuity, the full professional route, approval gates for external execution, and the role boundary. No score, guarantee or new mandatory research is added.

## v1.9.9-rc03 — Lifecycle Decision Routing

- Added one lifecycle router for plain-language `/fieldpilot` use across:
  - idea validation;
  - MVP / build decisions;
  - pre-launch / pre-sell;
  - launched with no response;
  - launched with interest but no payment;
  - monetizing products;
  - returning evidence / decision updates.
- Wired existing demand-vs-distribution diagnostics, signal-integrity checks, channel routing, pricing/payment logic, competitor/substitute research, product-state comparison and decision surfaces into the lifecycle route.
- Added post-launch guards so "no response" is not collapsed into a single product or advertising cause.
- Added product-specific promotion/channel output with one first route, one fallback, an exact test and measurement logic.
- Added explicit guardrails for red-ocean, niche, customer and jackpot/no-hope claims.
- Added runtime contract tests for lifecycle routing and updated Korea-local tests to expect rc03.
- Updated public README descriptions and usage examples.

This release does not add a success-probability score, guaranteed advertising channel, PMF/WTP certification, direct code editing, autonomous spend, or proof of a niche from search absence.
