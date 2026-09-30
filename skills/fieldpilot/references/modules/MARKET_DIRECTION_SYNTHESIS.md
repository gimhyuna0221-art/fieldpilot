# MARKET_DIRECTION_SYNTHESIS — evidence-grounded direction selection

## Purpose

FieldPilot should not stop at "what the market looks like." When the active business decision is broad enough
to require a direction choice, convert the researched market evidence into a **recommended current direction**,
a supported alternative when one exists, explicit avoid/defer boundaries, reversal conditions, and the smallest
real-world discriminator.

This is a synthesis layer, not a new research engine. It reuses the evidence and decision machinery FieldPilot
already has and must never create confidence by adding unsupported options, scores, or forecasts.

## 1. Activation

Activate only when direction is decision-material, including broad viability, commercialization, market entry,
positioning, customer/segment focus, build/change/hold, or a material pivot/reposition decision.

Run it **after** the relevant evidence collection, competitor/substitute map, product-state check, and material
coverage audit, and **before** the final `CURRENT_DECISION` / executive recommendation is finalized.

Do not activate for:
- an explicit narrow fact/source-only request;
- a user scope lock that excludes strategy/direction advice;
- descriptive research where no direction choice is being made;
- cases where adding a direction layer would merely restate one obvious requested action.

## 2. Reuse existing controls; do not duplicate them

Direction synthesis consumes, when available:

- `CLIENT_DECISION_BRIEF` — the decision, owner/user, choice set, stakes, and evidence that would change it;
- `EVIDENCE_PLAN + COVERAGE_AUDIT` — what is ANSWERED / PARTIAL / UNKNOWN;
- `EVIDENCE_TRACE`, provenance, freshness, counterevidence, and claim ceilings;
- `COMPETITIVE_ALTERNATIVES`, including direct, substitute, manual, service, general-AI, spreadsheet, and
  do-nothing options where material;
- `PRODUCT_STATE` and the user-case gap;
- `DECISION_SURFACES` `CHANGE_OPTIONS` and `COMPARE_VARIANTS` when they are already applicable;
- `DECISION_SUPPORT` commitment boundaries and cheapest-next-informative-action logic;
- commercial-evidence rung separation for pricing/payment/WTP decisions.

Do not rebuild these as parallel schemas or databases.

## 3. Feasible direction object

Create a direction only when there is enough evidence to make it meaningfully distinct from the current path.

```text
DIRECTION_ID
DIRECTION_TYPE              optional: KEEP / NARROW / REPOSITION / PIVOT / HOLD or another case-fit label
WHO                         customer / buyer / segment when material
JOB_OR_PROBLEM
OFFER_OR_PRODUCT_CHANGE
CHANNEL_OR_MOTION           only when material
WHAT_STAYS
WHAT_CHANGES
EVIDENCE_FOR
EVIDENCE_AGAINST
COVERAGE_AND_UNKNOWNS
SWITCHING_OR_EXECUTION_BURDEN
NEXT_COMMITMENT_BOUNDARY
REVERSAL_EVIDENCE
SMALLEST_DISCRIMINATOR
```

Rules:
- The current direction is the baseline. Do not compare alternatives only against a strawman.
- Generate **only evidence-supported feasible directions**. There is no required option count.
- Do not invent three directions to make the answer look strategic.
- A change in customer, job, offer, channel, or business model is not automatically a pivot; describe the
  actual material change.
- A direction may be unattractive because of weak evidence, switching burden, implementation burden, access,
  regulation, economics, or a stronger substitute. Name which one; do not hide it inside a generic score.

## 4. Direction synthesis states

The user-facing synthesis may contain:

```text
MARKET_REALITY
FEASIBLE_DIRECTIONS
PRIMARY_DIRECTION
WHY_PRIMARY_NOW
ALTERNATIVE_DIRECTION       only when a materially viable alternative exists
AVOID_OR_DEFER               only when evidence supports an explicit boundary
REVERSAL_CONDITIONS
NEXT_DISCRIMINATING_ACTION
CLAIM_CEILING
```

### PRIMARY_DIRECTION

