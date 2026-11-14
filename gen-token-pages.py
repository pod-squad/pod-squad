#!/usr/bin/env python3
"""Generate static per-token pages: site/token/<id>.html  (SEALED version)

Pre-reveal, every token page shows the sealed gift: OpenGraph / Twitter Card
image = the shared gift image, title "Pod Squad #<id> — Sealed", and no trait
information anywhere. Human visitors are redirected to the single-page app
view (index.html#/token/<id>), which also renders the gift until reveal.

Deploy step: set SITE_BASE below to the live site root (must end with "/")
and re-run, so og:image becomes an absolute URL (X requires absolute URLs).
With SITE_BASE empty the tags stay relative — fine for local preview only.

After reveal, this generator is replaced by the reveal-pack one.
"""
import json, pathlib

SITE_BASE = "https://pod-squad.github.io/pod-squad/"

ROOT = pathlib.Path(__file__).resolve().parent.parent          # pod-squad/
SITE = ROOT / "site"
ASSIGNMENT = ROOT / "art" / "assignment.json"

DESC = ("A sealed Pod Squad gift on BSC. A chibi whale sleeps inside — "
        "all 7,000 reveal at once when the mint window closes. "
        "First mint per wallet is free.")

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Pod Squad #{tid} — Sealed</title>
<meta name="description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:title" content="Pod Squad #{tid} — Sealed">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{base}images/sealed-gift.webp">
<meta property="og:url" content="{base}token/{tid}.html">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Pod Squad #{tid} — Sealed">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{base}images/sealed-gift.webp">
<script>location.replace("../index.html#/token/{tid}");</script>
</head>
<body>
<p>Pod Squad #{tid} — sealed gift. {desc}</p>
<p><a href="../index.html#/token/{tid}">View this sealed gift</a></p>
<img src="../images/sealed-gift.webp" alt="Pod Squad #{tid} — Sealed" width="512">
</body>
</html>
"""


def main():
    assignment = json.loads(ASSIGNMENT.read_text())
    out = SITE / "token"
    out.mkdir(parents=True, exist_ok=True)
    n = 0
    for entry in assignment:
        tid = entry["tokenId"]
        (out / f"{tid}.html").write_text(
            PAGE.format(tid=tid, desc=DESC, base=SITE_BASE), encoding="utf-8")
        n += 1
    print(f"sealed token pages generated: {n}")


if __name__ == "__main__":
    main()
