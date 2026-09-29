# Market Anchor & Expansion — market-anchor-01

This module removes unnecessary geography questions without turning language into a false fact.

Its operating pattern is:

`LOCAL-FIRST -> GLOBAL-BEST -> LOCAL-TRANSFER`

Language may set a **provisional search prior**. It never, by itself, proves the user's actual target market, legal jurisdiction, customer location, or launch geography.

## 1. Market-anchor precedence

Resolve the strongest available anchor in this order:

1. `EXPLICIT_MARKET` — the user directly names a country/region/market.
2. `VERIFIED_CASE_MARKET` — the product/store/contract/distribution scope establishes a market.
3. `STRONG_LOCAL_SIGNAL` — a case-relevant currency, local platform, jurisdiction-specific regulation, local store/channel, domain, addressable customer scope, or other concrete local fact strongly identifies the market.
4. `PROVISIONAL_LANGUAGE_MARKET` — the conversation language is used only as the first search prior.
5. `LANGUAGE_CLUSTER` — for widely multinational languages, use the language-market cluster rather than inventing one country.
6. `GLOBAL_UNRESOLVED` — no useful market anchor exists.

Higher-precedence evidence always overrides lower-precedence priors.
## 2. Language is a search prior, not geography proof

Examples:

- Korean with no contrary case evidence -> provisional South Korea first-pass market.
- Japanese with no contrary case evidence -> provisional Japan first-pass market.
- English -> English-speaking/global cluster; **never default to the United States**.
- Spanish -> Spanish-speaking cluster; never default to Spain, Mexico or another country without evidence.
- Portuguese -> Lusophone cluster; never default to Brazil or Portugal without evidence.
- French -> Francophone cluster.
- Arabic -> Arabic-speaking cluster.

For other languages, use a country prior only when the language is strongly concentrated in one relevant commercial ecosystem. Otherwise use a language cluster.

Mixed-language prompts do not trigger arbitrary country selection. Use the language carrying the product/customer context, or keep a cluster/UNKNOWN when no defensible prior exists.

Never use:
- account country;
- device/physical location;
- remembered owner location;
- IP-derived location;
as a market anchor unless the user explicitly supplied that information for this task.
## 3. Local-first research

When the anchor is explicit, verified, strong-local-signal, or a defensible provisional country prior, search that market first for the decision-relevant classes:

- local direct competitors;
- local bundled/adjacent incumbents;
- local free/manual/do-nothing substitutes;
- local price, billing, tax, procurement or refund conditions when material;
- local platforms and distribution channels;
- local customer language/problem framing;
- local regulation/certification when material;
- local official statistics or industry evidence when the proposition requires them.

A provisional language anchor controls search order, not claim strength. Jurisdiction-sensitive claims remain provisional until independently established by case evidence or are explicitly stated as conditional.
## 4. Global-best expansion

After the local/language first pass, expand globally for:

- category leaders;
- specialist products;
- high-quality professional research;
- superior workflows or interaction patterns;
- adjacent/component/cross-category references;
- technical standards;
- emerging product capabilities;
- success/failure cases;
- better evidence sources unavailable locally.

Do not prefer the United States merely because English-language sources are abundant or highly ranked.

The goal is to find the best transferable reference, not the most visible English result.

## 5. Local-transfer gate

A global finding enters the local decision only after checking transferability when material:

```text
GLOBAL_REFERENCE
LOCAL_JOB_MATCH
LOCAL_BUYER_OR_PAYER_MATCH
LOCAL_PRICE_PURCHASING_CONTEXT
LOCAL_PLATFORM_DISTRIBUTION_MATCH
LOCAL_REGULATORY_CERTIFICATION_MATCH
LOCAL_CULTURAL_WORKFLOW_MATCH
TRANSFER_STATE = DIRECT / PLAUSIBLE_WITH_CAVEATS / WEAK_PROXY / NOT_TRANSFERABLE / UNKNOWN
```

Examples:
- a US $50 product does not establish a Korean ₩70,000 market;
- US adoption does not establish Korean demand;
- a global SaaS feature may be directly comparable if it is actually available to the local buyer on the same terms;
- a regulatory or certification difference may make a technically similar product non-transferable.
## 6. Question behavior

Do not ask "which country?" merely because geography was not explicitly stated.

Instead:
1. establish the best provisional anchor;
2. perform the useful first-pass research;
3. expand globally;
4. apply the local-transfer gate;
5. ask a geography question only if the remaining ambiguity can materially reverse the recommendation and cannot be resolved from accessible case evidence.

When the provisional anchor materially affects the answer, disclose it in one short line such as:

> 별도 지역 지정이 없어 한국어 기준으로 한국을 1차 시장으로 보고, 해외 대안까지 확장했습니다.

Do not turn this into an intake form.

If the user later names another market, rerun only the geography-dependent slots as a decision delta.

## 7. Claim ceilings

Never convert:
- conversation language -> confirmed launch market;
- local search priority -> proven local demand;
- global leader -> local leader;
- foreign price -> local WTP;
- foreign market size -> local market size;
- local search miss -> absence of local competition.

Use `PROVISIONAL_MARKET_ANCHOR` internally until stronger case evidence establishes the market.
## 8. Interaction with Korea local coverage

For Korean-language prompts with no stronger contradictory signal:

- set `PROVISIONAL_MARKET_ANCHOR = South Korea`;
- run a **provisional Korea-first discovery pass**;
- then run global-best expansion;
- apply local-transfer checks before using foreign evidence in the Korean decision.

This does **not** mean Korean language establishes Korean legal jurisdiction.

If the user explicitly says the target is Korea, or the product/store/contract scope establishes Korea, activate the full Korea local coverage contract in `KOREA_LOCAL_DISTRIBUTION.md`.

If Korea is only provisional, local competitor/source discovery may run immediately, but jurisdiction-specific legal/compliance conclusions stay conditional until market scope is established.

## 9. Quality check

Before finishing, ask internally:

1. Did source abundance silently turn English into "US"?
2. Did the first search pass reflect the user's likely market/language context?
3. Did global references add genuinely better examples instead of replacing local evidence?
4. Did every material foreign fact pass a transfer check?
5. Did we avoid asking the user for geography when a useful provisional search could proceed?
