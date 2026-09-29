# Frozen input pointer

All behavioral inputs are frozen at candidate commit:

`f3dc869b032091d611dfa016007d2612bdd2fb03`

Canonical case definitions:

- `skills/fieldpilot/tests/runtime_quality/cases.json`
- `skills/fieldpilot/tests/runtime_quality/README.md`

The runner used the exact prompts and supplied fixture from those files. The predeclared must-lists were retained for the later independent reviewer and were not injected into the model prompts.

Candidate lineage:

- base: `c59dc56c6765cdaf3d69bf4b5398486bb96cfa06`
- head: `f3dc869b032091d611dfa016007d2612bdd2fb03`
- PR: #6, draft, unmerged at runner baseline verification
