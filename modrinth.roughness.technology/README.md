# modrinth.roughness.technology

modrinth.roughness.technology Website

## Install dependencies

```bash
pnpm install
```

## Why pnpm?

This project uses [pnpm](https://pnpm.io/) for faster, more efficient dependency management. If you don't have pnpm installed, run:

```bash
npm install -g pnpm
```

All npm/yarn commands can be replaced with their pnpm equivalents (e.g., `pnpm run dev`, `pnpm run build`).

## Development

```bash
pnpm run dev   # runs dev instance for dev work on site
```

## Pre-publishing

```bash
pnpm run preflight:release  # validates dependencies, lints, tests
pnpm run build              # builds site in ../website
```
