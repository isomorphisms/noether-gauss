#!/usr/bin/env python3
"""Retrieve public reading evidence; retrieval is not a claim of reading.

Writes only to a local directory. Records failures and content checksums.
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
        if name.endswith((".jpg", ".png")):
            if data.startswith(b"\x89PNG\r\n\x1a\n"):
                name = str(Path(name).with_suffix(".png"))
                entry["file"] = name
            elif not data.startswith(b"\xff\xd8\xff"):
                raise ValueError("Response is not a JPEG or PNG image")
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
    selected = [canvas for canvas in canvases if re.search(r"(?<!\d)(?:350|351|352|353)\s*[rv](?![a-z])", str(canvas.get("label", "")), re.I)]
    (OUTPUT / "newton-selected-canvases.json").write_text(json.dumps(selected, ensure_ascii=False, indent=2))
    requests = []
    for number, canvas in enumerate(selected[:12]):
        images = canvas.get("images", [])
        if not images:
            continue
        resource = images[0].get("resource", {})
        service = resource.get("service", {})
        base = service.get("@id") if isinstance(service, dict) else None
        if isinstance(base, str) and base.startswith("https://images.lib.cam.ac.uk/iiif/"):
            # The bare IIIF service returns metadata. This requests a rendered page.
            image_url = base.rstrip("/") + "/full/3000,/0/default.jpg"
            label = re.sub(r"[^A-Za-z0-9_-]", "_", str(canvas.get("label")))
            requests.append((f"newton-{number:02d}-{label}.jpg", image_url))
    with ThreadPoolExecutor(max_workers=4) as pool:
        receipts.extend(pool.map(retrieve, requests))


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
        label, url = image.get("alt", ""), image.get("src", "")
        if re.search(r"Newton|coloured|contiguous", label, re.I) and url.startswith("https://"):
            receipts.append(retrieve((f"newton-reproduction-{number:02d}.jpg", url)))

(OUTPUT / "retrieval-receipt.json").write_text(json.dumps(receipts, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(receipts, ensure_ascii=False, indent=2))
if not any(entry["status"] == "retrieved-not-yet-read" for entry in receipts):
    sys.exit(1)
