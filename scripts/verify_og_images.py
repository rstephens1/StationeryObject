#!/usr/bin/env python3
"""Fail build when post pages are missing valid 1200x630 OG/Twitter images."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import urlparse

from PIL import Image


META_RE = re.compile(
    r"<meta\s+(?:property|name)=[\"']?(og:image|twitter:image)[\"']?\s+content=[\"']?([^\"'\s>]+)",
    re.IGNORECASE,
)

HERO_SRC_RE = re.compile(r'(?m)^\s*src\s*=\s*["\']([^"\']+)["\']')


def extract_meta_image_urls(html: str) -> dict[str, str]:
    found: dict[str, str] = {}
    for key, value in META_RE.findall(html):
        found[key.lower()] = value
    return found


def post_has_hero(content_file: Path) -> bool:
    text = content_file.read_text(encoding="utf-8", errors="ignore")
    if "[[images]]" in text and HERO_SRC_RE.search(text):
        return True
    if re.search(r"(?m)^\s*images\s*:", text):
        return True
    return False


def to_public_path(public_dir: Path, url: str) -> Path | None:
    if url.startswith("http://") or url.startswith("https://"):
        path = urlparse(url).path
    else:
        path = url

    if not path:
        return None

    if path.startswith("/"):
        return public_dir / path.lstrip("/")
    return public_dir / path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    public_dir = root / "public"
    post_pages = sorted(public_dir.glob("posts/*/index.html"))
    content_dir = root / "content" / "posts"

    if not post_pages:
        print("No built post pages found under public/posts/*/index.html")
        return 1

    failures: list[str] = []

    for page in post_pages:
        rel = page.relative_to(root)
        slug = page.parent.name
        source = content_dir / slug / "index.md"
        needs_og = source.exists() and post_has_hero(source)

        html = page.read_text(encoding="utf-8", errors="ignore")
        meta = extract_meta_image_urls(html)
        og = meta.get("og:image")
        tw = meta.get("twitter:image")

        if not needs_og:
            continue

        if not og:
            failures.append(f"{rel}: missing og:image")
            continue
        if not tw:
            failures.append(f"{rel}: missing twitter:image")
            continue
        if og != tw:
            failures.append(f"{rel}: og:image and twitter:image differ")
            continue

        image_path = to_public_path(public_dir, og)
        if image_path is None or not image_path.exists():
            failures.append(f"{rel}: image file not found for {og}")
            continue

        try:
            with Image.open(image_path) as im:
                width, height = im.size
        except Exception as exc:
            failures.append(f"{rel}: unable to open image {image_path}: {exc}")
            continue

        if (width, height) != (1200, 630):
            failures.append(
                f"{rel}: image {image_path.relative_to(root)} has {width}x{height}, expected 1200x630"
            )

    if failures:
        print("OG image verification failed:")
        for item in failures:
            print(f"- {item}")
        return 1

    print(f"OG image verification passed for {len(post_pages)} post pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
