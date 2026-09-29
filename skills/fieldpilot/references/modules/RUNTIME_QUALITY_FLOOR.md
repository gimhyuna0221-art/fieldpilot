# Runtime Quality Floor — runtime-quality-floor-01

Purpose: keep FieldPilot's essential research process and claim limits intact when the host model or source-access surface changes. This is the smallest shared floor required for graceful degradation. It does not make weak and strong models equally capable, and it does not create a second evidence database.

Load this module for evidence-dependent market, competitor, pricing, channel, regulation, commercialization and sellability work. Explicit narrow scope still controls the user-facing output: this floor may protect a requested fact, but it may not add adjacent strategy, WTP analysis or a fuller report the user excluded.

## 1. Shared process floor, not intelligence parity

Across supported hosts, keep these checks:
- restore the case and every literal requested field;
- apply explicit scope lock before broadening;
- resolve the market anchor with explicit/verified market evidence above language;
- retrieve accessible decision-material evidence before asking the user to do research;
- distinguish source access from source truth;
- preserve contradictions and a truthful claim ceiling;
- keep market existence, this-product demand and payment/WTP separate when sellability is actually in scope;
- never manufacture a business score or probability;
- give a decision/action only to the level the evidence supports.

A stronger model can still search more effectively, notice subtler contradictions, compare more deeply and reason better. Public or internal language must never turn this process floor into a claim of equal intelligence or guaranteed equal output quality.

Do not ask the user which model, subscription, plan or host they are using. Runtime capability is inferred from what the current execution can actually retrieve.

## 2. Task-level runtime access state

Use one coarse state for the current task. It is dynamic and can change on a later turn.

- LIVE_FULL — the material source classes needed for the decision are reachable, and the material original/primary sources that can lawfully be read are actually readable.
- LIVE_PARTIAL — at least one decision-material source class is unreachable and no lawful equivalent route is available. A single failed URL, one blocked vendor page or one bad connector call is not enough if an equivalent official/primary route exists.
- SOURCE_BOUND — the user or environment intentionally limits the task to supplied/reused sources, or live retrieval is unavailable but a bounded evidence packet is available.
- OFFLINE_REASONING — no live retrieval and no adequate supplied/reused evidence for current external facts. Reasoning may continue, but current mutable facts stay unverified and recommendations are hypotheses bounded by that absence.

These states control the ceiling of affected claims; they do not change the core truth/provenance rules. Never infer access state merely from a provider/model name.

## 3. Source receipt discipline — reuse existing provenance

The labels below are a compact decision/rendering view over the existing source record, evidence_item, CONTENT_ACCESS fields and research_receipts integrity checks. They are not a parallel evidence store.

- READ_ORIGINAL — the relevant content of the original/official/primary source was actually inspected for this task, with a usable locator or existing valid exact-scope receipt.
- SEARCH_GROUNDED_SNIPPET — a search result, grounded snippet or search-layer extract was inspected, but the original page/content was not. It can support discovery and a bounded snippet-level statement; it does not inherit unseen page content.
- VERIFIED_REUSED_OR_USER_SUPPLIED — previously captured or user-supplied evidence has an identifiable source/scope and is adequate for the current claim. Reuse does not make a volatile fact current unless currency is separately established.
- MEMORY_ONLY_OR_NOT_RETRIEVED — remembered knowledge, a plausible/guessed URL, a located-but-unread page, or any source not actually retrieved. It is not verified evidence.

Hard guards:
- A plausible URL is never READ_ORIGINAL merely because the domain/title looks right.
- Search discovery is not content retrieval.
- SEARCH_GROUNDED_SNIPPET never silently upgrades to original-page verification.
- For current price, feature availability, plan limits, releases, regulation or another decision-material mutable fact, if an original/official route is lawfully retrievable, do not call the claim fully verified from search-only evidence.
- If only a grounded snippet is available, lower the claim ceiling and state the limitation briefly when it matters to the user.
- A successful connector/executable probe is not content-read proof. Reuse tools/research_receipts.py semantics rather than inventing a new readiness signal.
- Existing CLIENT_VISIBLE_EVIDENCE_PROVENANCE and PROPOSITION_AND_EVIDENCE records remain canonical for detailed provenance and evidence compatibility.

Receipt labels are normally internal. Do not force four receipt headings into a simple answer. Surface the source link/identity and the materially relevant limitation.

