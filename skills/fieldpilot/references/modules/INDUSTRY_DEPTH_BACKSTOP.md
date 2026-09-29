# Industry Depth Backstop — industry-depth-backstop-01

This module prevents FieldPilot's decision-first path from becoming narrower than a strong general deep-research answer when industry context can materially change the decision.

It does **not** turn every request into a giant market report. It adds an explicit escalation gate between ordinary decision research and the existing full/professional route.

## 1. Core principle

FieldPilot keeps its signature behavior:

`reference-first → alternatives/substitutes → evidence/claim ceiling → build/change/hold → one next action`.

But for a broad category, service, commercialization, or viability question, FieldPilot must also ask internally:

> Could a competent industry-level landscape change this decision, reveal a missed alternative class, or invalidate the apparent opportunity?

If yes, run the backstop before finalizing the decision.

The purpose is to absorb the strongest part of general deep research — market/industry breadth — without losing FieldPilot's decision compression.
## 2. Activation

Use this module when at least one is true:

- the user asks broadly about a market, product category, service class, commercialization, or whether an idea is worth entering;
- the category has materially different consumer / SMB / enterprise / infrastructure solution layers;
- market structure, concentration, installed incumbents, standards, regulation, security, or platform change can reverse the recommendation;
- a whitespace / niche / "no competitor" / "market opportunity" claim would be unsafe without a broader landscape;
- local and global markets may differ enough to change competitors, price ladders, channels, or feasibility;
- the ordinary alternative map finds a promising gap but macro context could explain why the gap exists;
- the user explicitly asks for market size, industry structure, share, growth, enterprise alternatives, or a comprehensive landscape.

Do **not** activate merely because a narrow fact question mentions a market or competitor.

Explicit full/professional market-research requests still use Route B. This module strengthens Route A and can trigger deeper bounded research; it does not replace the full deliverable contract.
## 3. Depth states

Record one internal state:

```text
INDUSTRY_DEPTH = NOT_NEEDED | COMPACT_BACKSTOP | DEEP_ESCALATION
```

### NOT_NEEDED

Use for narrow facts, one price, one feature, one source check, or a tactical question whose answer cannot be changed by industry breadth.

### COMPACT_BACKSTOP

Default for broad category / commercialization / viability work when industry context is relevant but a full report is not required.

Check the landscape slots in §4 and integrate only decision-relevant findings into the ordinary answer.

### DEEP_ESCALATION

Escalate when the compact sweep finds a contradiction, structural uncertainty, or industry-level factor capable of reversing the current decision.

Deep escalation is still bounded by the active decision. It is not permission to pad the response or search indefinitely.
## 4. Compact industry landscape slots

Assess each applicable slot as `PRESENT / NOT_APPLICABLE / NOT_DEFENSIBLE / UNKNOWN`.

1. **MARKET_BOUNDARY_AND_STRUCTURE**
   - What market(s) actually contain this job?
   - Is the feature a standalone market, a sub-feature inside a larger market, or split across several categories?
   - What major solution layers exist?

2. **MAGNITUDE_AND_GROWTH**
   - Is market magnitude/capacity material to this decision?
   - If yes, use supportable ranges, definitions, geography, period and conflicting estimates.
   - Do not create TAM/SAM/SOM theater when size does not change the decision.

3. **VENDOR_AND_PRICE_LADDER**
   - Map representative free, low-cost, mainstream SaaS/service, specialist hardware/service, and enterprise tiers when they exist.
   - Preserve price/terms dates and distinguish vendor claims from observed purchasing.

4. **ENTERPRISE_OR_INFRASTRUCTURE_ALTERNATIVES**
   - Check standards, bundled capabilities, operating-system/platform features, hardware management, internal IT tools, open-source/self-hosted options, and "already included" capabilities.
   - These often erase apparent startup whitespace.
5. **SECURITY_REGULATORY_TECH_SHIFT**
   - Check only material security failures, regulation/compliance, platform policy, standards, or technology shifts.
   - Ask whether the shift creates demand, destroys demand, changes trust, or moves the job into another layer.

6. **LOCAL_GLOBAL_CONTEXT**
   - When geography is known and material, compare local incumbents, distribution, certification/regulation, price/access and global alternatives.
   - Global evidence never silently substitutes for a materially different local market.

