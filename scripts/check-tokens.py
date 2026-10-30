#!/usr/bin/env python3
"""Check that colors.json and tokens.css hold the same values.

Usage: python3 scripts/check-tokens.py

Exits with status 1 and lists every mismatch if the two files drift apart.
"""
import json
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
data = json.loads((root / "colors.json").read_text())
css = (root / "tokens.css").read_text()

# Read every custom property in tokens.css: name -> value.
props = {
    name: value.strip().strip(";").strip()
    for name, value in re.findall(r"(--hc-[a-z-]+)\s*:\s*([^;]+);", css)
}

expected = {
    "--hc-logo-dark": data["colors"]["logoDark"]["hex"],
    "--hc-accent": data["colors"]["accent"]["hex"],
    "--hc-accent-on-light": data["colors"]["accentOnLight"]["hex"],
    "--hc-ink": data["colors"]["ink"]["hex"],
    "--hc-surface": data["colors"]["surface"]["hex"],
    "--hc-logo-min-width": f'{data["logo"]["minimumWidthPx"]}px',
}


def font_stack(entry):
    family = '"{}"'.format(entry["family"])
    return f'{family}, {entry["fallback"]}'


expected["--hc-font-display"] = font_stack(data["fonts"]["display"])
expected["--hc-font-mono"] = font_stack(data["fonts"]["mono"])

problems = []
for name, want in expected.items():
    got = props.get(name)
    if got is None:
        problems.append(f"{name}: missing from tokens.css")
    elif got.lower() != want.lower():
        problems.append(f"{name}: tokens.css has {got!r}, colors.json has {want!r}")

for name in props:
    if name not in expected:
        problems.append(f"{name}: in tokens.css but not covered by colors.json")

if problems:
    print("\n".join(problems))
    print("token check failed")
    sys.exit(1)

print(f"token check passed ({len(expected)} tokens)")
