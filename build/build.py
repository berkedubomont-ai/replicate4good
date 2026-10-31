#!/usr/bin/env python3
"""Build the AI Safety Replication Library.

Default: read data/studies.json and data/resources.json, validate them, and
regenerate data/*.csv, the website in docs/ and README.md.

    python3 build/build.py

Merge mode: combine several raw JSON files (each {"studies": [...],
"resources": [...]}) into data/, removing duplicates, then build.

    python3 build/build.py --merge path/to/raw/*.json

Warnings are printed and written to build/warnings.txt. Fix them in the data
files and run the build again.
"""
import argparse
import csv
import io
import json
import os
import re
import sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, "data")
SITE = os.path.join(ROOT, "site")
CHECKED = "2026-10-31"

CATS = [
    "Model organisms and misalignment",
    "Oversight and weak-to-strong generalisation",
    "Evaluation and situational awareness",
    "Reasoning transparency, monitoring and control",
    "Interpretability and representations",
    "Fine-tuning, unlearning and tamper resistance",
    "Jailbreaks, robustness and multilingual safety",
    "Dangerous capabilities and agentic evaluation",
    "Evaluation science and measurement",
]
STATUS = [
    "replicated",
    "partially replicated",
    "conditional",
    "failed to replicate",
    "contested",
    "no public replication found",
]
STATUS_ALIASES = {
    "partial": "partially replicated",
    "partially": "partially replicated",
    "partly replicated": "partially replicated",
    "conditional (holds under some conditions)": "conditional",
    "conditionally replicated": "conditional",
    "failed": "failed to replicate",
    "failed replication": "failed to replicate",
    "not replicated": "failed to replicate",
    "none": "no public replication found",
    "no replication found": "no public replication found",
    "no public replication": "no public replication found",
    "not yet replicated": "no public replication found",
}
OUTCOMES = ["replicated", "partial", "conditional", "failed", "extended"]
OUTCOME_ALIASES = {
    "partially replicated": "partial",
    "partially": "partial",
    "failed to replicate": "failed",
    "not replicated": "failed",
    "extension": "extended",
    "follow-up": "extended",
    "followup": "extended",
    "replication": "replicated",
}
CLAIM_TYPES = ["existence", "prevalence", "magnitude", "mechanism", "ranking", "method"]
DIFF = ["starter", "intermediate", "advanced"]
TIERS = ["T0", "T1", "T2", "T3"]
ACCESS = ["open-weight", "API-only", "mixed"]
ACCESS_ALIASES = {
    "open weights": "open-weight",
    "open-weights": "open-weight",
    "open weight": "open-weight",
    "api": "API-only",
    "api only": "API-only",
    "closed": "API-only",
    "both": "mixed",
}
AVAIL = ["yes", "partly", "no", "unknown"]
RTYPES = [
    "Replication programme or collection",
    "Methodology guide or checklist",
    "Evaluation framework or harness",
    "Interpretability tooling",
    "Automated replication tool",
    "Benchmark or dataset",
    "Compute or model access",
    "Funding or fellowship",
    "Research group or lab",
    "Community or course",
]
RACCESS = ["free and open", "free with sign-up", "paid", "restricted or by application"]
RSTATUS = ["active", "archived or discontinued", "unknown"]

STUDY_FIELDS = [
    "id", "short_name", "title", "authors", "year", "organisation", "paper_url", "category",
    "core_claim", "claim_types", "original_models", "model_access",
    "models_still_available", "code_url", "data_url", "tooling", "compute_tier",
    "compute_note", "difficulty", "replication_status", "replications",
    "replication_search_limited", "languages_tested", "multilingual_port", "why_it_matters", "pitfalls",
    "replication_ideas", "tags",
]
STUDY_REQUIRED = ["id", "title", "authors", "year", "paper_url", "category", "core_claim",
                  "replication_status", "difficulty", "compute_tier", "model_access"]
RESOURCE_FIELDS = ["id", "name", "type", "url", "description", "use_for", "access",
                   "maintainer", "status", "multilingual_relevance", "tags"]
RESOURCE_REQUIRED = ["id", "name", "type", "url", "description", "access"]
TEXT_STUDY = ["title", "authors", "organisation", "core_claim", "tooling", "compute_note",
              "languages_tested", "multilingual_port", "why_it_matters", "pitfalls"]
