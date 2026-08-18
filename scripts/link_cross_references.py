#!/usr/bin/env python3
"""Turn printed book numbers into native MyST cross-references.

The PDF-derived Markdown contains literal section, figure, equation, and table
numbers.  This script inventories the corresponding targets, gives each one a
stable label, and links prose references to those labels.  It is deliberately
conservative: duplicate targets are fatal, unknown references are reported,
and ``--check`` detects both stale generated output and unresolved references.

Run ``python3 scripts/link_cross_references.py`` to update the book, or add
``--check`` for a read-only CI/verification pass.
"""

from __future__ import annotations

import argparse
import difflib
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = ROOT / "chapters"

NUMBER = r"[1-9]\d*(?:\.\d+)+"
HEADING_RE = re.compile(rf"^(##|###)\s+({NUMBER})\s+(.+?)(?:\s+\{{#[^}}]+\}})?\s*$")
GENERIC_HEADING_RE = re.compile(r"^(#{2,6})\s+(.+?)\s+\{#([^}]+)\}\s*$")
IMAGE_RE = re.compile(r"^!\[([^]]*)\]\(([^)]+)\)\s*$")
FIGURE_CAPTION_RE = re.compile(rf"^Figure\s+({NUMBER}):\s*(.*)$")
LINKED_FIGURE_CAPTION_RE = re.compile(
    rf"^\{{numref\}}`Figure %s <fig-({NUMBER})>`:\s*(.*)$"
)
TABLE_CAPTION_RE = re.compile(rf"^Table\s+({NUMBER}):\s*(.*)$")
TAG_RE = re.compile(rf"\\tag\{{({NUMBER})\}}")
LABEL_RE = re.compile(r"^(?:\(([^)]+)\)=|:label:\s*(\S+))$")
CHAPTER_FILE_RE = re.compile(r"ch-(\d+)-")


@dataclass
class Inventory:
    sections: set[str] = field(default_factory=set)
    figures: set[str] = field(default_factory=set)
    equations: set[str] = field(default_factory=set)
    tables: set[str] = field(default_factory=set)
    duplicates: list[str] = field(default_factory=list)

    def add(self, kind: str, number: str) -> None:
        values: set[str] = getattr(self, kind)
        if number in values:
            self.duplicates.append(f"duplicate {kind[:-1]} {number}")
        values.add(number)


def chapter_number(path: Path) -> int:
    match = CHAPTER_FILE_RE.search(path.name)
    if not match:
        raise ValueError(f"cannot determine chapter number from {path}")
    return int(match.group(1))


def source_lines(text: str) -> list[str]:
    """Expand our own figure directives back to their logical source lines.

    This makes the transformation idempotent and lets the same code validate
    already-linked files.
    """
    lines = text.splitlines()
    output: list[str] = []
    index = 0
    while index < len(lines):
        equation_label = re.fullmatch(r"\(eq-([^)]+)\)=", lines[index])
        if equation_label and index + 1 < len(lines) and lines[index + 1].lstrip().startswith("$$"):
            number = equation_label.group(1)
            index += 1
            while index < len(lines):
                value = lines[index]
                if value.rstrip().endswith("$$"):
                    value = value.replace("\\end{equation*}", f"\\tag{{{number}}}\\end{{equation*}}")
                    output.append(value)
                    index += 1
                    break
                output.append(value)
                index += 1
            continue
        math_directive = re.match(r"^:::\{math\}\s*$", lines[index])
        if math_directive and index + 1 < len(lines) and lines[index + 1].startswith(":label: eq-"):
            number = lines[index + 1].removeprefix(":label: eq-")
            output.append("$$\\begin{equation*}")
            index += 2
            while index < len(lines) and lines[index] != ":::":
                output.append(lines[index])
                index += 1
            output.append(f"\\tag{{{number}}}\\end{{equation*}}$$")
            index += 1
            continue
        match = re.match(r"^:::\{figure\}\s+(.+)$", lines[index])
        if not match:
            # A caption whose image was separated by a PDF page break may have
            # been linked as prose by an older run.  Normalize it so the global
            # image/caption pairing pass below can recover it mechanically.
            linked_caption = LINKED_FIGURE_CAPTION_RE.match(lines[index])
            if linked_caption:
                output.append(f"Figure {linked_caption.group(1)}: {linked_caption.group(2)}")
            else:
                output.append(lines[index])
            index += 1
            continue
        target = match.group(1)
        index += 1
        label = ""
        caption: list[str] = []
        while index < len(lines) and lines[index] != ":::":
            if lines[index].startswith(":label:"):
                label = lines[index].split(None, 1)[1]
            elif lines[index] or caption:
                caption.append(lines[index])
            index += 1
        if index == len(lines):
            raise ValueError("unterminated figure directive")
        number_match = re.fullmatch(r"fig-(.+)", label)
        if not number_match:
            raise ValueError(f"generated figure has invalid label {label!r}")
        output.extend([f"![image]({target})", "", f"Figure {number_match.group(1)}: {' '.join(caption).strip()}"])
        index += 1
    return output