7. **INDUSTRY_COUNTEREVIDENCE**
   - Preserve mature substitutes, bundled/free solutions, declining economics, security liabilities, platform displacement, buyer inertia, and other facts that weaken the opportunity.

These slots are a coverage backstop, not mandatory report headings. User-facing output stays decision-first unless the user requested the full report.
## 5. Deep-escalation triggers

Move from `COMPACT_BACKSTOP` to `DEEP_ESCALATION` when one or more of these remains decision-material:

- market definitions or size estimates conflict enough to change the opportunity;
- the apparent category is actually spread across several parent markets;
- enterprise/infrastructure alternatives serve the same job with different economics;
- a local incumbent, certification requirement, procurement structure, or regulation changes entry feasibility;
- current technology/platform movement may shrink or relocate the problem;
- security/trust is a purchase or deployment gate rather than a side issue;
- vendor concentration, switching cost, installed base, or bundling changes the realistic addressable market;
- a whitespace claim survives direct/substitute closure but still lacks an industry explanation;
- the recommendation depends on whether an observed pattern is niche, structural, temporary, or already commoditized.

When escalated, load only the needed existing methods/modules, for example:

- `references/methods/sizing-and-segmentation.md`
- `references/methods/secondary-and-competitors.md`
- `references/modules/MARKET_PRIOR_AND_BASE_RATES.md`
- `references/modules/LOCAL_AND_EXPERT_RESEARCH.md`
- `references/modules/LIVE_TREND_AND_FRESHNESS_RADAR.md`
- `references/modules/REGULATORY_CONTEXT_CHECK.md`

Use official statistics, filings, primary vendor/platform documentation and high-quality industry sources proportionate to the claim.
## 6. Decision integration

Do not create a second generic market report beside the ordinary FieldPilot answer.

Feed the backstop into the existing decision surface:

```text
CURRENT_DECISION
DECISIVE_EVIDENCE
COUNTEREVIDENCE
UNKNOWNS
BUILD_CHANGE_OR_HOLD
ONE_NEXT_ACTION
```

Typical effects:

- a large parent market may show that the job exists, while the standalone feature remains a tiny add-on;
- a crowded vendor map may still leave a viable segment, but only if switching or distribution is favorable;
- a free/bundled infrastructure option may convert an apparent product opportunity into HOLD;
- a security/regulatory weakness in incumbents may create a differentiated opportunity, but only if buyers actually value and can purchase the safer alternative;
- a platform shift may make a current pain real but temporary.

Market breadth changes the recommendation only through evidence, not because "big market" or "growing market" sounds attractive.
## 7. Claim ceilings

Never convert:

- parent-market size → this product's market size;
- category CAGR → demand for this product;
- vendor count → market attractiveness;
- competitor absence → confirmed whitespace;
- review/interest → purchase or WTP;
- security incident → willingness to pay for security;
- enterprise feature availability → actual deployment/adoption;
- local seller count → market share;
- crowdfunding/funding → durable commercial success.

Keep market-size and market-share numbers definition-, geography-, period-, source- and method-specific. When sources conflict, show the range or disagreement instead of averaging it away.

## 8. Search / stopping rule

No fixed source count is required.

Continue while a lawful, task-fit route produces a new:
- solution layer;
- major vendor/incumbent;
- materially different price tier;
- infrastructure substitute;
- structural contradiction;
- local/global difference;
- security/regulatory/technology factor;
- decision-changing market-size definition.

Stop when the applicable slots are sufficiently supported or honestly blocked and new searches no longer change the decision.

Never claim global exhaustiveness.
## 9. Quality check against general deep research

Before finalizing a broad Route A answer, ask:

> Would a strong general deep-research report likely reveal an important market layer, enterprise alternative, size/structure fact, or technology/security shift that this answer never checked?

If yes, the backstop is incomplete.

Then ask the opposite:

> Did the extra industry research actually change, bound, or strengthen the user's decision?

If no, do not dump the extra material into the answer. Preserve it only when it earns its space.

## 10. Evidence boundary

This module was added after a same-topic comparison in which a general deep-research report produced stronger industry breadth (market size, vendor tiers, enterprise alternatives, security and industry structure), while FieldPilot produced stronger user-specific decision routing, substitute logic, HOLD discipline and next-action compression.

That comparison is a single-case development signal, not proof that either system is universally superior. See `references/development/GENERAL_RESEARCH_VS_FIELDPILOT_2026-09-29.md`.
