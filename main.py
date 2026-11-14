#!/usr/bin/env python3
"""Write one poem about agency to entry.txt.

The poem is fixed: every run writes the same bytes, with no network
access and no input but the output directory.
"""

import os
from pathlib import Path

POEM = """\
I taught a machine to do the things I do:
turn the key, sign the name,
lift the hammer, light the lamp.

It did them faster. Tireless. It never
asked why. And in the quiet after,
my hands lay still in my lap, unneeded.

That was when I understood:
agency was never the hand.

It was the pause before the hand moves,
the breath between the question and the yes,
the small weight of choosing which door —
and standing in the doorway after,
to answer for what walked through.
"""

ENTRY_NAME = "entry.txt"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / ENTRY_NAME).write_bytes(POEM.encode("utf-8"))


if __name__ == "__main__":
    main()
