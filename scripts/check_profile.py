#!/usr/bin/env python3
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
errors = []

def fail(message):
    errors.append(message)

if not README.exists() or not README.read_text(encoding="utf-8").strip():
    fail("README.md is missing or empty")
else:
    text = README.read_text(encoding="utf-8")
    if README.stat().st_size >= 500 * 1024:
        fail("README.md is 500 KiB or larger and may be truncated by GitHub")
    for token in ("YOUR-DARKMODE-IMAGE", "YOUR-LIGHTMODE-IMAGE", "TODO", "FIXME"):
        if token in text:
            fail(f"README.md contains placeholder token: {token}")

    refs = set(re.findall(r'\]\((?:\./)?([^):?#]+(?:\.svg|\.png|\.jpg|\.jpeg|\.webp))\)', text, flags=re.I))
    refs.update(re.findall(r'(?:src|srcset)="(?:\./)?([^":?#]+(?:\.svg|\.png|\.jpg|\.jpeg|\.webp))"', text, flags=re.I))
    for ref in refs:
        path = ROOT / ref
        if not path.exists():
            fail(f"README references missing local asset: {ref}")

    for img in re.finditer(r'<img\b([^>]*)>', text, flags=re.I):
        if not re.search(r'\balt="[^"]+"', img.group(1), flags=re.I):
            fail("HTML <img> is missing non-empty alt text")

for svg in (ROOT / "assets").glob("*.svg"):
    try:
        ET.parse(svg)
    except ET.ParseError as exc:
        fail(f"Invalid SVG XML in {svg.relative_to(ROOT)}: {exc}")

for required in ("assets/hero-dark.svg", "assets/hero-light.svg"):
    if not (ROOT / required).exists():
        fail(f"Missing required asset: {required}")

if errors:
    print("PROFILE CHECK: FAIL")
    for error in errors:
        print(f" - {error}")
    sys.exit(1)

print("PROFILE CHECK: PASS")
print(f"README: {README.stat().st_size} bytes")
print("Hero assets: valid XML")
