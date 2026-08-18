#!/usr/bin/env python3
"""Run inexpensive structural checks on the converted MyST book."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEX = ROOT / "latex" / "UniversityPhysicsIClassicalMechanics.tex"


def main() -> int:
    errors: list[str] = []
    chapters = sorted((ROOT / "chapters").glob("ch-*.md"))
    if len(chapters) != 13:
        errors.append(f"expected 13 chapters, found {len(chapters)}")

    tex = TEX.read_text(encoding="utf-8")
    expected_images = len(re.findall(r"\\includegraphics[^\{]*\{[^}]+\}", tex))
    markdown = "\n".join(path.read_text(encoding="utf-8") for path in chapters)
    image_targets = re.findall(r"^!\[[^]]*\]\((.*)\)$", markdown, flags=re.MULTILINE)
    if len(image_targets) != expected_images:
        errors.append(f"expected {expected_images} figure references, found {len(image_targets)}")

    for chapter in chapters:
        content = chapter.read_text(encoding="utf-8")
        if not content.startswith("---\n"):
            errors.append(f"{chapter.name}: missing frontmatter")
        if "image-not-found" in content:
            errors.append(f"{chapter.name}: contains image-not-found")
        if content.count("$") % 2:
            errors.append(f"{chapter.name}: odd number of dollar delimiters")

    for target in image_targets:
        resolved = (ROOT / "chapters" / target).resolve()
        if not resolved.is_file():
            errors.append(f"missing image: {target}")

    if errors:
        print("Verification failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"OK: {len(chapters)} chapters and {len(image_targets)} figure references verified")
    return 0


if __name__ == "__main__":
    sys.exit(main())
