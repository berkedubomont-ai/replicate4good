"""Build the two website versions of the AI Safety Replication Library.

Reads data/studies.json and data/resources.json, adds a few derived fields,
and writes:
  docs/index.html    the general library website
  docs/network.html  the library plus the replication-network prototype
The docs/ folder is what GitHub Pages serves.
Both are single self-contained HTML files with the data embedded.
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# Studies whose languages_tested text mentions other languages without testing them.
NOT_MULTI = {"taken-out-of-context-2023", "scaling-monosemanticity-2024", "error-bars-evals-2024"}
NA_PREFIX = ("not applicable", "synthetic", "not language-specific")


def lang_flag(s):
    lt = (s.get("languages_tested") or "").strip()
    low = lt.lower()
    if low.startswith(NA_PREFIX):
        return "na"
    if s["id"] in NOT_MULTI:
        return "en"
    head = lt.split("(")[0]
    items = [x for x in re.split(r",|;| and ", head) if x.strip()]
    if re.search(r"multilingual|turkish|somali|languages", lt, re.I) and not low.startswith("english only"):
        return "multi"
    return "multi" if len(items) > 1 else "en"


def main(out_dir=None, network_url="network.html"):
    with open(os.path.join(ROOT, "data", "studies.json"), encoding="utf-8") as fh:
        studies = json.load(fh)
    with open(os.path.join(ROOT, "data", "resources.json"), encoding="utf-8") as fh:
        resources = json.load(fh)
    for s in studies:
        s["_lang"] = lang_flag(s)
    payload = json.dumps({"studies": studies, "resources": resources}, ensure_ascii=False, separators=(",", ":"))
    payload = payload.replace("</", "<\\/")
    with open(os.path.join(HERE, "site_template.html"), encoding="utf-8") as fh:
        template = fh.read()
    for flag, name in ((False, "index.html"), (True, "network.html")):
        html = (template.replace("/*__DATA__*/{}", payload)
                .replace("/*__NETWORK__*/false", "true" if flag else "false")
                .replace("/*__NETURL__*/", network_url))
        os.makedirs(out_dir or os.path.join(ROOT, "docs"), exist_ok=True)
        out = os.path.join(out_dir or os.path.join(ROOT, "docs"), name)
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(html)
        print("wrote", out, len(html), "bytes")
    print("multi:", sum(s["_lang"] == "multi" for s in studies), "en:", sum(s["_lang"] == "en" for s in studies),
          "na:", sum(s["_lang"] == "na" for s in studies))


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", help="output folder (default: docs/)")
    ap.add_argument("--network-url", default="network.html", help="where the library links to the network prototype")
    a = ap.parse_args()
    main(a.out, a.network_url)
