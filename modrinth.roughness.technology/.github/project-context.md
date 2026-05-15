# modrinth.roughness.technology — Project Context

## What This Is
SvelteKit frontend for the ModrinthBadge-Unofficial service, hosted at modrinth.roughness.technology.

## IMPORTANT: Subdirectory Context
This directory is a child of the `ModrinthBadge-Unofficial` repository. There is no `.git` here — git operations must be run from the parent repo root. If you are opened at this directory level, the parent repo is at `../` (i.e. `ModrinthBadge-Unofficial/`).

Do not treat this as a standalone repository. Do not run `git` commands from this directory. All git operations belong at `ModrinthBadge-Unofficial/`.

## Tech Stack
- SvelteKit + TypeScript + Tailwind CSS
- pnpm
- Playwright for tests

## Branch Convention
- `main` only (inherited from parent repo); HEAD is deployed

## Deployment
Deployed statically on a Digital Ocean personal server, served by nginx.

**Frontend update steps:**
1. `git pull` at parent repo root (`ModrinthBadge-Unofficial/`)
2. Build: `pnpm build` from this directory
3. Nginx cache clear — no systemd service restart needed for frontend changes

**Python API changes** are a separate concern handled at the parent repo level — see `../.github/project-context.md`.
