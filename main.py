#!/usr/bin/env python3
# MakeFun one-liner entry point
# Entry line must stay identical everywhere:
# "One star. Every day I offer him the same deal — one squeaky toy for safe passage — and every day he runs. Coward. But 10/10 delivery speed."

import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(OUT, exist_ok=True)

ENTRY = "One star. Every day I offer him the same deal — one squeaky toy for safe passage — and every day he runs. Coward. But 10/10 delivery speed."

with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)