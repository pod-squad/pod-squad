#!/usr/bin/env python3
"""Generate the PUBLIC (sealed) site assets for Pod Squad.

SEALED-REVEAL DESIGN: before reveal, nothing on the public site may show a
real whale's traits or portrait. This script therefore only writes:

  site/metadata/<id>.json   SEALED metadata (gift image, NO attributes)
                             — one file per token id in the assignment,
                             so tokenURI works for every mint from day one.
  site/tokens.js             window.TOKENS = {} — intentionally EMPTY.
                             Real trait data is private until reveal and
                             lives only in ../reveal-pack/ (never publish).

The real metadata generator is ../reveal-pack/gen-real-metadata.py.
The sealed gift artwork is copied into the site by hand (or by the build
step): art/final/sealed-gift.webp -> site/images/sealed-gift.webp.
Style samples in site/images/sample-*.webp come from art/proof/ — they are
NOT tied to token ids and are labelled "sample art" everywhere.
"""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent          # pod-squad/
SITE = ROOT / "site"
ASSIGNMENT = ROOT / "art" / "assignment.json"

DESCRIPTION = ("A sealed Pod Squad gift. One of 7,000 chibi whales on BNB "
               "Smart Chain sleeps inside — every whale is revealed at once "
               "when the 7-day mint window closes. The first mint per "
               "wallet is free.")


def main():
    assignment = json.loads(ASSIGNMENT.read_text())
    (SITE / "metadata").mkdir(parents=True, exist_ok=True)
    n = 0
    for entry in assignment:
        tid = entry["tokenId"]
        meta = {
            "name": f"Pod Squad #{tid}",
            "description": DESCRIPTION,
            "image": "images/sealed-gift.webp",
        }
        (SITE / "metadata" / f"{tid}.json").write_text(
            json.dumps(meta, indent=2, ensure_ascii=False) + "\n")
        n += 1
    js = ("// Sealed until reveal: real trait data is private and never ships\n"
          "// with the public site. Reveal pack lives outside site/.\n"
          "window.TOKENS = {};\n")
    (SITE / "tokens.js").write_text(js)
    print(f"sealed metadata written for {n} tokens; tokens.js emptied (sealed)")


if __name__ == "__main__":
    main()
