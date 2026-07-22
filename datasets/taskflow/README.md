# TaskFlow

Used by: **[Claude Ecosystem Mastery guide](../../claude-ecosystem-mastery/claude-ecosystem-mastery_learning_guide.html)**

**Not a downloadable dataset.** TaskFlow is a small Next.js + Supabase task-management app the learner scaffolds and extends across the guide — the point is building it with Claude Code, not downloading it pre-built. This file is a spec for consistency. If you don't have it locally, any comparable Next.js/Supabase (or similar full-stack) repo you already have open works as a substitute.

## Stack

- Frontend: Next.js (App Router)
- Backend/DB: Supabase (Postgres)
- Core entity: `tasks` table — id, title, severity (P0–P3), status, assignee, created_at

## Progression across the guide

1. **Phase 1 (CLI Foundations):** scaffold the Next.js + Supabase app, connect the first MCP server.
2. **Phase 2 (Skills):** author a `task-triage` skill that reads open tasks and produces a priority-ranked digest using a P0–P3 severity rubric.
3. **Phase 3 (API Connectors):** connect a Supabase MCP server (project scope), a filesystem MCP server (local scope), and a personal MCP server (user scope) — with a written audit of what each can access.
4. **Phase 4 (Building MCP Servers):** build `taskflow-mcp` — a custom MCP server exposing `list_open_tasks`, `create_task`, `close_task` tools against the Supabase `tasks` table.
5. **Phase 5 (Plugins):** package the `task-triage` skill and `taskflow-mcp` server together as a `taskflow-toolkit` plugin, installable via `--plugin-dir` and (optionally) a marketplace.
6. **Phase 6 (Agent SDK):** build a standalone, unattended TaskFlow triage agent using the Agent SDK — connects to `taskflow-mcp`, assigns severities with a custom tool, and is guarded by an explicit `allowedTools` list plus a hook that blocks it from ever calling `close_task`.

## Severity rubric (used throughout)

| Severity | Meaning |
|---|---|
| P0 | Data loss, auth bypass, or the app fails to build |
| P1 | A core user flow is broken with no workaround |
| P2 | A secondary flow is broken, or a P1 has a workaround |
| P3 | Cosmetic, or an enhancement request |

See also: [`devtoolkit/`](../devtoolkit/) — the separate example project used by the companion Claude Code guide.
