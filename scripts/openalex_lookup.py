#!/usr/bin/env python3
"""Look up a professor in OpenAlex and list works from the last N years.

Needs internet access to api.openalex.org (some sandboxes block it; if so use WebSearch/WebFetch instead).
Standard library only.

Usage:
  python3 openalex_lookup.py "Full Name" --inst "University of Saskatchewan" --years 3
  python3 openalex_lookup.py --author-id A5023888391 --years 3
Optional: set OPENALEX_API_KEY in the environment (a free key raises the daily budget).
Always open each DOI before listing a paper in a dossier. Common names collide.
"""
import argparse
import datetime
import json
import os
import urllib.parse
import urllib.request

BASE = "https://api.openalex.org"


def get(path, params):
    key = os.environ.get("OPENALEX_API_KEY")
    if key:
        params = dict(params, api_key=key)
    url = f"{BASE}{path}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": "ag-professor-finder"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def abstract(inv):
    if not inv:
        return ""
    pos = {}
    for word, idxs in inv.items():
        for i in idxs:
            pos[i] = word
    return " ".join(pos[i] for i in sorted(pos))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("name", nargs="?")
    ap.add_argument("--inst", default="")
    ap.add_argument("--author-id")
    ap.add_argument("--years", type=int, default=3)
    ap.add_argument("--max", type=int, default=40)
    a = ap.parse_args()

    author_id = a.author_id
    if not author_id:
        if not a.name:
            ap.error("give a name or --author-id")
        res = get("/authors", {"search": a.name, "per-page": 8,
                               "select": "id,display_name,last_known_institutions,works_count,orcid"})
        print("Author candidates (pick by institution/ORCID):")
        for i, r in enumerate(res.get("results", [])):
            inst = ", ".join(x.get("display_name", "") for x in (r.get("last_known_institutions") or []))
            print(f" [{i}] {r['id'].split('/')[-1]}  {r['display_name']}  | {inst}  | works={r.get('works_count')}  | {r.get('orcid')}")
        pick = None
        for r in res.get("results", []):
            inst = " ".join(x.get("display_name", "") for x in (r.get("last_known_institutions") or []))
            if a.inst and a.inst.lower() in inst.lower():
                pick = r
                break
        if not pick:
            print("\nNo institution match. Re-run with --author-id <ID> after choosing.")
            return
        author_id = pick["id"].split("/")[-1]
        print(f"\nUsing {author_id} ({pick['display_name']})\n")

    start = datetime.date.today().year - a.years
    works = get("/works", {
        "filter": f"authorships.author.id:{author_id},publication_year:{start}-{datetime.date.today().year}",
        "sort": "publication_date:desc",
        "per-page": min(a.max, 100),
        "select": "title,publication_year,doi,primary_location,abstract_inverted_index,authorships",
    })
    for w in works.get("results", []):
        src = ((w.get("primary_location") or {}).get("source") or {}).get("display_name", "")
        print(f"{w['publication_year']}  {w['title']}")
        print(f"      {src} | {w.get('doi')}")
        ab = abstract(w.get("abstract_inverted_index"))
        if ab:
            print(f"      {ab[:300]}...")
        print()


if __name__ == "__main__":
    main()