The strongest defensible path **under current evidence and constraints**. It is a recommendation, not a claim
that the path is objectively correct or guaranteed to succeed.

Selection rule:
- explain why it dominates the plausible alternatives **now**;
- preserve decisive counterevidence;
- prefer a reversible or lower-commitment path when evidence is insufficient to justify a larger irreversible
  commitment;
- never promote a direction because it sounds novel, has a large TAM, has many competitors, or received a high
  synthetic score.

### ALTERNATIVE_DIRECTION

Include only if it is genuinely plausible and materially different. State the condition under which it would
become preferable to the primary direction.

### AVOID_OR_DEFER

Not mandatory. Use when evidence supports a concrete boundary such as "do not scale paid acquisition yet" or
"do not build the broad workflow before the narrower buyer/job is resolved." This is not a permanent rejection
unless the evidence supports one.

### DIRECTION_UNRESOLVED

If the available evidence cannot separate the feasible directions, say so. Do not force a winner. Name:
- the two or more directions that remain live;
- exactly what unresolved evidence separates them;
- the smallest lawful, feasible discriminator.

## 5. Reversal conditions are mandatory

For every PRIMARY_DIRECTION, state the strongest evidence that would cause FieldPilot to:
- switch to the alternative;
- narrow the recommendation;
- HOLD;
- or reopen the direction search.

Reuse the existing falsifier/reversal discipline. A recommendation without a reversal condition is incomplete
for a material direction decision.

## 6. Market direction is not the same as the next action

Keep these separate:

```text
MARKET_DIRECTION            where the evidence says to aim
NEXT_DISCRIMINATING_ACTION  the smallest action that tests whether that direction should keep its rank
```

The next action should resolve the highest residual uncertainty that can change the direction. Do not substitute
an easy technical task for a commercial/customer uncertainty when the latter is what separates the paths.

When the action is consequential, attach the existing `IMPACT_VERIFICATION` chain:
`ACTION -> MECHANISM -> OBSERVABLE METRIC/STATE -> MEASUREMENT CONTEXT -> DECISION CHECK -> CAUSAL CAVEAT`.

## 7. Ordinary Route A delivery

Do not print a giant new framework. Integrate the synthesis into the existing answer:

- `CURRENT_DECISION` becomes the recommended current direction when direction is material;
- `BUILD_CHANGE_OR_HOLD` carries what stays / changes / is deferred;
- show the strongest supported alternative only when useful;
- show the reversal condition in plain language;
- `ONE_NEXT_ACTION` becomes the smallest discriminator when a discriminator is needed.

A novice should be able to answer: "어디로 가는 게 낫고, 왜 그런지, 언제 생각을 바꿔야 하는지,
그리고 지금 뭘 확인하면 되는지."

## 8. Full / professional Route B delivery

In a full report, include a compact `Market Direction Synthesis` after the user-case gap assessment and before
the prioritized recommendation plan when direction is material. The Executive Decision Layer should summarize
the same primary direction, strongest counterevidence, reversal condition, and next verification rather than
creating a second competing recommendation.

The professional delivery envelope, coverage audit, AI/human disclosure, and Findings -> Interpretation ->
Recommendations separation remain unchanged.

## 9. Returning evidence

New REAL evidence updates only the affected direction rows and dependencies.

Return:
`WHAT_CHANGED / WHAT_STAYED_STABLE / UPDATED_DIRECTION / REVERSAL_STATUS / NEXT_DISCRIMINATOR`.

Do not rerun unrelated research or silently erase a previously supported direction. If a reversal condition
fires, say which evidence triggered it.

## 10. Hard guards

- No success probability, viability score, market score, or confidence percentage invented by the model.
- No "best direction" from source count, popularity, TAM/CAGR, or competitor count alone.
- No direction can outrun its weakest decision-material coverage state or commercial claim ceiling.
- Market evidence informs the recommendation; it does not guarantee the customer's outcome.
- Do not convert `UNKNOWN` into a confident direction just to be decisive.
- Do not turn multiple options into multiple simultaneous user homework assignments.
- Preserve AI-first/no-homework: FieldPilot performs accessible research and preparation before escalating to
  irreducible real-world evidence.
