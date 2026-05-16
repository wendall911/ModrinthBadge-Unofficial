## Architecture Overview

This project has two components that must be understood together:

- **Repo root** — Python/Flask API that generates SVG badges and serves the frontend
- **`modrinth.roughness.technology/`** — SvelteKit static site; builds its output into `../website/` (repo root)
- **`website/`** — SvelteKit build output. Flask serves this directory as static files. Not committed to git; populated by the frontend build step.

In production, nginx sits in front of Gunicorn and serves `website/` directly for static file requests, routing only badge routes to Gunicorn/Flask.

---

## Install Dependencies — Fedora / Rocky Linux 8/9 / RHEL 8/9

```
dnf install dejavu-sans-fonts python3-pillow python3-gunicorn python3-dotenv python3-flask
```

Frontend requires Node.js and pnpm:
```
npm install -g pnpm
```

---

## Local Development

**Step 1 — Build the frontend**

The SvelteKit app must be built before the Flask app can serve it. The build
writes output directly into `../website/` (the repo root's `website/` directory).

```
cd modrinth.roughness.technology
pnpm install
pnpm run build
cd ..
```

**Step 2 — Configure environment**

Create a `.env` file at repo root with required values (refer to `.env.example` if present).

**Step 3 — Run the API**

Flask serves both the badge routes and the built frontend from `website/`:

```
gunicorn ModrinthBadge:api -c gunicorn.conf.py
```

Site available at `http://localhost:8000` (or configured port).

**Frontend-only changes**

Re-run the frontend build; no Flask restart needed:
```
cd modrinth.roughness.technology && pnpm run build
```

---

## Deployment

See `.github/project-context.md` for the full deployment sequence and the distinction
between API-only and frontend-only deploys.

Reference: https://docs.gunicorn.org/en/stable/deploy.html
