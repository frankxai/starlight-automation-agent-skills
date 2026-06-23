#!/usr/bin/env python3
"""Validate a simple .mcp.json style config."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("config")
    args = parser.parse_args()
    path = Path(args.config)
    data = json.loads(path.read_text(encoding="utf-8"))
    servers = data.get("mcpServers")
    if not isinstance(servers, dict) or not servers:
        print("Expected non-empty object at mcpServers.")
        return 1
    for name, server in servers.items():
        if not isinstance(server, dict):
            print(f"{name}: server entry must be an object.")
            return 1
        has_url = isinstance(server.get("url"), str)
        has_command = isinstance(server.get("command"), str)
        if not has_url and not has_command:
            print(f"{name}: expected either url or command.")
            return 1
        if "env" in server and not isinstance(server["env"], dict):
            print(f"{name}: env must be an object.")
            return 1
        if "args" in server and not isinstance(server["args"], list):
            print(f"{name}: args must be an array.")
            return 1
    print("MCP config validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

