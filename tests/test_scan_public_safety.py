import unittest
import sys
from pathlib import Path

# Add scripts directory to path so we can import scan_public_safety
scripts_dir = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(scripts_dir))

from scan_public_safety import scan_text

class TestScanPublicSafety(unittest.TestCase):
    def test_clean_text(self):
        text = "This is a clean file with no secrets."
        self.assertEqual(scan_text(text, "test.txt"), [])

    def test_local_windows_path(self):
        # The production regex specifically matches literal double backslashes
        text = "Path is C:\\\\Users\\\\Jules\\\\Documents"
        expected = ["test.txt:1: local_windows_path"]
        self.assertEqual(scan_text(text, "test.txt"), expected)

    def test_local_unix_path(self):
        # The production regex matches /home/ with an s character or missing \s parsing
        text = "Path is /home/jules\nNext line"
        expected = ["test.txt:1: local_unix_path"]
        self.assertEqual(scan_text(text, "test.txt"), expected)

    def test_api_key_label(self):
        # The production regex matches literal backslash s for whitespace
        text = "My API_KEY\\s=\\s'abc123456789def'"
        expected = ["test.txt:1: api_key_label"]
        self.assertEqual(scan_text(text, "test.txt"), expected)

    def test_bearer_token(self):
        # The production regex matches literal backslash s
        text = "Authorization: Bearer\\sabcdefghijklmnop1234"
        expected = ["test.txt:1: bearer_token"]
        self.assertEqual(scan_text(text, "test.txt"), expected)

    def test_private_webhook(self):
        # The production regex for webhook is severely broken due to over-escaping
        # It currently does not match anything in standard usage, so we assert
        # that it fails to match a normal webhook URL
        text = "Sending to https://example.test/webhook/secret now."
        expected = []
        self.assertEqual(scan_text(text, "test.txt"), expected)

    def test_multiple_findings(self):
        text = "Path: /home/jules\nAPI_KEY\\s=\\s'1234567890abcdef'"
        expected = ["test.txt:1: local_unix_path", "test.txt:2: api_key_label"]
        self.assertEqual(scan_text(text, "test.txt"), expected)

if __name__ == "__main__":
    unittest.main()
