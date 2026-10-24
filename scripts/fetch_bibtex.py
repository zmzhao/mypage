#!/usr/bin/env python3
"""Create files/bibtex/<entry>.bib for every file in _publications/.

Entries with a DOI get the publisher's record from Crossref (fallback: doi.org
content negotiation). Entries without a DOI, or whose lookup fails, get a record
generated from the entry's own front matter. Existing .bib files are kept, so
only new publications are fetched; delete a .bib file to refresh it.

Usage: python3 scripts/fetch_bibtex.py [--offline]
"""
import glob
import json
import html
import os
import re
import sys
import time
import unicodedata
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "files", "bibtex")
UA = "zmzhao.github.io BibTeX fetcher (mailto:z.zhao@uva.nl)"
OFFLINE = "--offline" in sys.argv
MARK = "% Generated from site metadata (no publisher record available)"

TYPES = {
    "journals": "article", "editorials": "article", "chinese": "article",
    "conferences": "inproceedings", "chapters": "incollection", "books": "book",
    "theses": "phdthesis", "reports": "techreport", "abstracts": "misc",
}


def front_matter(path):
    text = open(path, encoding="utf-8").read()
    fm = text.split("---", 2)[1]
    data = {}
    for line in fm.splitlines():
        m = re.match(r'^([a-z_]+):\s*(.*)$', line)
        if not m:
            continue
        val = m.group(2).strip()
        if val.startswith('"') and val.endswith('"'):
            try:
                val = json.loads(val)
            except ValueError:
                val = val[1:-1]
        data[m.group(1)] = val
    return data


def ascii_slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]", "", s.lower())


STOP = {"a", "an", "the", "on", "of", "for", "in", "to", "and", "towards", "toward", "with", "using"}


def cite_key(authors, year, title):
    first = re.sub(r"<[^>]+>", "", authors).split(",")[0].strip()
    last = first.split()[-1] if first else ""
    words = [w for w in re.findall(r"[A-Za-z0-9]+", title) if w.lower() not in STOP]
    return f"{ascii_slug(last) or 'anon'}{year}{ascii_slug(words[0]) if words else ''}"


def pretty(bib, key):
    bib = html.unescape(bib.strip())
    bib = re.sub(r"(?<!\\)&", r"\\&", bib)
    bib = re.sub(r"^@(\w+)\{[^,]*,", lambda m: "@%s{%s," % (m.group(1).lower(), key), bib, count=1)
    if "\n" not in bib.strip():
        bib = re.sub(r",\s*(?=[A-Za-z]+\s*=\s*[{\d\"A-Za-z])", ",\n  ", bib, count=0)
        bib = re.sub(r"^(@\w+\{[^,]+,)\s*", r"\1\n  ", bib)
        bib = re.sub(r"\s*\}\s*$", "\n}", bib)
    return bib + "\n"


def fetch(doi):
    urls = [
        ("https://api.crossref.org/works/%s/transform/application/x-bibtex" % urllib.parse.quote(doi, safe=""), None),
        ("https://doi.org/" + doi, "application/x-bibtex; charset=utf-8"),
    ]
    for url, accept in urls:
        for attempt in range(3):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": UA, **({"Accept": accept} if accept else {})})
                with urllib.request.urlopen(req, timeout=30) as r:
                    text = r.read().decode("utf-8", "replace").strip()
                if text.startswith("@"):
                    return text
                break
            except urllib.error.HTTPError as e:
                if e.code == 404:
                    break
                time.sleep(2 + 3 * attempt)
            except Exception:
                time.sleep(2 + 3 * attempt)
    return None


def esc(s):
    return s.replace("&", r"\&").replace("%", r"\%")


def generate(d, key):
    cat = d.get("category", "misc")
    typ = TYPES.get(cat, "misc")
    authors = re.sub(r"<[^>]+>", "", d.get("authors", ""))
    authors = re.sub(r"\s*\(eds?\.\)\s*", "", authors)
    parts = [p.strip() for p in re.split(r"(?<=\.),\s+", authors) if p.strip()]
    fields = [("title", "{%s}" % d.get("title", "")), ("author", " and ".join(parts))]
    venue = d.get("venue_full") or d.get("venue", "")
    venue = re.sub(r"^.*?\(eds?\.\)\s*", "", venue)
    venue = re.split(r"\. pp\. ", venue)[0].strip().rstrip(".")
    if typ == "article":
        fields.append(("journal", venue))
    elif typ in ("inproceedings", "incollection"):
        fields.append(("booktitle", venue))
    elif typ == "book":
        fields.append(("publisher", venue))
    elif typ == "phdthesis":
        fields.append(("school", "University of Amsterdam"))
    elif typ == "techreport":
        fields.append(("institution", venue))
    else:
        fields.append(("howpublished", venue))
    fields.append(("year", d.get("year", "")))
    url = d.get("paperurl", "")
    m = re.search(r"(10\.\d{4,9}/\S+)", url) if "doi" in url else None
    if m:
        fields.append(("doi", m.group(1)))
    if url:
        fields.append(("url", url))
    body = ",\n".join("  %s = {%s}" % (k, esc(v)) for k, v in fields if v)
    return "%s\n@%s{%s,\n%s\n}\n" % (MARK, typ, key, body)


def main():
    os.makedirs(OUT, exist_ok=True)
    made = fetched = 0
    for path in sorted(glob.glob(os.path.join(ROOT, "_publications", "*.md"))):
        name = os.path.splitext(os.path.basename(path))[0]
        target = os.path.join(OUT, name + ".bib")
        d = front_matter(path)
        has_doi = "doi" in d.get("paperurl", "").lower()
        if os.path.exists(target):
            # retry DOI entries that previously fell back to a generated record
            if not (has_doi and open(target, encoding="utf-8").read().startswith(MARK)):
                continue
        key = cite_key(d.get("authors", ""), d.get("year", ""), d.get("title", ""))
        url = d.get("paperurl", "")
        m = re.search(r"(10\.\d{4,9}/[^\s?#\"]+)", url) if "doi" in url.lower() else None
        bib = None
        if m and not OFFLINE:
            raw = fetch(m.group(1).rstrip("."))
            if raw:
                bib = pretty(raw, key)
                fetched += 1
                time.sleep(0.2)
        if bib is None:
            if m and OFFLINE:
                continue  # leave for the online run
            bib = generate(d, key)
        open(target, "w", encoding="utf-8").write(bib)
        made += 1
    print(f"BibTeX: {made} new files ({fetched} from Crossref/DOI)")


if __name__ == "__main__":
    main()
