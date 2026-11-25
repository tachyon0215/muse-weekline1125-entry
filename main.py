#!/usr/bin/env python3
"""Write the week-in-one-line entry to entry.txt.

Entry for make.fun's "Your Week in One Line": the whole week is one
meeting that refused to end. Monday's throwaway 'quick call' is the
concrete detail; by Friday it has franchised itself into a sequel and
a spin-off, and the cost lands in the last three words, my weekend,
spent in the credits of somebody else's production.

Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = (
    "Monday I said 'quick call'; by Friday it had a sequel, "
    "a spin-off, and my weekend in the credits."
)
TEXT = LINE + "\n"
MAX_CHARS = 100


def verify_written(path: Path) -> None:
    """Read the file back and refuse to leave a wrong line behind."""
    back = path.read_bytes()
    if back != TEXT.encode("utf-8"):
        raise ValueError("written bytes differ from the intended entry")


def main() -> None:
    if not (1 <= len(LINE) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if "\n" in LINE:
        raise ValueError("entry must be a single line")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(TEXT.encode("utf-8"))
    verify_written(target)


if __name__ == "__main__":
    main()
