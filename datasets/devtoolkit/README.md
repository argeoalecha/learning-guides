# DevToolkit

Used by: **[Claude Code guide](../../claude-code/claude-code_learning_guide.html)**, **[Claude Ecosystem Mastery guide](../../claude-ecosystem-mastery/claude-ecosystem-mastery_learning_guide.html)**

**Not a downloadable dataset.** DevToolkit is a scaffolded application the learner builds and extends *with* Claude Code across both guides — the exercise is the act of building it, so no starter code is provided here. This file is a spec so both guides stay consistent about what it is.

## Stack

- Runtime: Node.js 20 + TypeScript (strict)
- Framework: Express.js
- Database: PostgreSQL via Prisma ORM
- Auth: JWT (24h expiry) + bcryptjs (12 rounds)
- Validation: Zod for all external inputs
- Testing: Vitest + Supertest

## Starting shape

DevToolkit is **not** the same project as the Ecosystem Mastery guide's own example (TaskFlow) — it's the Claude Code guide's equivalent, built with that guide's CLI Foundations workflow (`claude`, then ask it to scaffold Express + TypeScript with a `/health` endpoint returning `{"status":"ok"}`, then connect an MCP server). By the time the Claude Code guide's exercises begin, DevToolkit is assumed to already have `/health` and `/users` (GET, POST) endpoints and at least one MCP server connected — see that guide's Module 1.1 Capstone.

## Where it goes from there

The Claude Code guide adds CLAUDE.md + memory, hooks (TypeScript type-check on edit, `rm -rf` guard), subagent-based health checks, autonomous loops, an `/api-endpoint` code-generation skill, and a CI/CD pipeline with prompt-injection defenses — all layered onto this same DevToolkit codebase.

See also: [`taskflow/`](../taskflow/) — the Ecosystem Mastery guide's own, separate example project.

If you want a literal starting point instead of scaffolding from a blank directory, `npx express-generator --no-view devtoolkit` plus `npm install -D typescript ts-node @types/express` gets you an equivalent bare-bones base to hand to Claude Code.
