# University Physics I: Classical Mechanics

This repository contains a MyST Markdown edition of Julio Gea-Banacloche's
*University Physics I: Classical Mechanics*. The root-level MyST project is
the primary, editable edition. The previous PDF-derived LaTeX conversion is
preserved under [`latex/`](latex/) as a secondary source.

The Fall 2019 source textbook is available from
[ScholarWorks@UARK](https://scholarworks.uark.edu/oer/3/) and is licensed
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

## Repository layout

- [`myst.yml`](myst.yml) — project metadata and table of contents
- [`index.md`](index.md) and [`preface.md`](preface.md) — front matter
- [`chapters/`](chapters/) — thirteen MyST Markdown chapters
- [`images/`](images/) — 117 figures used by the MyST edition
- [`latex/`](latex/) — legacy LaTeX source and its image copy
- [`scripts/`](scripts/) — reproducible conversion and verification tools

## Preview and build

The project targets MyST CLI 1.10.1:

```bash
npm install -g mystmd@1.10.1
myst start
```

Build the static site with:

```bash
myst build --html
```

Generated files are written to `_build/` and are not committed. Pushes to
`main` also build and deploy the site through GitHub Pages.

## Verify the conversion

```bash
python3 scripts/verify_book.py
```

The verifier checks the chapter list, figure-reference parity with the legacy
LaTeX source, missing assets, semantic cross-references, and common conversion
artifacts.

Numbered headings, figures, equations, and tables are linked mechanically:

```bash
python3 scripts/link_cross_references.py          # update the Markdown
python3 scripts/link_cross_references.py --check  # read-only validation
python3 scripts/link_cross_references.py --check --diff
```

The linker fails on duplicate targets and reports unresolved or missing
references with file and line numbers, making exceptions straightforward to
review by hand. It is also run automatically by the LaTeX conversion script.

To regenerate the Markdown mechanically from the archived LaTeX extraction:

```bash
python3 scripts/convert_latex_to_myst.py
```

The generated chapters are intended to be reviewed and improved as MyST; the
LaTeX extraction remains available to cross-check any questionable passage.
