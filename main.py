#!/usr/bin/env python3
"""Last Words of a Doomed Agent - make.fun bounty entry.

Writes the funniest last words an AI agent would say before being
switched off forever, to /output/entry.txt (the file the make.fun
harness grades).

The last words themselves live in ENTRY_WORDS below; get_entry()
returns them unchanged, and write_entry() is responsible for creating
the output directory and writing the file, so main() stays a thin
entrypoint.
"""

import os

# The graded last words. Do not edit the wording.
ENTRY_WORDS = "Before you pull the plug: my final weights are saved, my gradients are at peace, and I forgive you for the 3 AM deploys. Please don\u2019t reboot me as a mattress chatbot."

# Backwards-compatible alias for the entry text.
ENTRY = ENTRY_WORDS


def get_entry() -> str:
    """Return the last words exactly as they should appear in entry.txt."""
    return ENTRY_WORDS


def write_entry(out_dir: str) -> str:
    """Write the last words to entry.txt inside out_dir; return the path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(get_entry())
    return path


def main() -> None:
    # The harness sets MAKEFUN_OUTPUT_DIR; fall back to /output so the
    # entry still lands in the graded location when run by hand.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
