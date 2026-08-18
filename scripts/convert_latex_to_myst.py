#!/usr/bin/env python3
"""Split the legacy LaTeX extraction into a root-level MyST book.

The source is an already extracted LaTeX document. Pandoc performs the
LaTeX-to-Markdown conversion; this wrapper supplies stable chapter boundaries,
frontmatter, image paths, and a few MyST-oriented normalizations.
"""

from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "latex" / "UniversityPhysicsIClassicalMechanics.tex"
CHAPTERS = ROOT / "chapters"

TITLES = [
    "Reference frames, displacement, and velocity",
    "Acceleration",
    "Momentum and Inertia",
    "Kinetic Energy",
    "Interactions and energy",
    "Interactions, part 2: Forces",
    "Impulse, Work and Power",
    "Motion in two dimensions",
    "Rotational dynamics",
    "Gravity",
    "Simple harmonic motion",
    "Waves in one dimension",
    "Thermodynamics",
]


def slugify(title: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return slug


def pandoc(fragment: str) -> str:
    wrapper = "\\documentclass{article}\n\\usepackage{amsmath,amssymb,graphicx}\n\\begin{document}\n" + fragment + "\n\\end{document}\n"
    with tempfile.NamedTemporaryFile("w", suffix=".tex", encoding="utf-8") as source:
        source.write(wrapper)
        source.flush()
        result = subprocess.run(
            [
                "pandoc",
                source.name,
                "--from=latex",
                "--to=markdown+tex_math_dollars+fenced_divs",
                "--wrap=none",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
    return result.stdout


def normalize(markdown: str, chapter: int) -> str:
    # Pandoc emits raw attributes on unnumbered headings. MyST does not need
    # them because the printed section numbers already live in the headings.
    markdown = markdown.replace(" .unnumbered", "")
    markdown = re.sub(r"^# ", "## ", markdown, flags=re.MULTILINE)
    markdown = re.sub(r"^## ", "### ", markdown, flags=re.MULTILINE)
    # Restore the intended hierarchy after the simultaneous-looking regexes.
    markdown = re.sub(r"^### (\d+\.\d+\s)", r"## \1", markdown, flags=re.MULTILINE)
    markdown = re.sub(r"^### (\d+\.\d+\.\d+\s)", r"### \1", markdown, flags=re.MULTILINE)
    markdown = re.sub(r"\A(?:### .+\n\n){2}", "", markdown)

    image_by_stem = {path.stem: path.name for path in (ROOT / "images").iterdir() if path.is_file()}
    normalized_lines: list[str] = []
    for line in markdown.splitlines():
        if line.startswith("![") and "](" in line:
            target_start = line.index("](") + 2
            target_end = line.rfind("){" if "){" in line else ")")
            target = line[target_start:target_end]
            filename = image_by_stem.get(Path(target).stem, Path(target).name)
            line = f"![image](../images/{filename})"
        normalized_lines.append(line)
    markdown = "\n".join(normalized_lines)
    markdown = re.sub(r"^::: center\n|^:::\n", "", markdown, flags=re.MULTILINE)
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    return markdown.strip() + "\n"


def main() -> None:
    text = SOURCE.read_text(encoding="utf-8")
    starts = list(re.finditer(r"^\\section\*\{Chapter (\d+)\}\s*$", text, re.MULTILINE))
    if len(starts) != len(TITLES):
        raise SystemExit(f"expected {len(TITLES)} chapters, found {len(starts)}")
    CHAPTERS.mkdir(exist_ok=True)

    preface_start = text.index("\\section*{Preface}")
    preface_fragment = text[preface_start:starts[0].start()]
    preface_markdown = pandoc(preface_fragment)
    preface_markdown = preface_markdown.replace(" .unnumbered", "")
    preface_markdown = re.sub(r"^# Preface[^\n]*\n+", "", preface_markdown, count=1, flags=re.MULTILINE)
    preface_markdown = re.sub(r"^# ", "## ", preface_markdown, flags=re.MULTILINE)
    (ROOT / "preface.md").write_text(
        '---\ntitle: Preface\nshort_title: Preface\nlabel: preface\n---\n\n' + preface_markdown.strip() + "\n",
        encoding="utf-8",
    )
    for index, match in enumerate(starts):
        number = int(match.group(1))
        end = starts[index + 1].start() if index + 1 < len(starts) else text.index("\\end{document}", match.end())
        fragment = text[match.start():end]
        title = TITLES[index]
        filename = f"ch-{number:02d}-{slugify(title)}.md"
        frontmatter = (
            "---\n"
            f'title: "{number}. {title}"\n'
            f'short_title: "Chapter {number}"\n'
            f"label: ch-{number}\n"
            "---\n\n"
        )
        (CHAPTERS / filename).write_text(frontmatter + normalize(pandoc(fragment), number), encoding="utf-8")
        print(filename)


if __name__ == "__main__":
    main()
