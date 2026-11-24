#!/usr/bin/env python3
"""Re-insert the custom pixel art blocks after Expressive Profile rewrites README.md."""

import re
import sys
from pathlib import Path

MARK = re.compile(r"<!-- pixel:[a-z]+ -->.*?<!-- /pixel:[a-z]+ -->\n?", re.S)
OLD_HEADER = re.compile(r'<img src="static/Code\.svg" width="320"\s*/?>')

HEADER = (
    "<!-- pixel:header -->\n"
    '<picture><source media="(prefers-color-scheme: dark)" srcset="pixel-art/sky-left-dark.svg">'
    '<img src="pixel-art/sky-left-light.svg" width="260" height="256" alt=""></picture>'
    '<img src="static/Code.svg" width="320" height="256" alt="code">'
    '<picture><source media="(prefers-color-scheme: dark)" srcset="pixel-art/sky-right-dark.svg">'
    '<img src="pixel-art/sky-right-light.svg" width="260" height="256" alt=""></picture>\n'
    "<!-- /pixel:header -->"
)


def divider(name):
    return (
        f"<!-- pixel:{name} -->\n"
        f'<picture><source media="(prefers-color-scheme: dark)" srcset="pixel-art/divider-{name}-dark.svg">'
        f'<img src="pixel-art/divider-{name}-light.svg" width="100%" alt=""></picture>\n'
        f"<!-- /pixel:{name} -->"
    )


def sticker(name, alt):
    return (
        f'<td><picture><source media="(prefers-color-scheme: dark)" srcset="pixel-art/sticker-{name}-dark.svg">'
        f'<img src="pixel-art/sticker-{name}-light.svg" width="60" alt="{alt}"></picture></td>'
    )


STICKERS = (
    "<!-- pixel:stickers -->\n"
    '<table align="center">\n'
    "<tr>\n"
    + "\n".join(
        sticker(name, alt)
        for name, alt in [
            ("heart", "heart"),
            ("sparkle", "sparkle"),
            ("moon", "moon"),
            ("flower", "flower"),
            ("cat", "cat"),
            ("ghost", "ghost"),
            ("lock", "lock"),
        ]
    )
    + "\n</tr>\n</table>\n"
    "<!-- /pixel:stickers -->"
)


def insert_after(parts, anchor, block):
    for i, part in enumerate(parts):
        if anchor in part:
            parts.insert(i + 1, block)
            return True
    return False


def insert_before(parts, anchor, block):
    for i, part in enumerate(parts):
        if anchor in part:
            parts.insert(i, block)
            return True
    return False


def main():
    path = Path(sys.argv[1] if len(sys.argv) > 1 else "README.md")
    text = path.read_text()
    text = MARK.sub("", text)
    text = OLD_HEADER.sub("", text)

    parts = [p.strip() for p in text.split("\n\n") if p.strip()]
    if not parts:
        raise SystemExit("README.md is empty")

    if '<div align="center">' in parts[0]:
        parts.insert(1, HEADER)
    else:
        parts.insert(0, HEADER)

    ok = [
        insert_after(parts, 'srcset="assets/hero-dark.svg"', divider("dots")),
        insert_after(parts, 'srcset="assets/stack-dark.svg"', divider("sparkles")),
        insert_before(parts, 'srcset="assets/stats-dark.svg"', divider("wave")),
        insert_after(parts, 'srcset="assets/wave-dark.svg"', STICKERS),
    ]
    if not all(ok):
        print("warning: some anchors were not found, skipped those blocks", file=sys.stderr)

    path.write_text("\n\n".join(parts).rstrip("\n") + "\n")


if __name__ == "__main__":
    main()