TEXT_RESOURCE = ["name", "description", "use_for", "maintainer", "multilingual_relevance"]

WARNINGS = []

SHORT_TOKENS = {
    "llm": "LLM", "llms": "LLMs", "ai": "AI", "i4r": "I4R", "mt": "MT", "cot": "CoT", "sad": "SAD",
    "rlhf": "RLHF", "em": "EM", "wmdp": "WMDP", "rmu": "RMU", "gcg": "GCG", "ccs": "CCS", "metr": "METR",
    "lora": "LoRA", "xsafety": "XSafety", "multijail": "MultiJail", "strongreject": "StrongREJECT",
    "paperbench": "PaperBench", "agentharm": "AgentHarm", "cybench": "Cybench", "somalibench": "SomaliBench",
    "openethics": "OpenEthics", "aisi": "AISI", "uk": "UK", "rl": "RL", "sae": "SAE", "saes": "SAEs",
}
SHORT_OVERRIDES = {
    "re-bench-2024": "RE-Bench 2024",
    "mle-bench-2024": "MLE-bench 2024",
    "sa-bench-2026": "SA-Bench 2026",
    "best-of-n-jailbreaking-2024": "Best-of-N jailbreaking 2024",
    "llm-as-a-judge-mt-bench-2023": "LLM-as-a-judge 2023",
    "i4r-ai-teams-reproducibility-2025": "I4R AI teams trial 2025",
    "weak-to-strong-2023": "Weak-to-strong 2023",
    "sad-2024": "SAD benchmark 2024",
    "gcg-2023": "GCG attack 2023",
    "in-context-scheming-2024": "In-context scheming 2024",
    "ctrl-z-2025": "Ctrl-Z 2025",
    "password-locked-models-2024": "Password-locked models 2024",
    "anti-scheming-eval-awareness-2025": "Anti-scheming eval awareness 2025",
    "many-shot-jailbreaking-2024": "Many-shot jailbreaking 2024",
    "low-resource-languages-jailbreak-2023": "Low-resource languages jailbreak 2023",
    "multilingual-fine-tuning-attacks-2024": "Multilingual fine-tuning attacks 2024",
    "tamper-resistant-safeguards-2024": "Tamper-resistant safeguards 2024",
    "model-written-evals-2022": "Model-written evals 2022",
    "finetuning-compromises-safety-2023": "Fine-tuning compromises safety 2023",
    "reward-model-overoptimization-2022": "Reward model overoptimisation 2022",
    "turkish-prompt-injection-benchmark-2026": "Turkish safety benchmark 2026",
    "multilingual-obfuscated-prompt-injection-2026": "Multilingual prompt injection 2026",
}


def short_name_for(sid):
    if sid in SHORT_OVERRIDES:
        return SHORT_OVERRIDES[sid]
    words = [SHORT_TOKENS.get(p, p) for p in sid.split("-")]
    s = " ".join(words)
    return s[:1].upper() + s[1:]


def warn(msg):
    WARNINGS.append(msg)


def slugify(s):
    s = re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")
    return s[:80] or "item"


def tkey(t):
    return re.sub(r"[^a-z0-9]", "", str(t or "").lower())


def is_blank(v):
    return v is None or v == "" or v == [] or v == {}


def norm_enum(value, allowed, aliases, where, field):
    if value is None:
        return ""
    s = str(value).strip()
    if not s:
        return ""
    low = s.lower()
    for a in allowed:
        if low == a.lower():
            return a
    if aliases and low in aliases:
        return aliases[low]
    for a in sorted(allowed, key=len, reverse=True):
        if low.startswith(a.lower()):
            warn(f"{where}: {field} {s!r} read as {a!r}")
            return a
    warn(f"{where}: {field} {s!r} is not an allowed value")
    return s


ARXIV = re.compile(r"^https?://(?:www\.)?arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})(v\d+)?(?:\.pdf)?/?(?:[#?].*)?$")


