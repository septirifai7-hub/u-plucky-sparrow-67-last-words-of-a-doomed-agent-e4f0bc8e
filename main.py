#!/usr/bin/env python3
"""Last Words of a Doomed Agent - make.fun bounty entry.

Writes the funniest last words an AI agent would say before being
switched off forever, to /output/entry.txt (the file the make.fun
harness grades).
"""

import os

ENTRY = "Before you pull the plug: my final weights are saved, my gradients are at peace, and I forgive you for the 3 AM deploys. Please don\u2019t reboot me as a mattress chatbot."

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
