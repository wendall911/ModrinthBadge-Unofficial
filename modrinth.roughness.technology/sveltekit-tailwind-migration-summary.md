Upgrade Summary: What Changed and What Broke

Context
- This file summarizes concrete upgrade changes and regressions encountered in this repository.
- It is intentionally different from the reusable migration plan.

pnpm: Changes and Issues
- Scripts and docs were moved to pnpm usage (`pnpm install`, `pnpm run ...`) instead of npm command examples.
- Project lockfile direction switched to pnpm.
- The repository policy has been updated to track `pnpm-lock.yaml` in git for reproducible installs.
- `.gitignore` no longer excludes `pnpm-lock.yaml`.

pnpm-specific issues encountered
- Some migration notes assumed pnpm installation instructions were needed, but pnpm was already installed on this workstation.
- Resulting rule for this environment: do not add global pnpm install instructions unless target machines actually need them.
- Lockfile policy decision: commit `pnpm-lock.yaml` as part of the migration changeset.

SvelteKit/Svelte 5: Changes and Issues
- State API migration from `$app/stores` to `$app/state` in migrated files.
- Template usages moved from store syntax (`$page`, `$navigating`) to state objects (`page`, `navigating`) where applicable.
- Event syntax and reactive syntax updates were applied in migrated components (for example `on:click` to `onclick`, and selected reactive updates).
- Deprecated config key migration: `kit.csrf.checkOrigin` was replaced with the current `csrf.trustedOrigins` shape.

SvelteKit-specific regressions encountered and fixes
- Regression: navigation progress bar (green bar) became visible at idle.
  - Cause: with `$app/state`, `navigating` is an object shape even when idle, so truthiness checks always pass.
  - Fix: check `navigating.to` instead of `navigating` object truthiness.
- Regression risk: routes still using `$app/stores` after partial migration.
  - Fix: migrate remaining files (notably `+error.svelte`) to `$app/state` usage.

Tailwind v4: Changes and Issues
- PostCSS plugin moved from `tailwindcss` to `@tailwindcss/postcss`.
- CSS import model updated for v4 (`preflight`, `theme`, `utilities`).
- Base typographic styles were moved to `src/base.css` and imported from `src/app.css`.
- Obsolete Tailwind config usage was removed from project references (`tailwind.config.ts` removed and related config references cleaned up).

Tailwind/theme-specific regressions encountered and fixes
- Regression: logo image appearance in light/dark themes became inconsistent during migration attempts.
  - Cause: theme-dependent class toggling for inversion became fragile during the upgrade.
  - Fix: centralized CSS approach with `.logo-img` filter defaults and `.dark .logo-img` override; simplified markup class usage.

Documentation and Workflow Updates
- README restructured to reflect modern development workflow.
- Added `Pre-publishing` section consolidating pre-release validation and build steps as separate commands.
- `preflight:release` script added to package.json: runs validation only (`pnpm install --frozen-lockfile`, `pnpm audit`, `pnpm outdated`, `pnpm run check`, `pnpm run lint`, `pnpm run test`).
- Static site build handled separately via `pnpm run build` (not part of preflight validation).
- README commands presented in concise format with inline comments for easy reference during releases.
- "Dev Notes" section renamed to "Development" for clarity.

Validation outcome for this repository
- Framework/type checks reached clean state (`svelte-check` with 0 errors and 0 warnings after fixes).
- Primary upgrade regressions identified in-session (navigation bar visibility and logo theme rendering) were corrected.

Related file
- Reusable process document: `sveltekit-tailwind-migration-plan.md`
