# AGENTS.md

## Standard

This book follows the [QuadriviumPress MyST baseline](https://github.com/QuadriviumPress/bindery/blob/main/doc/myst-baseline.md) and the [presentation skill](https://github.com/QuadriviumPress/bindery/blob/main/skills/quadrivium-myst-presentation/SKILL.md).

## Commands

```bash
npm run start
npm run build
npm run verify
npm run check
```

`npm run check` is the production-equivalent verification and HTML build.

## Intentional differences

- `verify` runs `python3 scripts/verify_book.py`, copied from bindery's `scripts/myst-verify-base.py`.

## Presentation gap

Problems are heading trees (`### Problem 1`), sometimes with an explicit target. They are not `{exercise}` directives, and answers are not `{solution}` dropdowns. The LibreTexts heading style is kept until a later presentation pass.
