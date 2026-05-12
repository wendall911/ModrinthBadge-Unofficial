SvelteKit + Tailwind Migration Plan (Reusable)

Purpose
- Provide a repeatable process to migrate SvelteKit projects to current SvelteKit and Tailwind versions with minimal regressions.
- Keep package manager, framework APIs, and styling toolchain aligned.

Scope
- Package manager standardization (pnpm preferred)
- All package upgrades (`dependencies` and `devDependencies`)
- SvelteKit state/store API migration
- Tailwind v4 migration
- Regression checks and validation

Phase 1: Baseline and Safety
1. Record current state
   - Save current dependency versions from package.json.
   - Capture build/check/test status before changes.
   - Snapshot git status and last known good commit.
2. Confirm package manager strategy
   - Choose one lockfile and one package manager command set.
   - If using pnpm, ensure scripts and docs use pnpm commands.
   - Define lockfile policy explicitly:
     - Recommended: commit `pnpm-lock.yaml` for reproducible installs.
     - Alternative: if intentionally ignored, document why and accept non-reproducible install risk.
   - Remove or stop updating conflicting lockfiles (`package-lock.json`, `yarn.lock`) during migration.
   - Update `.gitignore` to match the chosen lockfile policy.
   - Update README and developer docs to pnpm commands (`pnpm install`, `pnpm run dev`, `pnpm run build`, etc.).
   - Create a pre-publishing workflow in package.json scripts:
     - Add `preflight:release` script that runs `pnpm install --frozen-lockfile`, audit, outdated check, type/lint checks, tests, and build.
     - Document the pre-publishing workflow in README with clear command examples and inline comments for easy reference during releases.
   - Environment policy: do not add pnpm installation steps when pnpm is already available on target workstations/CI images.
3. Create rollback point
   - Tag or note a pre-migration commit SHA.

Phase 2: Dependency Upgrade
0. Upgrade all direct packages in package.json
   - Update both `dependencies` and `devDependencies` to current compatible versions.
   - Do not stop after framework-only packages; include runtime, tooling, test, and lint packages.
1. Upgrade core stack first
   - svelte
   - @sveltejs/kit
   - @sveltejs/vite-plugin-svelte
   - vite
   - typescript
2. Upgrade styling/tooling stack
   - tailwindcss
   - @tailwindcss/postcss (for Tailwind v4)
   - postcss, autoprefixer
   - linting/formatting/test packages
3. Install missing type packages
   - Add @types/node if tsconfig or tooling references Node types.

Phase 3: SvelteKit API Migration
1. Move from old stores API where required
   - Replace imports from $app/stores with $app/state where applicable.
2. Replace store-style template usage
   - Replace $page, $navigating, etc. with page, navigating when using $app/state.
3. Validate condition checks for state objects
   - Do not rely on object truthiness for navigation indicators.
   - Preferred check: navigating.to (or a similarly explicit field) to avoid always-on UI.
4. Update event and reactivity syntax as needed for Svelte 5
   - Migrate on:click to onclick where required by code style/migration goals.
   - Replace legacy reactive patterns with runes where intentionally adopted.

Phase 4: Tailwind v4 Migration
1. Update PostCSS plugin usage
   - tailwindcss plugin key -> @tailwindcss/postcss.
2. Move to v4 CSS import style
   - Use preflight/theme/utilities imports.
   - Keep project base styles in a dedicated CSS file if helpful.
3. Remove obsolete Tailwind config usage
   - If project does not use JS/TS Tailwind config with v4, remove dead config files.
   - Update related tool configs (for example component generator settings) to avoid stale references.
4. Validate light/dark image rendering
   - If logos/icons are PNG assets, prefer a stable CSS class strategy over reactive class toggles for inversion.
   - Example pattern from migration: apply inversion filter to `.logo-img` by default and disable it in `.dark .logo-img`.
   - Keep image class usage simple in markup and avoid fragile theme-store-dependent class interpolation.

Phase 5: Regression Prevention Checklist
- Navigation/loading indicators are hidden at idle and visible only during transitions.
- Error routes still render correct status/message after state API changes.
- Theme toggles and icon logic still work in light and dark mode.
- PNG/SVG branding images render correctly in both light and dark themes (no washed-out or invisible logo).
- Links/buttons do not use invalid native HTML attributes.
- Script commands consistently use selected package manager.
- No duplicated or malformed markup introduced during migration edits.

Phase 6: Validation Gates
1. Static checks
   - Run framework sync/check command.
   - Run TypeScript checks.
   - Run package outdated check and confirm no remaining direct package upgrades are pending.
2. Lint and format checks
3. Unit/integration tests
4. Manual smoke tests
   - Home route, error route, navigation transitions, theme switch, key UI flows.
5. Final diff review
   - Ensure each changed file has a migration reason.
   - Remove unrelated edits.

Deliverables
- Updated package graph (`dependencies` and `devDependencies`) and lockfile strategy
- Migrated app/state usage
- Tailwind v4-compatible CSS/PostCSS setup
- Pre-publishing workflow script and README documentation
- Passing checks/tests
- Short migration notes for other developers

Common Pitfalls and Fixes
- Pitfall: Progress bar always visible after switching to $app/state.
  Fix: Use explicit field checks (example: navigating.to) instead of checking navigating object truthiness.
- Pitfall: TypeScript error for missing Node type definitions.
  Fix: Add @types/node as a dev dependency.
- Pitfall: Old package-manager commands remain in scripts/docs.
  Fix: Normalize scripts/docs to the chosen manager.
- Pitfall: README/docs were not migrated with the package-manager switch.
   Fix: Update README command examples and installation instructions to match chosen package-manager policy.
- Pitfall: Migration upgrades only framework packages and misses other direct packages.
   Fix: Explicitly upgrade all direct packages in `dependencies` and `devDependencies`, then verify with an outdated check.
- Pitfall: pnpm migration done, but lockfile policy is unclear or mixed lockfiles remain.
   Fix: Decide whether `pnpm-lock.yaml` is committed or intentionally ignored, document the rationale, and enforce one-lockfile policy in repo.
- Pitfall: Dark/light logo filter fix regresses during Tailwind migration.
   Fix: Keep theme-dependent image filtering in centralized CSS (for example `.logo-img` + `.dark .logo-img`) and include visual smoke tests.
- Pitfall: Deprecated config keys remain in framework config.
  Fix: Replace deprecated keys with current equivalents and re-run checks.

Reusable Command Sequence (template)
- install deps
- run framework sync/check
- run lint
- run tests
- run build

Note
- Adapt this plan to the project risk profile. For high-traffic apps, stage migration in smaller commits and validate each phase independently.
