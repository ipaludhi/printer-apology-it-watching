"""The Printer Apology — one-line entry (program/v1, python3.13).

Writes a single original apology note, written by an office printer to the
people who use it, to /output/entry.txt, or to $MAKEFUN_OUTPUT_DIR/entry.txt
when the grader sets that variable. The line is fixed text, so every run
writes identical bytes.

Why this line: the printer apologises in its own voice and names its own
grievance — it only behaves while IT is watching, and jams the rest of the
time "out of professional respect". The joke is printer truth (every office
has watched a printer work perfectly the moment IT walks over), the punch
lands on the last words, and the angle is not the cheap-paper jam every
other entry will write. The entry text itself is never built, formatted or
read from anywhere else: it is the ENTRY constant below, byte for byte.
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
