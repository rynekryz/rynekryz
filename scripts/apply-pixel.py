#!/usr/bin/env python3
"""Re-insert the custom pixel blocks after Expressive Profile rewrites README.md."""

import re
import sys
from pathlib import Path

MARK = re.compile(r"<!-- pixel:[a-z]+ -->.*?<!-- /pixel:[a-z]+ -->\n?", re.S)
OLD_HEADER = re.compile(r'<img src="static/Code\.svg" width="320"\s*/?>')
PROJECT = re.compile(
    r'<a href="https://github\.com/rynekryz/[^"]+"><picture>.*?</picture></a>',
    re.S,
)

HEADER = (
    "<!-- pixel:header -->\n"
    '<picture><source media="(prefers-color-scheme: dark)" srcset="pixel-art/sky-banner-dark.svg">'
    '<img src="pixel-art/sky-banner-light.svg" width="100%" alt="night sky"></picture>\n'
    "<!-- /pixel:header -->"
)

CODE_CARD = (
    '<picture><source media="(prefers-color-scheme: dark)" srcset="static/code-card-dark.svg">'
    '<img src="static/code-card-light.svg" width="49%" alt="hello world, I\'m Ryne, here\'s some of my projects"></picture>'
)

HEART = [
    ".XX.XX.",
    "XXXXXXX",
    "XXXXXXX",
    ".XXXXX.",
    "..XXX..",
    "...X...",
]


def divider(name):
    return (
        f"<!-- pixel:{name} -->\n"
        f'<picture><source media="(prefers-color-scheme: dark)" srcset="pixel-art/divider-{name}-dark.svg">'
        f'<img src="pixel-art/divider-{name}-light.svg" width="100%" alt=""></picture>\n'
        f"<!-- /pixel:{name} -->"
    )


def sticker(name, alt):
    return (
        f'<picture><source media="(prefers-color-scheme: dark)" srcset="pixel-art/sticker-{name}-dark.svg">'
        f'<img src="pixel-art/sticker-{name}-light.svg" width="60" alt="{alt}"></picture>'
    )


STICKERS = (
    "<!-- pixel:stickers -->\n"
    + " ".join(
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
    + "\n<!-- /pixel:stickers -->"
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


def repack_projects(text):
    code_pos = text.find(CODE_CARD)
    all_blocks = [b.strip() for b in PROJECT.findall(text) if "assets/project-" in b]
    if not all_blocks:
        return text
    blocks = [b for b in all_blocks if "assets/project-dormguard-" not in b]
    if not blocks:
        return text
    cards = [CODE_CARD] + blocks
    rows = ["&nbsp;".join(cards[i : i + 2]) for i in range(0, len(cards), 2)]
    start = code_pos if code_pos != -1 else text.find(all_blocks[0])
    end = text.find(all_blocks[-1], start) + len(all_blocks[-1])
    return text[:start] + "\n\n".join(rows) + text[end:]


def patch_about(path):
    if not path.exists():
        return
    text = path.read_text()
    match = re.search(
        r'(<g class="up"[^>]*>)((?:(?!</g>).)*?)(<text[^>]*>Privacy first[^<]*</text>)',
        text,
        re.S,
    )
    if not match or "pixel-heart" in match.group(2):
        return
    inner = match.group(2)
    circle = re.search(r'<circle\s+cx="([\d.]+)"\s+cy="([\d.]+)"', inner)
    if not circle:
        return
    cx, cy = float(circle.group(1)), float(circle.group(2))
    fill_match = re.search(r'<path\b[^>]*?fill="([^"]+)"', inner)
    fill = fill_match.group(1) if fill_match else "#1b1b1b"
    inner = re.sub(r"<path\b[^>]*?/?>(?:</path>)?", "", inner, count=1, flags=re.S)
    cell = 3
    ox = cx - 3.5 * cell + 0.5
    oy = cy - 3 * cell
    rects = "".join(
        f'<rect x="{ox + x * cell:.1f}" y="{oy + y * cell:.1f}" width="{cell}" height="{cell}"/>'
        for y, row in enumerate(HEART)
        for x, ch in enumerate(row)
        if ch == "X"
    )
    heart = f'<g class="pixel-heart" fill="{fill}" shape-rendering="crispEdges">{rects}</g>'
    text = text[: match.start(2)] + inner + heart + text[match.end(2) :]
    path.write_text(text)


def main():
    path = Path(sys.argv[1] if len(sys.argv) > 1 else "README.md")
    text = path.read_text()
    text = MARK.sub("", text)
    text = OLD_HEADER.sub("", text)
    text = repack_projects(text)

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

    for scheme in ("light", "dark"):
        patch_about(Path(f"assets/about-{scheme}.svg"))


if __name__ == "__main__":
    main()