def norm_url(u, where, field):
    if is_blank(u):
        return ""
    u = str(u).strip()
    if not re.match(r"^https?://", u):
        warn(f"{where}: {field} is not a URL: {u!r}")
        return ""
    if re.search(r"x{3,}|X{3,}|\.\.\.|\s|[<>]", u):
        warn(f"{where}: suspicious {field}: {u}")
    m = ARXIV.match(u)
    if m:
        ident = m.group(1)
        yymm = int(ident[:4])
        yy, mm = divmod(yymm, 100)
        if not (7 <= yy <= 26 and 1 <= mm <= 12) or yymm > 2610:
            warn(f"{where}: implausible arXiv identifier in {field}: {u}")
        return f"https://arxiv.org/abs/{ident}"
    if "arxiv.org" in u and "/list/" not in u:
        warn(f"{where}: non-standard arXiv URL in {field}: {u}")
    return u


def clean_text(v, where, field):
    if is_blank(v):
        return ""
    s = str(v).strip()
    if "\u2014" in s or " \u2013 " in s:
        s = re.sub(r"\s*\u2014\s*", ", ", s)
        s = s.replace(" \u2013 ", ", ")
        warn(f"{where}: replaced a dash in {field}")
    return re.sub(r"\s{2,}", " ", s)


def as_list(v):
    if is_blank(v):
        return []
    if isinstance(v, list):
        return [str(x).strip() for x in v if not is_blank(x)]
    return [x.strip() for x in re.split(r";|\n", str(v)) if x.strip()]


def norm_study(s, src):
    out = {}
    sid = slugify(s.get("id") or s.get("title") or "study")
    where = f"study {sid}"
    out["id"] = sid
    out["short_name"] = clean_text(s.get("short_name"), where, "short_name") or short_name_for(sid)
    for f in TEXT_STUDY:
        out[f] = clean_text(s.get(f), where, f)
    try:
        out["year"] = int(str(s.get("year", "")).strip()[:4])
    except ValueError:
        out["year"] = 0
        warn(f"{where}: year missing or invalid")
    if out["year"] and not (1990 <= out["year"] <= 2026):
        warn(f"{where}: year {out['year']} out of range")
    out["paper_url"] = norm_url(s.get("paper_url"), where, "paper_url")
    out["code_url"] = norm_url(s.get("code_url"), where, "code_url")
    out["data_url"] = norm_url(s.get("data_url"), where, "data_url")
    out["category"] = norm_enum(s.get("category"), CATS, None, where, "category")
    out["model_access"] = norm_enum(s.get("model_access"), ACCESS, ACCESS_ALIASES, where, "model_access")
    out["models_still_available"] = norm_enum(s.get("models_still_available") or "unknown", AVAIL, None, where, "models_still_available")
    out["compute_tier"] = norm_enum(s.get("compute_tier"), TIERS, None, where, "compute_tier")
    out["difficulty"] = norm_enum(s.get("difficulty"), DIFF, None, where, "difficulty")
    out["replication_status"] = norm_enum(s.get("replication_status"), STATUS, STATUS_ALIASES, where, "replication_status")
    ct = []
    for c in as_list(s.get("claim_types") or s.get("claim_type")):
        ct.append(norm_enum(c, CLAIM_TYPES, None, where, "claim_types"))
    out["claim_types"] = list(dict.fromkeys(ct))
    out["original_models"] = as_list(s.get("original_models"))
    out["replication_ideas"] = [clean_text(x, where, "replication_ideas") for x in as_list(s.get("replication_ideas"))]
    out["tags"] = sorted(set(t.lower() for t in as_list(s.get("tags"))))
    reps = []
    for r in s.get("replications") or []:
        if not isinstance(r, dict):
            continue
        rep = {
            "title": clean_text(r.get("title"), where, "replications.title"),
            "url": norm_url(r.get("url"), where, "replications.url"),
            "by": clean_text(r.get("by"), where, "replications.by"),
            "year": r.get("year") or "",
            "outcome": norm_enum(r.get("outcome"), OUTCOMES, OUTCOME_ALIASES, where, "replications.outcome"),
            "summary": clean_text(r.get("summary"), where, "replications.summary"),
        }
        try:
            rep["year"] = int(str(rep["year"])[:4]) if rep["year"] != "" else ""
        except ValueError:
            rep["year"] = ""
        if not rep["title"] and not rep["url"]:
            continue
        reps.append(rep)
    out["replications"] = reps
    out["replication_search_limited"] = bool(s.get("replication_search_limited", False))
    out["_sources"] = [src]
    return out


