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
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
