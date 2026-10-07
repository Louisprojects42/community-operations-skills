# Community Operations Skills

Build durable Discord workflows, review Supabase authorization, prepare public event reports, and compare game trading routes.

Four portable Agent Skills for Claude and ChatGPT/Codex. They contain original workflow guidance and synthetic examples, with no application source, credentials, live data, or project-specific infrastructure.

## Skills

| Skill | Use it for |
| --- | --- |
| [Durable Discord Workflows](skills/discord-durable-workflows/SKILL.md) | Build or repair Discord attendance, points, and background workflows that must survive restarts and duplicate events. Use for persistent bot state and cross-service side effects. |
| [Supabase Authorization Review](skills/supabase-authorization-review/SKILL.md) | Review or fix Supabase row policies and backend authorization across browser, database, and bot services. Use for ownership, tenant isolation, role checks, or admin actions. |
| [Community Event Reporting](skills/community-event-reporting/SKILL.md) | Turn community or gaming event notes into an internal after-action report and a separately sanitized public recap. Use for event write-ups and publication previews. |
| [Game Trade Route Analysis](skills/game-trade-route-analysis/SKILL.md) | Compare in-game commodity routes using cargo, budget, stock, demand, fees, travel time, and data freshness. Use for game economy tools; excludes real-money trading advice. |

## Try a workflow

- `discord-durable-workflows`: Make this bot workflow survive duplicate events and restarts.
- `supabase-authorization-review`: Review the authorization for this browser-to-database workflow.
- `community-event-reporting`: Prepare a factual public recap from these event notes.
- `game-trade-route-analysis`: Compare these in-game routes with explicit cargo and budget constraints.

Each skill is self-contained under skills/. Its SKILL.md is the entrypoint; references/ provides a worked example; agents/openai.yaml supplies optional OpenAI UI metadata. The two helper-bearing skills across this collection need Python 3.11+; other workflows use the tools already available in the host.

Read [installation and compatibility](INSTALL.md). Each skill works from the same source folder across hosts; there are no separate copies to drift apart. Host permissions and available tools still determine what can execute.

## Check and package

From this folder, using Python 3.11+ with the standard library:

```text
python -B scripts/validate.py
python -B -m unittest discover -s tests -v
python -B scripts/package.py
```

The last command creates one ZIP per skill under dist/. Each archive has one top-level skill folder. Validation checks structure, links, metadata, obvious private-path/credential patterns, and Python syntax. Run the unittest command only in packs containing tests/. Tests check helper behavior where present. [Behavioral evaluation prompts](evals/README.md) are provided for manual testing; no AI-model pass rate is claimed. CI is included for Windows and Linux and has not been run remotely.

## Sharing

This folder is an independent GitHub-ready repository. Review the files, publish it to a repository you own, and share its URL. plugin.json and .claude-plugin/plugin.json provide OpenAI/portable and Claude packaging metadata. No marketplace listing, remote repository, or publication is created automatically.

The newly authored content and helpers are MIT licensed; see [LICENSE](LICENSE) and [provenance](PROVENANCE.md). Linked documentation and original project materials retain their own terms.
