"""Write one fixed one-line joke about working beside AI coding agents.

Deterministic: the same joke is written on every run. Standard library
only, no network.
"""

from pathlib import Path

JOKE = "My agent fixed the bug behind a feature flag that defaults to the bug."
# Hard-coded on purpose: the brief asks for one fixed joke, the same every run.


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
