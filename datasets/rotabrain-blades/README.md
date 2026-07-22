# rotabrain-blades

Used by: **[Terminal, Git & GitHub guide](../../terminal-git/terminal-git-github_learning_guide.html)**

**Not a downloadable dataset.** rotabrain-blades is a Next.js web app deployed on Vercel, used purely as a realistic local git repository to practice terminal navigation, git operations, and GitHub workflows against — the guide never asks you to build its business logic, only to operate on it as a repo.

## What it is

A Next.js app with at least one component the exercises reference directly (`src/components/HealthScoreCard.tsx`), deployed on Vercel — standing in for "a real-world frontend repo with `node_modules`, a `src/` tree, and a `package.json`" so terminal/git exercises (navigation, `find`, `grep -r`, aliases, pipes/redirection, stashing, branching) have realistic ground to run on.

## Minimal equivalent to clone/create locally

Any Next.js app scaffolded with `npx create-next-app@latest rotabrain-blades` and a placeholder `src/components/HealthScoreCard.tsx` component satisfies every exercise in this guide — the guide does not depend on rotabrain-blades' actual product logic, only on it being a real, buildable Next.js repo with a typical file tree.

## Notes

- If you already have any personal or work Next.js/Vercel repo, use that instead and swap `rotabrain-blades` for its actual name throughout the exercises — the guide's terminal/git skills transfer directly.
