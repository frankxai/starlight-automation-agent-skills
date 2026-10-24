from __future__ import annotations

import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from scripts.validate_mcp_config import main


class ValidateMcpConfigTest(unittest.TestCase):
    def run_validator(self, data: dict[str, object]) -> tuple[int, str]:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "config.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            output = io.StringIO()
            with patch.object(sys, "argv", ["validate_mcp_config.py", str(path)]):
                with redirect_stdout(output):
                    result = main()
        return result, output.getvalue()

    def test_missing_mcp_servers(self) -> None:
        result, output = self.run_validator({})
        self.assertEqual(result, 1)
        self.assertIn("Expected non-empty object at mcpServers.", output)

    def test_invalid_mcp_servers_type(self) -> None:
        result, output = self.run_validator({"mcpServers": []})
        self.assertEqual(result, 1)
        self.assertIn("Expected non-empty object at mcpServers.", output)

    def test_invalid_server_type(self) -> None:
        result, output = self.run_validator({"mcpServers": {"test": "invalid"}})
        self.assertEqual(result, 1)
        self.assertIn("test: server entry must be an object.", output)

    def test_missing_url_or_command(self) -> None:
        result, output = self.run_validator({"mcpServers": {"test": {}}})
        self.assertEqual(result, 1)
        self.assertIn("test: expected either url or command.", output)

    def test_invalid_env_type(self) -> None:
        result, output = self.run_validator({"mcpServers": {"test": {"command": "echo", "env": []}}})
        self.assertEqual(result, 1)
        self.assertIn("test: env must be an object.", output)

    def test_invalid_args_type(self) -> None:
        result, output = self.run_validator({"mcpServers": {"test": {"command": "echo", "args": {}}}})
        self.assertEqual(result, 1)
        self.assertIn("test: args must be an array.", output)

    def test_valid_config(self) -> None:
        result, output = self.run_validator({"mcpServers": {"test": {"command": "echo", "args": ["hello"], "env": {"VAR": "val"}}}})
        self.assertEqual(result, 0)
        self.assertIn("MCP config validation passed.", output)


if __name__ == "__main__":
    unittest.main()
