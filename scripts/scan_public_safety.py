#!/usr/bin/env python3
"""Scan a public bundle for obvious sensitive markers."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


PATTERNS = {
    "local_windows_path": re.compile(r"[A-Za-z]:\\\\Users\\\\", re.IGNORECASE),
    "local_unix_path": re.compile(r"/Users/[^\\s]+|/home/[^\\s]+"),
    "api_key_label": re.compile(r"(?i)(api[_-]?key|secret|token|password)\\s*[:=]\\s*['\\\"]?[^\\s'\\\"]{8,}"),
    "bearer_token": re.compile(r"(?i)bearer\\s+[a-z0-9._\\-]{16,}"),
    "private_webhook": re.compile(r"https://[^\\s)\\]\"]*(webhook|hook)[^\\s)\\]\"]*", re.IGNORECASE),
}

TEXT_EXTENSIONS = {
    ".md",
    ".txt",
    ".json",
    ".yaml",
    ".yml",
    ".py",
    ".ps1",
    ".js",
    ".ts",
    ".html",
    ".css",
}


def iter_files(root: Path):
    for path in root.rglob("*"):
        if path.is_dir():
            continue
        if path.name == "scan_public_safety.py":
            continue
        if any(part in {".git", "node_modules", ".venv", "__pycache__"} for part in path.parts):
            continue
        if path.suffix.lower() in TEXT_EXTENSIONS:
            yield path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.path).resolve()
    findings: list[str] = []

    for path in iter_files(root):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            text = path.read_text(encoding="utf-8", errors="ignore")
        for name, pattern in PATTERNS.items():
            for match in pattern.finditer(text):
                rel = path.relative_to(root)
                line = text.count("\n", 0, match.start()) + 1
                findings.append(f"{rel}:{line}: {name}")

    if findings:
        print("Sensitive markers found:")
        for finding in findings:
            print(f"- {finding}")
        return 1

    print("No obvious sensitive markers found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
