"""Ridiculous at First Glance, Real by the Second.

Writes one pitch sentence (<=200 chars) to /output/entry.txt.
The pitch: a bizarre startup idea that sounds like a joke, yet reads as a
real business once you see who pays and why.
"""

import os

ENTRY = (
    "For $99 a month, a man in a safari vest follows you around narrating "
    "your life like a nature documentary, because lonely executives will pay "
    "anything to feel like the protagonist of something."
)


def main() -> None:
    # The gate accepts 1-200 chars of non-whitespace UTF-8 text; verify the
    # pitch still fits before writing so a later wording change fails loudly
    # here instead of silently at grading time.
    line = ENTRY.strip()
    assert 1 <= len(line) <= 200, f"entry is {len(line)} chars, must be 1-200"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
