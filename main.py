"""The Printer Apology — one-line entry (program/v1, python3.13).

Writes a single original apology note, written by an office printer to the
people who use it, to /output/entry.txt, or to $MAKEFUN_OUTPUT_DIR/entry.txt
when the grader sets that variable. The line is fixed text, so every run
writes identical bytes.
"""

import os
from pathlib import Path

ENTRY = "I'm sorry I only work when IT is watching. The rest of the time I jam, out of professional respect."


def main() -> None:
    # Gate self-check (revision edit): the sealed gate wants 1-120 chars,
    # UTF-8 text, not only whitespace. Fail loudly instead of writing junk.
    assert 1 <= len(ENTRY) <= 120 and ENTRY.strip(), "entry fails the 1-120 char gate"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