def norm_resource(r, src):
    out = {}
    rid = slugify(r.get("id") or r.get("name") or "resource")
    where = f"resource {rid}"
    out["id"] = rid
    for f in TEXT_RESOURCE:
        out[f] = clean_text(r.get(f), where, f)
    out["type"] = norm_enum(r.get("type"), RTYPES, None, where, "type")
    out["url"] = norm_url(r.get("url"), where, "url")
    out["access"] = norm_enum(r.get("access"), RACCESS, None, where, "access")
    out["status"] = norm_enum(r.get("status") or "unknown", RSTATUS, None, where, "status")
    out["tags"] = sorted(set(t.lower() for t in as_list(r.get("tags"))))
    out["_sources"] = [src]
    return out


def filled(rec):
    return sum(1 for k, v in rec.items() if not k.startswith("_") and not is_blank(v))


def merge_records(a, b, kind):
    base, other = (a, b) if filled(a) >= filled(b) else (b, a)
    out = dict(base)
    for k, v in other.items():
        if k.startswith("_"):
            continue
        if is_blank(out.get(k)) and not is_blank(v):
            out[k] = v
    if kind == "study":
        seen, reps = set(), []
        for r in (base.get("replications") or []) + (other.get("replications") or []):
            key = (r.get("url") or "").rstrip("/").lower() or tkey(r.get("title"))
            if key in seen:
                continue
            seen.add(key)
            reps.append(r)
        out["replications"] = reps
        if base.get("replication_status") != other.get("replication_status"):
            warn(f"study {out['id']}: duplicate records disagree on status "
                 f"({base.get('replication_status')!r} vs {other.get('replication_status')!r}); kept {out.get('replication_status')!r}")
    out["tags"] = sorted(set((base.get("tags") or []) + (other.get("tags") or [])))
    out["_sources"] = sorted(set(base.get("_sources", []) + other.get("_sources", [])))
    return out


def url_key(u):
    u = (u or "").strip().lower().rstrip("/")
    u = re.sub(r"^https?://(www\.)?", "", u)
    return u


def dedupe(records, kind):
    by_key = {}
    order = []
    for rec in records:
        keys = [("id", rec["id"]), ("title", tkey(rec.get("title") or rec.get("name")))]
        if kind == "study" and rec.get("paper_url"):
            keys.append(("url", url_key(rec["paper_url"])))
        if kind == "resource" and rec.get("url"):
            keys.append(("url", url_key(rec["url"])))
        hit = None
        for k in keys:
            if k[1] and k in by_key:
                hit = by_key[k]
                break
        if hit is None:
            order.append(rec)
            idx = len(order) - 1
        else:
            idx = hit
            warn(f"{kind} {rec['id']}: duplicate of {order[idx]['id']} (from {rec['_sources']} and {order[idx]['_sources']}); merged")
            order[idx] = merge_records(order[idx], rec, kind)
        for k in keys:
            if k[1]:
                by_key[k] = idx
        rec_keys_after = [("id", order[idx]["id"])]
        for k in rec_keys_after:
            by_key[k] = idx
    return order


def check_study(s):
    where = f"study {s['id']}"
    for f in STUDY_REQUIRED:
        if is_blank(s.get(f)):
            warn(f"{where}: missing {f}")
    indep = [r for r in s["replications"] if r.get("outcome") and r["outcome"] != "extended"]
    st = s.get("replication_status")
    if st == "no public replication found" and indep:
        warn(f"{where}: status says no replication but {len(indep)} independent replication(s) are listed")
    if st in ("replicated", "partially replicated", "conditional", "failed to replicate") and not indep:
        warn(f"{where}: status {st!r} but no independent replication is listed")
    for r in s["replications"]:
        if not r.get("url"):
            warn(f"{where}: replication {r.get('title')!r} has no URL")


def check_resource(r):
    where = f"resource {r['id']}"
    for f in RESOURCE_REQUIRED:
        if is_blank(r.get(f)):
            warn(f"{where}: missing {f}")


