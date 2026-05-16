# ModrinthBadge-Unofficial — Project Context

## What This Is
A service that generates Modrinth badges for mod projects. Hosted at modrinth.roughness.technology on a personal Digital Ocean server.

## Structure — Two Distinct Components
This repo contains two separate concerns. Do not conflate them.

### Python API (repo root)
- Python Flask application, served by Gunicorn as a dedicated systemd service
- Key files: `ModrinthBadge.py`, `ModrinthApi.py`, `ModrinthBadgeReport.py`, `gunicorn.conf.py`
- Dependencies managed via system packages (see `DEVELOPMENT.md`); requires a `.env` file with configured values
- Run locally: `gunicorn ModrinthBadge:api -c gunicorn.conf.py`

### SvelteKit Frontend (`modrinth.roughness.technology/`)
- SvelteKit + TypeScript + Tailwind CSS, built statically and served by nginx
- pnpm for package management
- Has no `.git` folder — it is a child directory of this repo, not a separate repo
- See `modrinth.roughness.technology/.github/project-context.md` for frontend-specific context

## Runtime Architecture

```
nginx (reverse proxy)
  ├── /static, /*.html, /*.js, /*.css  →  serves website/ directly (no Gunicorn)
  └── /*.svg, /author/*.svg, /versions/*.svg  →  Gunicorn → Flask → badge generation
```

**`website/`** is the SvelteKit build output directory. It is not committed to git.
- Populated by running `pnpm run build` inside `modrinth.roughness.technology/`
- The SvelteKit adapter-static config sets `pages: '../website'` and `assets: '../website'`,
  writing output directly into the repo root's `website/` directory
- Flask is configured with `static_folder='website'` — in development it serves this
  directory directly; in production nginx serves it, bypassing Gunicorn for static files
- The frontend must be built before the Flask app can serve anything meaningful

## Branch Convention
- `main` only; no tags; HEAD is the deployed version

## Deployment (Digital Ocean personal server)
The two components deploy differently — treat them as separate operations:

**Python API update:**
1. `git pull` at repo root
2. `systemctl restart <api-service>` to apply changes

**Frontend update:**
1. `git pull` at repo root
2. `cd modrinth.roughness.technology && pnpm run build` — output lands in `../website/`
3. Nginx cache clear — no service restart needed

Do not restart the systemd service for frontend-only changes. Do not skip the service restart for API changes.
