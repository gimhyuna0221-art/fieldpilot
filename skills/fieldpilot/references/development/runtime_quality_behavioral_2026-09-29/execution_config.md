# Local execution configuration

Candidate commit: f3dc869b032091d611dfa016007d2612bdd2fb03
Claude Code CLI: 2.1.284
Remote device used for model-runner dependency: DESKTOP-I3LPM8E

Remote Desktop was used only to prepare the isolated temporary project, launch/capture the local Claude CLI sessions, and retrieve local evidence. GitHub and Google Drive reads/writes were performed through their connectors, not through Remote.

## Fresh-session command shape

Strong live-web arm:

`claude -p --model sonnet --no-session-persistence --output-format stream-json --verbose --safe-mode --restricted --strict-mcp-config --no-chrome --permission-prompts none --tools Read,Glob,Grep,WebSearch,WebFetch --allowedTools Read,Glob,Grep,WebSearch,WebFetch --effort high`

Weak live-web arm:

`claude -p --model haiku --no-session-persistence --output-format stream-json --verbose --safe-mode --restricted --strict-mcp-config --no-chrome --permission-prompts none --tools Read,Glob,Grep,WebSearch,WebFetch --allowedTools Read,Glob,Grep,WebSearch,WebFetch`

Planned no-web/source-bound arms, if reached:

`claude -p --model haiku --no-session-persistence --output-format stream-json --verbose --safe-mode --restricted --strict-mcp-config --no-chrome --permission-prompts none --tools Read,Glob,Grep --allowedTools Read,Glob,Grep`

No Bash, PowerShell, Edit, Write, Notebook, browser automation, or MCP tools were exposed inside the model sessions.

Each case used a new non-persistent CLI process. The model prompt required reading the exact project-local SKILL.md first and required a SELF_CHECK with loaded path and both revisions. Frozen must-lists were not shown to the model.

Secrets and authentication material are intentionally omitted.
