#!/usr/bin/env python3
"""로컬 링크 검사: 모든 HTML의 상대 링크·앵커·이미지·CSS 대상이 실제로 있는지 확인한다."""
import pathlib, re, sys
from html.parser import HTMLParser
ROOT = pathlib.Path(__file__).resolve().parent.parent
class P(HTMLParser):
    def __init__(s): super().__init__(); s.refs=[]; s.ids=set()
    def handle_starttag(s, t, a):
        a = dict(a)
        if "id" in a: s.ids.add(a["id"])
        for k in ("href", "src"):
            if k in a: s.refs.append(a[k])
pages = {p: P() for p in ROOT.rglob("*.html")}
for p, h in pages.items(): h.feed(p.read_text(encoding="utf-8"))
bad = 0
for p, h in pages.items():
    for r in h.refs:
        if re.match(r"(https?:|mailto:)", r): continue
        path, _, frag = r.partition("#")
        t = (p.parent / path) if path else p
        if t.is_dir(): t = t / "index.html"
        if not t.exists(): print("깨진 링크", p.relative_to(ROOT), "→", r); bad += 1; continue
        if frag and t.suffix == ".html" and frag not in pages[t].ids: print("없는 앵커", p.relative_to(ROOT), "→", r); bad += 1
print("검사한 페이지", len(pages), "· 문제", bad)
sys.exit(1 if bad else 0)
