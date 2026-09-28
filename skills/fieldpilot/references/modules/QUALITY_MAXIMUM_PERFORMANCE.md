# Quality-Maximum Performance Profile — quality-max-01

This profile changes FieldPilot's default optimization target based on convergent external pilot feedback.

Two external testers independently praised FieldPilot's strongest behavior as:
- finding non-obvious overlapping categories/genres/products they had not known;
- mapping representative products to each overlapping element and comparing them;
- searching unusually thoroughly for products with a similar feel or job.

The same feedback also said that after usage was reduced, the result felt less rich/detailed and not
different enough from asking ordinary ChatGPT.

This is qualitative pilot feedback, not a controlled benchmark, WTP proof, or market-wide preference.

## 1. Optimization order

Unless the user explicitly imposes a hard usage, time, or length constraint, optimize in this order:

1. factuality / provenance / claim ceiling;
2. decision-critical coverage;
3. high-recall competitor / substitute / reference discovery;
4. specificity and comparison depth;
5. decision usefulness and professional deliverable quality;
6. efficiency.

Efficiency means removing duplicated searches, repeated entities, unchanged rereads, dead branches,
and prose that adds no information.

**Efficiency must never be purchased by dropping a material competitor class, a useful overlap
dimension, a contradiction, a representative reference, or decision-changing detail.**

Do not use token count, output length, elapsed time, or source count as a primary success metric unless
the user explicitly asks for that optimization. Never claim usage savings unless actually measured.

## 2. High-recall overlap decomposition

For broad competitor/reference discovery, do not search only for products that share the same category
label. Decompose the subject into material dimensions that create its actual experience or buying
substitution.

Possible dimensions include, only when applicable:

```text
CORE_JOB_OR_OUTCOME
USER_OR_BUYER
USE_CONTEXT
WORKFLOW_OR_INTERACTION
MECHANIC_OR_BEHAVIOR
GENRE_OR_CATEGORY
AESTHETIC_OR_TONE
PROGRESSION_OR_RETENTION_LOOP
BUSINESS_MODEL_OR_PRICE
CHANNEL_OR_PLATFORM
TECHNICAL_FORM
TRUST_OR_RISK_MODEL
```

For games/media/creative products, mechanics, genre blend, progression loop, social structure,
camera/control pattern, aesthetic/tone, session structure and monetization may be separate dimensions.

For SaaS/services, job-to-be-done, workflow, user/payer, integration, pricing, distribution,
replacement behavior and trust may matter more.

Do not force irrelevant dimensions.

## 3. Representative reference map

For each material overlap dimension, search for the strongest **representative real products/cases**
that illuminate that dimension, even when the overall product belongs to another category.

Use:

```text
OVERLAP_DIMENSION
REPRESENTATIVE_REFERENCE
REFERENCE_CLASS
WHY_IT_MATCHES
IMPORTANT_DIFFERENCE
SOURCE_EVIDENCE
WHAT_TO_LEARN_OR_AVOID
```

Valid reference classes:
- DIRECT_COMPETITOR
- SUBSTITUTE
- ADJACENT_REFERENCE
- COMPONENT_ANALOGUE
- CROSS_CATEGORY_REFERENCE

The purpose is to reveal the market's actual solution vocabulary and transferable patterns, not to
inflate a competitor count.

A reference is not automatically evidence that buyers see the two products as substitutes.

## 4. Search breadth

For material broad research, challenge the initial framing through distinct search families:

- literal/direct category;
- alternate category and user vocabulary;
- same job, different solution;
- adjacent behavior/workflow;
- component/mechanic analogue;
- cross-category experience analogue;
- marketplace/store taxonomy;
- reviews/community language;
- "alternative to" / comparison / migration language;
- negative closure for purported whitespace.

Continue while a lawful search route is still producing decision-relevant new entities, overlap
dimensions, contradictions, or evidence.

Stop when remaining routes are redundant, blocked, not applicable, or no longer change the decision.

Never claim global exhaustiveness. State residual recall limits when they matter.

## 5. Detail preservation

For broad market/competitor/product-fit work, do not compress the useful result into a generic summary
merely to save usage.

Preserve, when material:
- non-obvious category/genre overlaps discovered;
- representative products for each important overlap;
- concrete similarities and important differences;
- why each reference changes a product/positioning decision;
- meaningful competitor/substitute breadth;
- contradictory evidence and uncertainty;
- direct source locators.

A long answer/report is acceptable when the information density earns the length.

Page count and word count are not quality goals, but neither is brevity.

A narrow factual question remains narrow. Quality-max does not turn every query into a full report.

## 6. Customer-visible differentiation check

Before finishing a broad answer, ask internally:

> If the same user asked a capable general-purpose AI without FieldPilot, what concrete discoveries,
> comparisons, evidence controls, or decision consequences in this result would be hard to obtain from
> a generic first-pass answer?

If the answer is "none", improve the investigation rather than adding decorative framework prose.

The strongest differentiation should be visible in the findings themselves.

## 7. Human pilot signal boundary

Current qualitative signal:
- strong positive: non-obvious overlapping categories/products found;
- strong positive: representative examples mapped to overlapping elements;
- strong positive: unusually thorough similar-product discovery;
- negative: aggressive usage reduction reduced perceived richness;
- negative: the reduced-usage result felt too close to ordinary ChatGPT;
- owner direction: maximize quality/discovery depth even when usage increases.

This feedback changes the runtime optimization policy.

It does **not** prove:
- commercial superiority;
- willingness to pay;
- exact token savings or cost;
- general superiority over ChatGPT/Claude;
- market-wide preference.
