#!/usr/bin/env python3
"""Retrieve public reading evidence without mistaking a failed download for a source.

Writes only to the chosen local evidence directory. Never commits downloaded
material, sends credentials to publishers, or claims that retrieval is reading.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
from pathlib import Path

OUTPUT = Path(sys.argv[1] if len(sys.argv) > 1 else "reading-evidence")
OUTPUT.mkdir(parents=True, exist_ok=True)
MAX_BYTES = 100 * 1024 * 1024

SOURCES = {
    "Gauss-1857-Theoria-motus-Davis.txt": "https://archive.org/download/theoryofmotionof00gausuoft/theoryofmotionof00gausuoft_djvu.txt",
    "Gauss-1857-Theoria-motus-Davis.pdf": "https://www.karlin.mff.cuni.cz/~tuma/Aplikace21/theoryofmotionof00gausuoft.pdf",
    "Gauss-1809-Theoria-motus-original.pdf": "https://www.e-rara.ch/zut/download/pdf/142787",
    "Quigg-2019-Noether-v2.pdf": "https://arxiv.org/pdf/1902.01989v2",
    "Riemann-1857-Abel-Wilkins.pdf": "https://www.emis.de/classics/Riemann/AbelFn.pdf",
    "newton-manifest.json": "https://cudl.lib.cam.ac.uk/iiif/MS-ADD-03970",
    "lab-notebooks.html": "https://press.asimov.com/articles/lab-notebooks",
}


def retrieve(item: tuple[str, str]) -> dict:
    name, url = item
    entry = {"file": name, "requested_url": url}
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "noether-gauss-public-source-audit/1.0"})
        with urllib.request.urlopen(request, timeout=60) as response:
            data = response.read(MAX_BYTES + 1)
            entry.update(final_url=response.url, content_type=response.headers.get("Content-Type"))
        if len(data) > MAX_BYTES:
            raise ValueError("Response exceeded 100 MiB limit")
        if name.endswith(".pdf") and not data.startswith(b"%PDF-"):
            raise ValueError("Response is not a PDF")
        if name.endswith(".json"):
            json.loads(data)
        (OUTPUT / name).write_bytes(data)
        entry.update(status="retrieved-not-yet-read", bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
    except Exception as error:
        entry.update(status="failed", error=f"{type(error).__name__}: {error}")
    return entry


with ThreadPoolExecutor(max_workers=4) as pool:
    receipts = list(pool.map(retrieve, SOURCES.items()))

manifest_path = OUTPUT / "newton-manifest.json"
if manifest_path.exists():
    manifest = json.loads(manifest_path.read_text())
    canvases = [canvas for sequence in manifest.get("sequences", []) for canvas in sequence.get("canvases", [])]
    selected = []
    for canvas in canvases:
        label = str(canvas.get("label", ""))
        if re.search(r"(?<!\d)(?:350|351|352|353)\s*[rv](?![a-z])", label, re.I):
            selected.append(canvas)
    (OUTPUT / "newton-selected-canvases.json").write_text(json.dumps(selected, ensure_ascii=False, indent=2))
    for number, canvas in enumerate(selected[:12]):
        images = canvas.get("images", [])
        if images:
            resource = images[0].get("resource", {})
            image_url = resource.get("@id")
            if isinstance(image_url, str) and image_url.startswith("https://"):
                name = f"newton-{number:02d}-" + re.sub(r"[^A-Za-z0-9_-]", "_", str(canvas.get("label"))) + ".jpg"
                receipts.append(retrieve((name, image_url)))


class Images(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            self.images.append(dict(attrs))


article_path = OUTPUT / "lab-notebooks.html"
if article_path.exists():
    parser = Images()
    parser.feed(article_path.read_text(errors="replace"))
    (OUTPUT / "article-image-links.json").write_text(json.dumps(parser.images, ensure_ascii=False, indent=2))
    for number, image in enumerate(parser.images):
        label = image.get("alt", "")
        url = image.get("src", "")
        if re.search(r"Newton|coloured|contiguous", label, re.I) and url.startswith("https://"):
            receipts.append(retrieve((f"newton-reproduction-{number:02d}.jpg", url)))

(OUTPUT / "retrieval-receipt.json").write_text(json.dumps(receipts, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(receipts, ensure_ascii=False, indent=2))
# A partial archive is valuable, but is explicitly not a successful complete audit.
if not any(entry["status"] == "retrieved-not-yet-read" for entry in receipts):
    sys.exit(1)
