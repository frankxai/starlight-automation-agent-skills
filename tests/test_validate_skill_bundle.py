from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.validate_skill_bundle import validate_skill

class ValidateSkillBundleTest(unittest.TestCase):
    def test_missing_skill_md(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir)
            errors = validate_skill(path)
            self.assertEqual(len(errors), 1)
            self.assertTrue(errors[0].endswith("missing SKILL.md"))

    def test_missing_frontmatter(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir)
            skill_file = path / "SKILL.md"
            skill_file.write_text("Hello World", encoding="utf-8")
            errors = validate_skill(path)
            self.assertEqual(len(errors), 1)
            self.assertTrue(errors[0].endswith("missing valid frontmatter"))

    def test_valid_skill(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir)
            path = path / "my-skill"
            path.mkdir()
            skill_file = path / "SKILL.md"
            content = "---\nname: my-skill\ndescription: " + "a" * 60 + "\n---\n"
            skill_file.write_text(content, encoding="utf-8")
            errors = validate_skill(path)
            self.assertEqual(len(errors), 0)

    def test_frontmatter_name_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "my-skill"
            path.mkdir()
            skill_file = path / "SKILL.md"
            content = "---\nname: other-skill\ndescription: " + "a" * 60 + "\n---\n"
            skill_file.write_text(content, encoding="utf-8")
            errors = validate_skill(path)
            self.assertEqual(len(errors), 1)
            self.assertTrue(errors[0].endswith("frontmatter name does not match folder"))

    def test_description_too_short(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "my-skill"
            path.mkdir()
            skill_file = path / "SKILL.md"
            content = "---\nname: my-skill\ndescription: short\n---\n"
            skill_file.write_text(content, encoding="utf-8")
            errors = validate_skill(path)
            self.assertEqual(len(errors), 1)
            self.assertTrue(errors[0].endswith("description is too short for reliable triggering"))

    def test_contains_todo(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "my-skill"
            path.mkdir()
            skill_file = path / "SKILL.md"
            content = "---\nname: my-skill\ndescription: " + "a" * 60 + "\n---\nTODO: do something"
            skill_file.write_text(content, encoding="utf-8")
            errors = validate_skill(path)
            self.assertEqual(len(errors), 1)
            self.assertTrue(errors[0].endswith("contains TODO placeholder"))

    def test_contains_local_windows_path(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "my-skill"
            path.mkdir()
            skill_file = path / "SKILL.md"
            content = "---\nname: my-skill\ndescription: " + "a" * 60 + "\n---\n" + "C:" + "\\Users\\john"
            skill_file.write_text(content, encoding="utf-8")
            errors = validate_skill(path)
            self.assertEqual(len(errors), 1)
            self.assertTrue(errors[0].endswith("contains local machine path"))

    def test_contains_local_unix_path(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "my-skill"
            path.mkdir()
            skill_file = path / "SKILL.md"
            content = "---\nname: my-skill\ndescription: " + "a" * 60 + "\n---\n" + "/" + "Users/john"
            skill_file.write_text(content, encoding="utf-8")
            errors = validate_skill(path)
            self.assertEqual(len(errors), 1)
            self.assertTrue(errors[0].endswith("contains local machine path"))

if __name__ == "__main__":
    unittest.main()
