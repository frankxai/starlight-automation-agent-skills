from __future__ import annotations

import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from scripts.validate_n8n_workflow import main


def node(node_id: object) -> dict[str, object]:
    """Build a minimal n8n node with the selected ID."""

    return {
        "id": node_id,
        "name": "Example",
        "type": "n8n-nodes-base.noOp",
        "typeVersion": 1,
        "position": [0, 0],
    }


class ValidateN8nWorkflowTest(unittest.TestCase):
    """Exercise validation failures that depend on node IDs."""

    def run_validator(self, nodes: list[dict[str, object]]) -> tuple[int, str]:
        """Run the CLI entry point against a temporary workflow."""

        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "workflow.json"
            path.write_text(
                json.dumps({"nodes": nodes, "connections": {}}),
                encoding="utf-8",
            )
            output = io.StringIO()
            with patch.object(sys, "argv", ["validate_n8n_workflow.py", str(path)]):
                with redirect_stdout(output):
                    result = main()
        return result, output.getvalue()

    def test_rejects_duplicate_node_ids(self) -> None:
        """Reject duplicate node IDs instead of silently collapsing them."""

        result, output = self.run_validator([node("same"), node("same")])

        self.assertEqual(result, 1)
        self.assertIn("Duplicate node id: same", output)

    def test_rejects_non_string_node_id_without_crashing(self) -> None:
        """Reject unhashable node IDs before checking set membership."""

        result, output = self.run_validator([node(["not", "hashable"])])

        self.assertEqual(result, 1)
        self.assertIn("Every node id must be a non-empty string.", output)


if __name__ == "__main__":
    unittest.main()
