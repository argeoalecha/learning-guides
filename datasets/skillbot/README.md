# SkillBot

Used by: **[Claude Design guide](../../claude-design/claude-design_learning_guide.html)**

**Not a downloadable dataset.** SkillBot is an AI-powered learning coach the learner builds progressively across the guide, from a bare API call to a production-grade multi-agent tutoring system. There's no pre-made starter code — building it *is* the curriculum.

## Stack

- Language: Python
- SDK: `anthropic` (official Python SDK)
- Model: `claude-haiku-4-5-20251001` for early modules (cheap, fast iteration), moving to larger models as the guide progresses into agentic/production modules

## Progression across the guide

1. **Phase 1 (Foundations):** `ask_skillbot(topic: str) -> str` — a single function wrapping one API call, with token-count and cost tracking, `stop_reason` guards, prompt architecture, and conversation management. Capstone: **SkillBot Core**.
2. **Phase 2 (Tool Use):** tool-calling fundamentals, structured outputs, multi-tool pipelines, vision/document input. Capstone: **SkillBot with Tools**.
3. **Phase 3 (Agentic Systems):** agentic loops, multi-agent orchestration, evals & safety, production patterns. Capstone: **Production SkillBot**.
4. **Final Capstone:** the full tutoring system integrating all three phases.

## Notes

- Start with `pip install anthropic` and an `ANTHROPIC_API_KEY` in your environment — no other setup is required for Module 1.1.
- Because every module builds on the same `ask_skillbot`-derived codebase, keep it in a single project directory (e.g. `skillbot/`) rather than starting fresh per module.
