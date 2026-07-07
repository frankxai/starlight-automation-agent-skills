#!/usr/bin/env python3
"""Create a dated LinkedIn daily packet skeleton."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower())
    return re.sub(r"-+", "-", slug).strip("-") or "linkedin-daily-packet"


def packet_markdown(brand: str, run_date: str) -> str:
    return f"""# {brand} LinkedIn Daily Packet - {run_date}

## Context

- Audience:
- Current signal:
- Sources:
- Prior learning:

## Candidate 1 - Founder POV

- Hook:
- Alternate hook:
- Full draft:
- Visual concept:
- Carousel or video variant:
- CTA:
- Claim-risk:
- Platform-risk:
- Source links:
- Editing notes:

## Candidate 2 - Tactical Teardown

- Hook:
- Alternate hook:
- Full draft:
- Visual concept:
- Carousel or video variant:
- CTA:
- Claim-risk:
- Platform-risk:
- Source links:
- Editing notes:

## Candidate 3 - Strategic Signal

- Hook:
- Alternate hook:
- Full draft:
- Visual concept:
- Carousel or video variant:
- CTA:
- Claim-risk:
- Platform-risk:
- Source links:
- Editing notes:

## Legal Asset Scout

| Asset | Source URL | License note | Intended use | Risk |
| --- | --- | --- | --- | --- |
| | | | | |

## Tool Routing

- Codex:
- Composio:
- Make.com:
- n8n:
- Scheduler or analytics:

## Approval

- Status: Draft
- Human approver:
- Next action:
"""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", required=True, help="Output directory for packet folders.")
    parser.add_argument("--brand", default="FrankX", help="Brand or creator name.")
    parser.add_argument("--date", default=date.today().isoformat(), help="Packet date, YYYY-MM-DD.")
    parser.add_argument("--slug", default="linkedin-top-voice", help="Topic slug.")
    parser.add_argument("--force", action="store_true", help="Overwrite an existing packet.")
    args = parser.parse_args()

    packet_dir = Path(args.out) / f"{args.date}-{slugify(args.slug)}"
    packet_dir.mkdir(parents=True, exist_ok=True)
    packet_path = packet_dir / "PACKET.md"
    if packet_path.exists() and not args.force:
        raise SystemExit(f"Refusing to overwrite existing packet: {packet_path}")

    packet_path.write_text(packet_markdown(args.brand, args.date), encoding="utf-8")
    print(packet_path)


if __name__ == "__main__":
    main()
