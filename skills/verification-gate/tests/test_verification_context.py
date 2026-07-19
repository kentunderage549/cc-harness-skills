from __future__ import annotations

import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path
from types import ModuleType


SCRIPT_PATH = Path(__file__).parents[1] / "scripts" / "verification_context.py"


def load_module() -> ModuleType:
    spec = importlib.util.spec_from_file_location("verification_context", SCRIPT_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Could not load verification_context.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_git(repo: Path, *args: str) -> None:
    subprocess.run(["git", *args], cwd=repo, check=True, capture_output=True)


class BuildContextTest(unittest.TestCase):
    def test_includes_staged_and_unstaged_changes(self) -> None:
        module = load_module()
        with tempfile.TemporaryDirectory() as temporary_directory:
            repo = Path(temporary_directory)
            run_git(repo, "init", "-q")
            run_git(repo, "config", "user.name", "Test User")
            run_git(repo, "config", "user.email", "test@example.com")

            staged = repo / "staged.txt"
            staged.write_text("initial\n", encoding="utf-8")
            unstaged = repo / "unstaged.txt"
            unstaged.write_text("initial\n", encoding="utf-8")
            run_git(repo, "add", "staged.txt", "unstaged.txt")
            run_git(repo, "commit", "-qm", "Initial commit")

            staged.write_text("staged change\n", encoding="utf-8")
            run_git(repo, "add", "staged.txt")
            unstaged.write_text("unstaged change\n", encoding="utf-8")
            untracked = repo / "untracked.txt"
            untracked.write_text("untracked files are reported by status\n", encoding="utf-8")

            context = module.build_context(repo)

            self.assertEqual(context["changed_files"], ["staged.txt", "unstaged.txt"])
            self.assertIn("staged.txt", context["diff_stat"])
            self.assertIn("unstaged.txt", context["diff_stat"])
            self.assertIn("staged.txt", context["status"])
            self.assertIn("unstaged.txt", context["status"])
            self.assertIn("untracked.txt", context["status"])


if __name__ == "__main__":
    unittest.main()
