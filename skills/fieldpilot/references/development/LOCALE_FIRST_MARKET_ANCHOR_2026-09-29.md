# Locale-First Market Anchor — 2026-09-29

## Trigger

User friction identified two linked problems:

1. Requiring a Korean user to repeatedly say "한국 시장" adds unnecessary prompt burden.
2. When geography is left unspecified, web-search abundance can make English/US sources dominate even though the user's likely commercial context is elsewhere.

The previous protection — never infer geography from language — prevented false jurisdiction claims, but it also removed a useful search prior.

## Design decision

Replace "language cannot affect geography" with:

> Language may set the first search market or language cluster, but never proves target geography, legal jurisdiction, customer location, demand or willingness to pay.

The runtime pattern is:

`LOCAL-FIRST -> GLOBAL-BEST -> LOCAL-TRANSFER`
## Anchor precedence

1. Explicitly stated market
2. Verified product/store/contract/distribution market
3. Strong case-relevant local signal
4. Provisional language market
5. Language cluster
6. Global unresolved

Higher-priority evidence always wins.

Examples:
- Korean -> provisional South Korea when no stronger conflicting signal exists.
- Japanese -> provisional Japan.
- English -> English-speaking/global cluster, not US.
- Spanish -> Spanish-speaking cluster, not Spain/Mexico by default.
- Portuguese/French/Arabic -> language cluster unless stronger evidence exists.

Account/device/IP/remembered owner location is not used.
## Transfer discipline

Foreign evidence is useful for discovering better products, methods and patterns, but must not silently become local evidence.

Material transfer checks include:
- buyer/payer match;
- price and purchasing context;
- platform/distribution availability;
- regulation/certification;
- cultural/workflow fit.

A US $50 product is evidence that a product exists at that price in that context. It is not evidence of Korean willingness to pay roughly the converted amount.

## Korea behavior

Two states are intentionally separate:

- `FULL_KOREA_CLOSURE`: Korea is established by explicit or verified case evidence.
- `PROVISIONAL_KOREA_FIRST_PASS`: Korean language supplies a first search prior only.

The provisional mode can search Korean competitors, prices, platforms, manual alternatives and public evidence immediately. Korea-specific legal/regulatory conclusions remain conditional until the market is established.
## Expected benefit

- less repeated user prompting;
- less accidental US-default behavior;
- better local competitor recall;
- global references are still retained;
- clearer separation between discovery priority and claim strength.

## Claim boundary

This is a product-design change, not empirical proof that language-first routing improves market-research accuracy across all languages or countries.

Behavioral validation should include at least:
- Korean prompt with no country;
- English prompt with no country;
- Spanish prompt with no country;
- Korean prompt explicitly targeting the United States;
- English prompt explicitly targeting Korea.

Expected behavior is routing correctness and claim discipline, not a universal quality score.