def inventory(files: list[Path]) -> Inventory:
    found = Inventory()
    for path in files:
        lines = source_lines(path.read_text(encoding="utf-8"))
        for line in lines:
            if match := re.fullmatch(r"\(eq-([^)]+)\)=", line):
                found.add("equations", match.group(1))
            if match := HEADING_RE.match(line):
                found.add("sections", match.group(2))
            if match := FIGURE_CAPTION_RE.match(line):
                found.add("figures", match.group(1))
            if match := TABLE_CAPTION_RE.match(line):
                found.add("tables", match.group(1))
            for match in TAG_RE.finditer(line):
                found.add("equations", match.group(1))
    return found


def cross_reference_prose(line: str, chapter: int, targets: Inventory) -> str:
    """Link references in a prose line, leaving roles and inline math alone."""
    if not line or line.startswith(("#", ":::", ":", "!", "|")) or re.fullmatch(r"\([^)]+\)=", line):
        return line

    # Split on existing MyST roles and inline/display math.  Only prose chunks
    # are rewritten, preventing accidental edits inside formulas or prior refs.
    chunks = re.split(r"(`[^`]*`|\$\$.*?\$\$|\$[^$]*\$)", line)
    for index in range(0, len(chunks), 2):
        text = chunks[index]

        def figure(match: re.Match[str]) -> str:
            prefix, number = match.groups()
            if number not in targets.figures:
                return match.group(0)
            display = "Fig. %s" if prefix.lower().startswith("fig.") else "Figure %s"
            return f"{{numref}}`{display} <fig-{number}>`"

        text = re.sub(rf"\b(Fig\.|Figure)\s+({NUMBER})\b", figure, text, flags=re.IGNORECASE)

        def equation(match: re.Match[str]) -> str:
            prefix, number = match.groups()
            if number not in targets.equations:
                return match.group(0)
            display = "Eq. %s" if prefix.lower().startswith("eq.") else "Equation %s"
            return f"{{numref}}`{display} <eq-{number}>`"

        text = re.sub(rf"\b(Eq\.|Equation)\s*\(?({NUMBER})\)?", equation, text, flags=re.IGNORECASE)

        # The source often uses just "(5.1)" after words such as definition,
        # result, formula, or theorem.  A parenthesized number is safe to link
        # when (and only when) it exactly matches an inventoried equation.
        def bare_equation(match: re.Match[str]) -> str:
            number = match.group(1)
            return f"{{eq}}`eq-{number}`" if number in targets.equations else match.group(0)

        text = re.sub(rf"\(({NUMBER})\)", bare_equation, text)

        def table(match: re.Match[str]) -> str:
            number = match.group(1)
            return f"{{numref}}`Table %s <tbl-{number}>`" if number in targets.tables else match.group(0)

        text = re.sub(rf"\bTable\s+({NUMBER})\b", table, text, flags=re.IGNORECASE)

        def section(match: re.Match[str]) -> str:
            prefix, raw_number = match.groups()
            number = raw_number if "." in raw_number else f"{chapter}.{raw_number}"
            if number not in targets.sections:
                return match.group(0)
            return f"{{ref}}`{prefix} {number} <sec-{number}>`"

        text = re.sub(rf"\b(Section|section)\s+([1-9]\d*(?:\.\d+)*)\b", section, text)

        def chapter_ref(match: re.Match[str]) -> str:
            prefix, number = match.groups()
            path_exists = any(CHAPTERS.glob(f"ch-{int(number):02d}-*.md"))
            return f"{{ref}}`{prefix} {number} <ch-{number}>`" if path_exists else match.group(0)

        text = re.sub(r"\b(Chapter|chapter)\s+([1-9]\d*)\b", chapter_ref, text)
        chunks[index] = text
    return "".join(chunks)


