"""Stdlib check that the tutorial scripts still parse. No network."""

from __future__ import annotations

import py_compile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ExampleCompileTests(unittest.TestCase):
    def test_example_scripts_compile(self) -> None:
        scripts = sorted(ROOT.glob("*.py"))
        self.assertGreaterEqual(len(scripts), 4, "expected tutorial scripts plus demo_local_gateway.py")
        for path in scripts:
            with self.subTest(script=path.name):
                py_compile.compile(str(path), doraise=True)


if __name__ == "__main__":
    unittest.main()
