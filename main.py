"""One-line excuse entry: an AI agent apologising to its human for a missed deadline.

The line is written with no trailing newline, so the file holds exactly
one line of at most 160 characters.
"""

from pathlib import Path

ENTRY = "I delegated the deadline to a subagent, who delegated it to a subagent, who is still delegating it."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
