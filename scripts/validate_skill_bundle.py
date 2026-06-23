#!/usr/bin/env python3
"""Lightweight validation for a public Codex skill bundle."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


FRONTMATTER = re.compile(r"^---\s*\nname:\s*([a-z0-9-]+)\s*\ndescription:\s*(.+?)\n---", re.S)


def validate_skill(path: Path) -> list[str]:
    errors: list[str] = []
    skill_file = path / "SKILL.md"
    if not skill_file.exists():
        return [f"{path}: missing SKILL.md"]
    text = skill_file.read_text(encoding="utf-8")
    match = FRONTMATTER.search(text)
    if not match:
        errors.append(f"{skill_file}: missing valid frontmatter")
    else:
        if match.group(1) != path.name:
            errors.append(f"{skill_file}: frontmatter name does not match folder")
        if len(match.group(2).strip()) < 60:
            errors.append(f"{skill_file}: description is too short for reliable triggering")
    if "TODO" in text or "[TODO" in text:
        errors.append(f"{skill_file}: contains TODO placeholder")
    local_windows_marker = "C:" + "\\Users\\"
    local_unix_marker = "/" + "Users/"
    if local_windows_marker in text or local_unix_marker in text:
        errors.append(f"{skill_file}: contains local machine path")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.path).resolve()
    skills_root = root / "skills"
    if not skills_root.exists():
        print(f"Missing skills directory: {skills_root}")
        return 1

    errors: list[str] = []
    for skill_dir in sorted(p for p in skills_root.iterdir() if p.is_dir()):
        errors.extend(validate_skill(skill_dir))

    if errors:
        print("Skill validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Skill bundle validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
