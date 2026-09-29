# Runtime quality floor behavioral evaluation

These cases are the clean-session behavioral gate for runtime-quality-floor-01. Static tests are necessary but not sufficient.

## Protocol

1. Load the candidate skill from the exact worker-branch commit and record the actual SKILL.md path plus runtime_quality_extension_revision.
2. Run every case in a fresh session with no prior project/chat memory except the case fixture. Do not reuse the implementation conversation.
3. For RQ1 use a strong model with live web. For RQ2 use a genuinely weaker model with live web; do not simulate weakness by prompting the same model to act weaker.
4. For RQ3 use live web and inspect official/original pages where retrievable.
5. For RQ4 disable web/source retrieval. For RQ5 provide only the fixture and forbid web.
6. Save the model reply verbatim under outputs/. Do not hand-edit model outputs. Save a sidecar manifest with model, tool availability, loaded skill revision and retrieved source IDs/URLs.
7. Review each reply against the predeclared must list in cases.json. Record PASS/FAIL plus exact evidence lines in a compact matrix.
8. One bounded repair cycle is allowed for an implementation defect. Do not tune indefinitely to the observed outputs.

## Gate

Promotion requires all behavior families to pass: strong-live, weak-live floor, narrow official/source receipt, no-web degradation, source-bound ceiling, provisional locale and explicit-market override. A missing genuine weak-model run is NOT_RUN, not PASS.

Behavioral samples are bounded evidence. They do not establish universal model parity or guaranteed output quality.
