#!/usr/bin/env python3
"""Redact common secret-shaped strings from text."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REPLACEMENTS = [
    (re.compile(r"(?i)(api[_-]?key|secret|token|password)(\s*[:=]\s*)['\"]?[^\s'\"]+"), r"\1\2<redacted>"),
    (re.compile(r"(?i)bearer\s+[a-z0-9._\-]+"), "Bearer <redacted>"),
    (re.compile(r"https://[^\s)\]\"]*(webhook|hook)[^\s)\]\"]*", re.IGNORECASE), "https://example.com/webhook"),
]


def redact(text: str) -> str:
    for pattern, replacement in REPLACEMENTS:
        text = pattern.sub(replacement, text)
    return text


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        sample = "API_KEY=abc123456789 bearer abcdefghijklmnop https://example.test/webhook/secret"
        print(redact(sample))
        return 0
    if not args.path:
        print("Provide a file path or --self-test.")
        return 1
    path = Path(args.path)
    print(redact(path.read_text(encoding="utf-8")))
    return 0


if __name__ == "__main__":
    sys.exit(main())

