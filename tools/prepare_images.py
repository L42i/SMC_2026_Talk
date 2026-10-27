#!/usr/bin/env python3
"""Downscale the paper's photos for web/slides use.

Usage:  python3 tools/prepare_images.py <source_pictures_dir> [pictures]

Camera originals (6000 px, 5-10 MB) are far too heavy for a web page that
remote attendees open during the talk. This writes copies capped at
2000 px on the long edge into ./pictures, keeping file names (spaces and
"(1)" suffixes are cleaned up).
"""
import re, sys
from pathlib import Path
from PIL import Image, ImageOps

MAX = 2000
src = Path(sys.argv[1])
dst = Path(sys.argv[2] if len(sys.argv) > 2 else "pictures")
dst.mkdir(exist_ok=True)

for f in sorted(src.iterdir()):
    if f.suffix.lower() not in {".jpg", ".jpeg", ".png"}:
        continue
    name = re.sub(r"\s*\(\d+\)", "", f.stem).replace(" ", "_") + f.suffix.lower()
    im = ImageOps.exif_transpose(Image.open(f))
    im.thumbnail((MAX, MAX), Image.LANCZOS)
    out = dst / name
    if out.suffix in {".jpg", ".jpeg"}:
        im.convert("RGB").save(out, quality=82, optimize=True, progressive=True)
    else:
        im.save(out, optimize=True)
    print(f"{f.name:40s} -> {out}  {im.size[0]}x{im.size[1]}  {out.stat().st_size//1024} kB")
