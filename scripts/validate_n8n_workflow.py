#!/usr/bin/env python3
"""Validate a minimal n8n workflow export for public sharing."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("workflow")
    args = parser.parse_args()
    path = Path(args.workflow)
    data = json.loads(path.read_text(encoding="utf-8"))
    nodes = data.get("nodes")
    if not isinstance(nodes, list) or not nodes:
        print("Expected non-empty nodes array.")
        return 1
    ids = set()
    for node in nodes:
        if not isinstance(node, dict):
            print("Every node must be an object.")
            return 1
        for key in ("id", "name", "type", "typeVersion", "position"):
            if key not in node:
                print(f"Node missing required key: {key}")
                return 1
        node_id = node["id"]
        if not isinstance(node_id, str) or not node_id.strip():
            print("Every node id must be a non-empty string.")
            return 1
        if node_id in ids:
            print(f"Duplicate node id: {node_id}")
            return 1
        ids.add(node_id)
        if "credentials" in node:
            print(f"Node {node.get('name')}: remove credentials before public sharing.")
            return 1
    if not isinstance(data.get("connections", {}), dict):
        print("connections must be an object.")
        return 1
    print(f"n8n workflow validation passed with {len(ids)} node(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