def transform(path: Path, targets: Inventory) -> str:
    lines = source_lines(path.read_text(encoding="utf-8"))
    chapter = chapter_number(path)
    # Pair captions with the nearest preceding unpaired image.  Usually they
    # are adjacent, but PDF page breaks put seven captions after intervening
    # prose.  Pairing first avoids treating those captions as ordinary prose.
    image_stack: list[int] = []
    pending_captions: list[tuple[int, tuple[str, str]]] = []
    figure_at_image: dict[int, tuple[str, str]] = {}
    paired_captions: set[int] = set()
    for position, candidate in enumerate(lines):
        if IMAGE_RE.match(candidate):
            if pending_captions:
                caption_position, groups = pending_captions.pop(0)
                figure_at_image[position] = groups
                paired_captions.add(caption_position)
            else:
                image_stack.append(position)
        elif caption := FIGURE_CAPTION_RE.match(candidate):
            if image_stack:
                image_position = image_stack.pop()
                figure_at_image[image_position] = caption.groups()
                paired_captions.add(position)
            else:
                # One source caption (Figure 12.1) precedes its image because
                # of PDF extraction order.  It is paired with the next image.
                pending_captions.append((position, caption.groups()))
    output: list[str] = []
    index = 0
    in_frontmatter = False
    while index < len(lines):
        line = lines[index]

        if index in paired_captions:
            index += 1
            continue

        if index == 0 and line == "---":
            in_frontmatter = True
            output.append(line)
            index += 1
            continue
        if in_frontmatter:
            output.append(line)
            if line == "---":
                in_frontmatter = False
            index += 1
            continue

        if match := HEADING_RE.match(line):
            level, number, title = match.groups()
            if output and output[-1] == f"(sec-{number})=":
                output.pop()
            output.extend([f"(sec-{number})=", f"{level} {number} {title}"])
            index += 1
            continue

        if match := GENERIC_HEADING_RE.match(line):
            level, title, old_label = match.groups()
            label = f"ch-{chapter}-{old_label}"
            if output and output[-1] == f"({label})=":
                output.pop()
            output.extend([f"({label})=", f"{level} {title}"])
            index += 1
            continue

        # An image plus its following numbered caption becomes a semantic MyST
        # figure.  Intervening blank lines are allowed, but no other content is.
        if match := IMAGE_RE.match(line):
            if index in figure_at_image:
                number, caption_text = figure_at_image[index]
                output.extend([
                    f":::{{figure}} {match.group(2)}",
                    f":label: fig-{number}",
                    cross_reference_prose(caption_text, chapter, targets),
                    ":::",
                    "",
                ])
                index += 1
                continue

        # Label display-math blocks and remove printed tags.  Keeping the label
        # outside the TeX makes it usable by HTML, PDF, and Jupyter Book builds.
        if line.lstrip().startswith("$$"):
            block_end = index
            # A closing delimiter can occur on the opening line or, as in the
            # extraction, after \end{equation*} several lines later.
            while block_end < len(lines) and not (
                lines[block_end].rstrip().endswith("$$")
                and (block_end > index or lines[block_end].count("$$") >= 2)
            ):
                block_end += 1
            if block_end < len(lines):
                block = lines[index : block_end + 1]
                tags = TAG_RE.findall("\n".join(block))
                if len(tags) > 1:
                    body = "\n".join(block)
                    body = re.sub(r"^\s*\$\$", "", body)
                    body = re.sub(r"\$\$\s*$", "", body)
                    body = re.sub(r"\\(?:begin|end)\{(?:align|gather)\*\}", "", body).strip()
                    for value in body.splitlines():
                        tag = TAG_RE.search(value)
                        if not tag:
                            continue
                        formula = TAG_RE.sub("", value).strip().removesuffix(r"\\").strip()
                        equation = [":::{math}", f":label: eq-{tag.group(1)}"]
                        if "&" in formula:
                            equation.append(r"\begin{aligned}")
                        equation.append(formula)
                        if "&" in formula:
                            equation.append(r"\end{aligned}")
                        output.extend(equation + [":::", ""])
                    index = block_end + 1
                    continue
                if len(tags) == 1:
                    number = tags[0]
                    body = "\n".join(block)
                    body = re.sub(r"^\s*\$\$", "", body)
                    body = re.sub(r"\$\$\s*$", "", body)
                    body = TAG_RE.sub("", body)
                    body = body.replace("\\begin{equation*}", "").replace("\\end{equation*}", "").strip()
                    output.extend([":::{math}", f":label: eq-{number}", body, ":::", ""])
                    index = block_end + 1
                    continue

        output.append(cross_reference_prose(line, chapter, targets))
        index += 1

    return re.sub(r"\n{3,}", "\n\n", "\n".join(output)).rstrip() + "\n"


