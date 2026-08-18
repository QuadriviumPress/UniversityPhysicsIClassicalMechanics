# University Physics I: Classical Mechanics

This repository contains a web-native [MyST Markdown](https://mystmd.org/) edition of
Julio Gea-Banacloche's *University Physics I: Classical Mechanics*. The root-level
MyST project is the primary, editable edition. The previous PDF-derived LaTeX
extraction is preserved under [`latex/`](latex/) for provenance and comparison.

**Live site:** [veillette.github.io/UniversityPhysicsIClassicalMechanics](https://veillette.github.io/UniversityPhysicsIClassicalMechanics/)

The book introduces classical mechanics for scientists and engineers, followed by
waves and a brief introduction to thermodynamics. It is organized into thirteen
chapters, from reference frames and kinematics through gravity, simple harmonic
motion, waves, and thermodynamics.

## Source and license

The Fall 2019 source textbook is available from
[ScholarWorks@UARK](https://scholarworks.uark.edu/oer/3/) and is licensed
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Suggested citation: Gea-Banacloche, J. (2019). *University Physics I:
Classical Mechanics*. University of Arkansas Open Educational Resources.

## Repository layout

- [`myst.yml`](myst.yml) — project metadata and table of contents
- [`index.md`](index.md) and [`preface.md`](preface.md) — front matter
- [`chapters/`](chapters/) — thirteen MyST Markdown chapters
- [`images/`](images/) — 117 figures used by the MyST edition
- [`latex/`](latex/) — legacy LaTeX extraction and its image copy
- [`scripts/`](scripts/) — conversion, cross-reference linking, and verification
- [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml) — GitHub Pages build

## Preview and build

The project targets MyST CLI 1.10.1. You need [Node.js](https://nodejs.org/) installed.

```bash
npm install -g mystmd@1.10.1
myst start          # local preview with live reload
myst build --html   # static site in _build/html/
```

Generated files under `_build/` are not committed.

## Deployment

Pushes to `main` trigger [GitHub Actions](.github/workflows/deploy.yml), which:

1. runs `python3 scripts/verify_book.py`
2. builds the HTML site with `myst build --html`
3. deploys `_build/html/` to GitHub Pages

You can also trigger a deploy manually from the Actions tab.

## Verification and maintenance

Structural checks (chapter count, figure parity with the legacy LaTeX source,
missing assets, cross-references, and common conversion artifacts):

```bash
python3 scripts/verify_book.py
```

Numbered headings, figures, equations, and tables are linked with
[`scripts/link_cross_references.py`](scripts/link_cross_references.py):

```bash
python3 scripts/link_cross_references.py          # update the Markdown
python3 scripts/link_cross_references.py --check  # read-only validation
python3 scripts/link_cross_references.py --check --diff
```

The linker fails on duplicate targets and reports unresolved or missing
references with file and line numbers. It runs automatically after LaTeX
conversion and as part of verification.

To regenerate the Markdown mechanically from the archived LaTeX extraction
(requires [Pandoc](https://pandoc.org/)):

```bash
python3 scripts/convert_latex_to_myst.py
```

The generated chapters are intended to be reviewed and improved as MyST; the
LaTeX extraction remains available to cross-check any questionable passage.

## Contributing

Corrections and improvements are welcome. Please open an issue or pull request.
Compare substantive changes against the [original OER](https://scholarworks.uark.edu/oer/3/)
when in doubt.