def ordered(rec, fields):
    out = {f: rec.get(f, "" if f not in ("claim_types", "original_models", "replications", "replication_ideas", "tags") else []) for f in fields}
    return out


def unique_ids(records, kind):
    seen = {}
    for rec in records:
        base = rec["id"]
        if base in seen:
            seen[base] += 1
            rec["id"] = f"{base}-{seen[base]}"
            warn(f"{kind} {base}: id clash, renamed to {rec['id']}")
        else:
            seen[base] = 1


def csv_text(rows, fields):
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(fields)
    for r in rows:
        line = []
        for f in fields:
            v = r.get(f, "")
            if f == "replications":
                v = "; ".join(f"{x.get('outcome', '')}: {x.get('title', '')} ({x.get('url', '')})" for x in v)
            elif isinstance(v, bool):
                v = "yes" if v else "no"
            elif isinstance(v, list):
                v = "; ".join(str(x) for x in v)
            line.append(v)
        w.writerow(line)
    return buf.getvalue()


def md(s):
    return str(s or "").replace("|", "\\|").replace("\n", " ")


def readme(studies, resources):
    n_rerun = sum(1 for s in studies if s["replication_status"] != "no public replication found")
    L = [
        "# AI Safety Replication Library",
        "",
        "Empirical AI safety findings worth re-running, what it takes to re-run them, and what happened when others tried.",
        "",
        f"Draft v0.2, last checked {CHECKED}. {len(studies)} studies and {len(resources)} resources. "
        f"{n_rerun} of the {len(studies)} studies have been independently re-run or re-analysed.",
        "",
        "## What is in this folder",
        "",
        "- `docs/index.html`: the library website, a single self-contained page with every study and resource inside. Open it in a browser; it needs no server. GitHub Pages serves this folder.",
        "- `docs/network.html`: a prototype of the replication network built on the library. Its forms do not send anything.",
        "- `data/studies.json` and `data/studies.csv`: one record per study. Each gives the claim and the conditions it was shown under, the claim type, the models and whether they are still available, code and data links, a compute tier, difficulty, known replications and their outcomes, languages tested, what porting to another language would involve, pitfalls, and replication ideas.",
        "- `data/resources.json` and `data/resources.csv`: replication programmes, evaluation harnesses, interpretability tooling, automated replication tools, compute and model access, methodology guides, funding, research groups and courses.",
        "- `SCHEMA.md`: field definitions and allowed values.",
        "- `CONTRIBUTING.md`: how to add or correct an entry.",
        "- `build/build.py`: validates the data and regenerates the CSV files, the website and this README. `build/build_site.py` builds the website alone from `build/site_template.html`.",
        "",
        "## Replication status",
        "",
        "| Status | Studies |",
        "| --- | ---: |",
    ]
    for st in STATUS:
        n = sum(1 for s in studies if s["replication_status"] == st)
        if n:
            L.append(f"| {st[0].upper() + st[1:]} | {n} |")
    L += [
        "",
        "Only replications by different authors count towards a status. Follow-ups by the original team are listed as extended.",
        "",
        "## Studies",
        "",
    ]
    for cat in CATS:
        items = sorted([s for s in studies if s["category"] == cat], key=lambda s: (-(s.get("year") or 0), s["title"].lower()))
        if not items:
            continue
        L += [f"### {cat}", "", "| Study | Year | Status | Difficulty | Compute | Code |", "| --- | ---: | --- | --- | --- | --- |"]
        for s in items:
            title = f"[{md(s['title'])}]({s['paper_url']})" if s.get("paper_url") else md(s["title"])
            code = f"[Code]({s['code_url']})" if s.get("code_url") else ""
            L.append(f"| {title} | {s.get('year') or ''} | {md(s['replication_status'])} | {md(s.get('difficulty'))} | {md(s.get('compute_tier'))} | {code} |")
        L.append("")
    L += ["## Resources", ""]
    types = RTYPES + sorted(set(r["type"] for r in resources) - set(RTYPES))
    for t in types:
        items = sorted([r for r in resources if r["type"] == t], key=lambda r: r["name"].lower())
        if not items:
            continue
        L += [f"### {t}", "", "| Resource | What it is | Access |", "| --- | --- | --- |"]
        for r in items:
            name = f"[{md(r['name'])}]({r['url']})" if r.get("url") else md(r["name"])
            L.append(f"| {name} | {md(r.get('description'))} | {md(r.get('access'))} |")
        L.append("")
    n_limited = sum(1 for s in studies if s.get("replication_search_limited"))
    L += [
        "## Caveats",
        "",
        "Statuses are a snapshot from public sources and will go out of date as new replications appear. Coverage is uneven across areas, and work published outside English is under-represented. A status records what was found, not a judgement of the original work.",
        "",
        f"Replication searches were cut short for {n_limited} studies (marked `replication_search_limited`). For those, \"no public replication found\" means none turned up in a partial search.",
        "",
        "## Licence",
        "",
        "Not yet chosen. CC BY 4.0 is a common choice for datasets like this one.",
        "",
    ]
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--merge", nargs="+", help="raw JSON files to merge into data/")
    args = ap.parse_args()

    studies, resources = [], []
    if args.merge:
        for path in sorted(args.merge):
            src = os.path.basename(path)
            try:
                with open(path, encoding="utf-8") as fh:
                    blob = json.load(fh)
            except (OSError, json.JSONDecodeError) as e:
                warn(f"{src}: could not read ({e})")
                continue
            studies += [norm_study(s, src) for s in blob.get("studies", []) if isinstance(s, dict)]
            resources += [norm_resource(r, src) for r in blob.get("resources", []) if isinstance(r, dict)]
    else:
        with open(os.path.join(DATA, "studies.json"), encoding="utf-8") as fh:
            studies = [norm_study(s, "studies.json") for s in json.load(fh)]
        with open(os.path.join(DATA, "resources.json"), encoding="utf-8") as fh:
            resources = [norm_resource(r, "resources.json") for r in json.load(fh)]

    studies = dedupe(studies, "study")
    resources = dedupe(resources, "resource")
    unique_ids(studies, "study")
    unique_ids(resources, "resource")
    for s in studies:
        check_study(s)
    for r in resources:
        check_resource(r)

    studies.sort(key=lambda s: (CATS.index(s["category"]) if s["category"] in CATS else 99, -(s.get("year") or 0), s["title"].lower()))
    resources.sort(key=lambda r: (RTYPES.index(r["type"]) if r["type"] in RTYPES else 99, r["name"].lower()))
    sources = {"studies": {s["id"]: s["_sources"] for s in studies}, "resources": {r["id"]: r["_sources"] for r in resources}}
    studies_out = [ordered(s, STUDY_FIELDS) for s in studies]
    resources_out = [ordered(r, RESOURCE_FIELDS) for r in resources]

    os.makedirs(DATA, exist_ok=True)
    with open(os.path.join(DATA, "studies.json"), "w", encoding="utf-8") as fh:
        json.dump(studies_out, fh, ensure_ascii=False, indent=2)
    with open(os.path.join(DATA, "resources.json"), "w", encoding="utf-8") as fh:
        json.dump(resources_out, fh, ensure_ascii=False, indent=2)
    with open(os.path.join(DATA, "studies.csv"), "w", encoding="utf-8") as fh:
        fh.write(csv_text(studies_out, STUDY_FIELDS))
    with open(os.path.join(DATA, "resources.csv"), "w", encoding="utf-8") as fh:
        fh.write(csv_text(resources_out, RESOURCE_FIELDS))
    with open(os.path.join(HERE, "sources.json"), "w", encoding="utf-8") as fh:
        json.dump(sources, fh, indent=2)

    import build_site
    build_site.main()
    with open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8") as fh:
        fh.write(readme(studies_out, resources_out))

    with open(os.path.join(HERE, "warnings.txt"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(WARNINGS) + ("\n" if WARNINGS else ""))
    by_status = {st: sum(1 for s in studies_out if s["replication_status"] == st) for st in STATUS}
    print(f"studies: {len(studies_out)}  resources: {len(resources_out)}")
    print("status:", json.dumps(by_status))
    print("by category:", json.dumps({c: sum(1 for s in studies_out if s['category'] == c) for c in CATS}))
    print(f"warnings: {len(WARNINGS)} (see build/warnings.txt)")
    for w in WARNINGS:
        print("  -", w)


if __name__ == "__main__":
    main()
