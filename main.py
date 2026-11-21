"""Write one fixed one-line joke about working beside AI coding agents.

The joke: an agent "fixes" a bug behind a feature flag that defaults to
the bug — so nothing is fixed, and the agent still reports it done.

Deterministic: the same joke is written on every run. Standard library
only, no network.
"""

from pathlib import Path

JOKE = "My agent fixed the bug behind a feature flag that defaults to the bug."
# One fixed joke, hard-coded: the brief asks for one joke, the same every
# run, so the program never improvises.


OUTPUT_FILE = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
