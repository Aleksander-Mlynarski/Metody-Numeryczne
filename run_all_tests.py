"""Uruchamia testy pytest we wszystkich katalogach laboratoriów."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parent
    labs = sorted(root.glob("lab*"))

    if not labs:
        print("Nie znaleziono katalogów laboratoriów.")
        return 1

    failed: list[str] = []
    passed: list[str] = []

    for lab in labs:
        test_file = lab / "test_main.py"
        if not test_file.exists():
            continue

        print(f"\n{'=' * 60}\n{lab.name}\n{'=' * 60}")
        result = subprocess.run(
            [sys.executable, "-m", "pytest", "test_main.py", "-q"],
            cwd=lab,
        )

        if result.returncode == 0:
            passed.append(lab.name)
        else:
            failed.append(lab.name)

    print(f"\n{'=' * 60}")
    print(f"Zaliczone: {len(passed)}/{len(passed) + len(failed)}")
    if failed:
        print("Niezaliczone:")
        for name in failed:
            print(f"  - {name}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