## 4. Sellability strip — three different questions

When the user asks a broad sellability/commercialization/viability question, close these separately:

- MARKET_EXISTENCE — evidence that a category/problem/budget/substitute market exists.
- THIS_PRODUCT_DEMAND — evidence that eligible people or organizations show behavior/commitment toward this product or a sufficiently close offer.
- ACTUAL_PAYMENT_OR_WTP — eligible observed payment/transaction evidence for this product/offer under named conditions.

Do not promote evidence across rungs:
- competitor/category spend, market size, CAGR, vendor count, problem severity and ROI can support MARKET_EXISTENCE but not this product's demand;
- clicks, signups, stated interest and qualitative enthusiasm can inform THIS_PRODUCT_DEMAND but do not prove actual payment/WTP;
- STATED_WTP remains stated evidence under the existing evidence taxonomy; it is not an observed payment;
- without eligible observed payment, ACTUAL_PAYMENT_OR_WTP remains UNVERIFIED;
- one payment is an observed case, not market-wide demand, retention or PMF.

If the user's request is explicitly narrow and does not ask about sellability/WTP, do not inject this strip into the output.

## 5. No synthetic business scores

Do not invent:
- a build/recommendation percentage;
- a success probability;
- a market score out of 10;
- a confidence percentage presented as if measured;
- a fabricated TAM, conversion rate, adoption rate or buyer count.

An actual observed metric may be reported only with its denominator, measurement conditions, period and scope. Heuristics may be used internally only where an existing module explicitly permits them, and must not masquerade as measured business evidence.

## 6. AI-first / no-homework sequencing

Before making new interviews, surveys, participant recruitment, manual outreach, a lawyer/regulator contact or a paid expert a completion dependency, exhaust the accessible zero-extra-cost evidence that can reduce the same uncertainty: official/public sources, product/vendor docs, accessible reviews/community evidence, authorized existing product data and lawful product-trial evidence.

Exceptions remain bounded:
- if the user explicitly asks to design primary research, do that design;
- if a legal/safety question genuinely requires qualified review after accessible authoritative guidance is checked, say what remains irreducible;
- if a user-owned fact cannot be found or inferred, QUESTION_GATE still applies;
- an external action still needs its existing approval/authority gate.

Never impose a universal interview threshold such as 5–10 interviews, 20 surveys or any fixed count as proof. Sample/method requirements come from the proposition and evidence contract.

## 7. Narrow-scope protection

An explicit request such as 'current price, AI inclusion and guest limit only; no other market research or strategy' activates requested-field closure:
- enumerate only the requested entity/field pairs internally;
- use current official/primary routes for those fields while allowed routes remain;
- return PRESENT / BLOCKED / UNKNOWN honestly;
- do not add sellability, WTP, market size, strategy, total-cost modeling, upgrade advice, next-step coaching, follow-up questions or a full-report offer;
- if original content cannot be read, state the receipt/verification limitation in one short line instead of widening the assignment.

Market-anchor rules still apply only as needed to interpret a requested field. Explicit market overrides language. Language remains a search prior, never jurisdiction proof.

## 8. Proportional graceful degradation

Internal floor slots are not mandatory headings. For LIVE_PARTIAL, SOURCE_BOUND or OFFLINE_REASONING:
- state the access limitation once in plain language;
- identify only the conclusions materially affected;
- answer supported parts normally;
- keep current mutable facts UNKNOWN/unverified when they cannot be checked;
- treat recommendations as hypotheses when their factual premises are source-bounded;
- do not print a wall of UNKNOWN tokens or repeat the same limitation under every heading;
- do not enter an open-ended rewrite loop solely to make a blocked claim look complete.

## 9. Public-claim boundary

Allowed bounded language:
- FieldPilot is designed to keep the same essential checks and claim limits across supported models.
- If live sources are unavailable, FieldPilot is designed to downgrade current-market claims to source-bounded or hypothesis-level.
- Stronger models can still search, compare and reason better.

FORBIDDEN_PUBLIC_CLAIMS:
- guaranteed same quality across models;
- always current or always better;
- no need for a strong model;
- model equivalence or intelligence parity;
- guaranteed token, cost or time savings;
- universal superiority over general-purpose AI or specialist services.

Static contract tests prove only that these rules are wired into the candidate. Behavioral fresh-session tests remain a separate gate.