def transform_unnumbered_headings(path: Path, namespace: str) -> str:
    """Hide explicit IDs in book pages that are not numbered chapters."""
    output: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if match := GENERIC_HEADING_RE.match(line):
            level, title, old_label = match.groups()
            label = f"{namespace}-{old_label}"
            if output and output[-1] == f"({label})=":
                output.pop()
            output.extend([f"({label})=", f"{level} {title}"])
        else:
            output.append(line)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(output)).rstrip() + "\n"


def unresolved(files_and_text: list[tuple[Path, str]], targets: Inventory) -> list[str]:
    findings: list[str] = []
    patterns = [
        ("figure", re.compile(rf"\b(?:Fig\.|Figure)\s+({NUMBER})\b", re.I), targets.figures),
        ("equation", re.compile(rf"\b(?:Eq\.|Equation)\s*\(?({NUMBER})\)?", re.I), targets.equations),
        ("table", re.compile(rf"\bTable\s+({NUMBER})\b", re.I), targets.tables),
    ]
    for path, text in files_and_text:
        for line_number, line in enumerate(text.splitlines(), 1):
            # Captions, directives, and already-linked role bodies are targets,
            # not unresolved prose references.
            scrubbed = re.sub(r"\{(?:numref|ref)\}`[^`]+`", "", line)
            if FIGURE_CAPTION_RE.match(scrubbed) or TABLE_CAPTION_RE.match(scrubbed):
                continue
            for kind, pattern, known in patterns:
                for match in pattern.finditer(scrubbed):
                    status = "unlinked" if match.group(1) in known else "missing target"
                    findings.append(f"{path.relative_to(ROOT)}:{line_number}: {status} {kind} {match.group(1)}")
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="report changes without writing files")
    parser.add_argument("--diff", action="store_true", help="print a unified diff")
    args = parser.parse_args()

    files = sorted(CHAPTERS.glob("ch-*.md"))
    targets = inventory(files)
    if targets.duplicates:
        print("Cross-reference target collisions:", file=sys.stderr)
        print("\n".join(f"- {item}" for item in targets.duplicates), file=sys.stderr)
        return 2

    changed: list[Path] = []
    results: list[tuple[Path, str]] = []
    for path in files:
        old = path.read_text(encoding="utf-8")
        new = transform(path, targets)
        results.append((path, new))
        if old != new:
            changed.append(path)
            if args.diff:
                print("".join(difflib.unified_diff(old.splitlines(True), new.splitlines(True), fromfile=str(path), tofile=str(path))))
            if not args.check:
                path.write_text(new, encoding="utf-8")

    preface = ROOT / "preface.md"
    old = preface.read_text(encoding="utf-8")
    new = transform_unnumbered_headings(preface, "preface")
    results.append((preface, new))
    if old != new:
        changed.append(preface)
        if args.diff:
            print("".join(difflib.unified_diff(old.splitlines(True), new.splitlines(True), fromfile=str(preface), tofile=str(preface))))
        if not args.check:
            preface.write_text(new, encoding="utf-8")

    problems = unresolved(results, targets)
    print(
        f"Targets: {len(targets.sections)} sections/subsections, "
        f"{len(targets.figures)} figures, {len(targets.equations)} equations, "
        f"{len(targets.tables)} tables"
    )
    print(f"Files needing updates: {len(changed)}")
    if problems:
        print("Unresolved numbered references:")
        print("\n".join(f"- {item}" for item in problems))
    if args.check and changed:
        return 1
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
