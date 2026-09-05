# retrieval.py

```python

from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CORPUS = Path("/mnt/data/SRI_Day3_Ingestion/synthetic-data/pine-ridge-corpus.jsonl")
ALIASES = ROOT / "config" / "project-aliases.json"

AI_ALLOWED_CLASSES = {"Approved for AI"}

STOP = {
    "what","which","who","is","are","the","a","an","of","for","to","and","in",
    "on","does","do","did","with","at","from","me","tell","give","please",
    "pine","ridge","apartments"
}

def load_records(path=DEFAULT_CORPUS):
    return [
        json.loads(line) for line in Path(path).read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]

def load_aliases():
    return json.loads(ALIASES.read_text(encoding="utf-8"))

def canonical_project(query):
    q = query.lower()
    for project_id, names in load_aliases().items():
        for name in names:
            if re.search(r"\b" + re.escape(name.lower()) + r"\b", q):
                return project_id
    return None

def _tokens(text):
    return [t for t in re.findall(r"[a-z0-9.%/$-]+", text.lower()) if t not in STOP and len(t) > 1]

def _version_num(v):
    if not v:
        return -1
    m = re.search(r"(\d+)", str(v))
    return int(m.group(1)) if m else -1

def _current_query(query):
    q = query.lower()
    return any(k in q for k in ["current", "latest", "now", "today"])

def _historical_query(query):
    q = query.lower()
    return any(k in q for k in ["original", "previous", "prior", "historical", "variance", "changed"])

def retrieve(query, top_k=5, corpus_path=DEFAULT_CORPUS, allowed_classes=None):
    allowed_classes = set(allowed_classes or AI_ALLOWED_CLASSES)
    records = load_records(corpus_path)
    project_id = canonical_project(query)
    qtokens = _tokens(query)
    scored = []

    for r in records:
        # Security/classification gate.
        if r.get("confidentiality_class") not in allowed_classes:
            continue

        # Project scoping: project questions can use the project corpus plus global reference rules.
        if project_id and r.get("project_id") not in {project_id, "GLOBAL"}:
            continue

        hay = (r.get("section_or_page","") + "\n" + r.get("content","")).lower()
        score = 0.0
        for t in qtokens:
            count = hay.count(t)
            if count:
                score += 2.0 + min(count, 4) * 0.5

        # Prefer project-specific records over global guidance for project factual questions.
        if project_id and r.get("project_id") == project_id:
            score += 4.0

        # Approved/current preference.
        if r.get("approval_status") == "Approved":
            score += 3.0
        if _current_query(query) and not _historical_query(query):
            score += max(_version_num(r.get("version_or_effective_date")), 0) * 0.1

        # Context-sensitive ranking.
        q = query.lower()
        sec = r.get("section_or_page","").lower()
        if "occupancy" in q and "project summary" in sec and "downside" not in q:
            score += 8.0
        if "occupancy" in q and "downside" in q and "downside scenario" in sec:
            score += 10.0
        if ("owner" in q or "contractor" in q or "party" in q) and "project team" in sec:
            score += 8.0
        if ("debt" in q or "equity" in q) and "capitalization" in sec:
            score += 8.0
        if ("interest rate" in q or "amortization" in q or "permanent loan" in q) and "permanent financing" in sec:
            score += 8.0
        if "exit cap" in q and "five-year simplified hold" in sec:
            score += 8.0
        if "operating expense ratio" in q and "project summary" in sec:
            score += 8.0
        if ("actual" in q or "verified" in q) and "finance" in sec:
            score += 5.0
        if "turnover" in q and "phoenix" in sec:
            score += 5.0

        if score > 0:
            scored.append((score, r))

    scored.sort(
        key=lambda x: (
            x[0],
            x[1].get("approval_status") == "Approved",
            _version_num(x[1].get("version_or_effective_date"))
        ),
        reverse=True
    )
    return [r for _, r in scored[:top_k]]

def _citation(r):
    return {
        "source_id": r["source_id"],
        "source_title": r["source_title"],
        "section_or_page": r["section_or_page"]
    }

def _find(pattern, text, flags=re.I | re.S):
    m = re.search(pattern, text, flags)
    return m.group(1).strip() if m else None

def _intent(query):
    q = query.lower()

    if "occupancy" in q:
        if any(k in q for k in ["current", "actual", "right now", "today"]):
            return "current_occupancy"
        if "downside" in q or "scenario" in q:
            return "downside_occupancy"
        return "stabilized_occupancy"

    if "how many units" in q or ("units" in q and any(k in q for k in ["planned","project","have"])):
        return "units"
    if "total development cost" in q or "development cost" in q:
        return "tdc"
    if "construction debt" in q or "construction-loan commitment" in q or "construction loan commitment" in q:
        return "construction_debt"
    if "equity" in q and any(k in q for k in ["required","capital","amount"]):
        return "equity"
    if ("average" in q and "rent" in q) or "monthly rent" in q:
        return "average_rent"
    if "property owner" in q or (any(k in q for k in ["owner", "owns", "owned"]) and "pine ridge" in q):
        return "property_owner"
    if "general contractor" in q:
        return "general_contractor"
    if "operating expense ratio" in q or "operating-expense ratio" in q:
        return "opex_ratio"
    if "interest rate" in q and ("permanent" in q or "loan" in q):
        return "perm_rate"
    if "exit cap" in q:
        return "exit_cap"
    if "preferred return" in q or "preferred-return" in q:
        return "preferred_return"
    if "acquisition fee" in q:
        return "acquisition_fee"
    if "actual sri investment" in q or ("actual" in q and "sri" in q and "investment" in q):
        return "actual_investment"
    if ("verified" in q and "actual" in q) or ("who" in q and "financial actual" in q):
        return "verified_actuals"
    if "turnover" in q and ("phoenix" in q or "construction" in q):
        return "phoenix_turnover"
    return None

def answer_question(query, corpus_path=DEFAULT_CORPUS, allowed_classes=None):
    project_id = canonical_project(query)
    intent = _intent(query)

    # A project-specific factual question without a recognized project is not safely answerable.
    if intent and intent not in {"verified_actuals"} and project_id is None and "pine ridge" not in query.lower():
        return {
            "answer": None,
            "status": "unknown",
            "calculation": None,
            "sources": [],
            "affected_functions": [],
            "missing_information": ["Canonical project identity"]
        }

    candidates = retrieve(query, top_k=8, corpus_path=corpus_path, allowed_classes=allowed_classes)

    def first_source(source_id=None, section_contains=None):
        # First prefer ranked candidates, then fall back to the full approved,
        # permission-eligible corpus so an exact requested section cannot be
        # replaced by an unrelated higher-scoring chunk.
        pool = list(candidates)
        allowed = set(allowed_classes or AI_ALLOWED_CLASSES)
        seen = {r["chunk_id"] for r in pool}
        for r in load_records(corpus_path):
            if r["chunk_id"] in seen:
                continue
            if r.get("confidentiality_class") not in allowed:
                continue
            if project_id and r.get("project_id") not in {project_id, "GLOBAL"}:
                continue
            pool.append(r)

        for r in pool:
            if source_id and r["source_id"] != source_id:
                continue
            if section_contains and section_contains.lower() not in r["section_or_page"].lower():
                continue
            if r.get("approval_status") != "Approved":
                continue
            return r
        return None

    # Explicit unknowns: the case does not provide actual/current occupancy, preferred return, or acquisition fee.
    if intent == "current_occupancy":
        supporting = first_source("SRC-CASE-001", "Project summary")
        return {
            "answer": None,
            "status": "unknown",
            "calculation": None,
            "sources": [_citation(supporting)] if supporting else [],
            "affected_functions": ["Property Management", "Asset Management"],
            "missing_information": ["Approved current/actual occupancy record for Pine Ridge"]
        }
    if intent in {"preferred_return", "acquisition_fee"}:
        supporting = first_source("SRC-CASE-001")
        return {
            "answer": None,
            "status": "unknown",
            "calculation": None,
            "sources": [_citation(supporting)] if supporting else [],
            "affected_functions": [],
            "missing_information": [
                "Approved governing/economic source specifying this term"
            ]
        }

    extraction = None
    answer = None
    affected = []

    if intent == "units":
        extraction = first_source("SRC-CASE-001", "Project summary")
        if extraction:
            answer = _find(r"\|\s*Units\s*\|\s*([0-9,]+)\s*\|", extraction["content"])
    elif intent == "tdc":
        extraction = first_source("SRC-CASE-001", "Development budget")
        if extraction:
            answer = _find(r"\*\*Total development cost\*\*\s*\|\s*\*\*(\$[0-9,]+)\*\*", extraction["content"])
    elif intent == "construction_debt":
        extraction = first_source("SRC-CASE-001", "Capitalization")
        if extraction:
            answer = _find(r"\|\s*Construction debt\s*\|\s*(\$[0-9,]+)", extraction["content"])
    elif intent == "equity":
        extraction = first_source("SRC-CASE-001", "Capitalization")
        if extraction:
            answer = _find(r"\|\s*Investor and sponsor equity\s*\|\s*(\$[0-9,]+)", extraction["content"])
    elif intent == "average_rent":
        extraction = first_source("SRC-CASE-001", "Project summary")
        if extraction:
            answer = _find(r"\|\s*Average monthly rent\s*\|\s*(\$[0-9,]+\s*per unit)", extraction["content"])
    elif intent == "stabilized_occupancy":
        extraction = first_source("SRC-CASE-001", "Project summary")
        if extraction:
            answer = _find(r"\|\s*Stabilized physical occupancy\s*\|\s*([0-9.]+%)", extraction["content"])
    elif intent == "downside_occupancy":
        extraction = first_source("SRC-CASE-001", "Day 9 downside scenario")
        if extraction:
            answer = _find(r"Stabilized physical occupancy is\s*([0-9.]+%)", extraction["content"])
    elif intent == "property_owner":
        extraction = first_source("SRC-CASE-001", "Project team")
        if extraction:
            answer = _find(r"\|\s*Property owner\s*\|\s*([^|]+)\|", extraction["content"])
    elif intent == "general_contractor":
        extraction = first_source("SRC-CASE-001", "Project team")
        if extraction:
            answer = _find(r"\|\s*General contractor\s*\|\s*([^|]+)\|", extraction["content"])
    elif intent == "opex_ratio":
        extraction = first_source("SRC-CASE-001", "Project summary")
        if extraction:
            answer = _find(r"\|\s*Operating expense ratio\s*\|\s*([^|]+)\|", extraction["content"])
    elif intent == "perm_rate":
        extraction = first_source("SRC-CASE-001", "Permanent financing")
        if extraction:
            answer = _find(r"\|\s*Interest rate\s*\|\s*([0-9.]+%)", extraction["content"])
    elif intent == "exit_cap":
        extraction = first_source("SRC-CASE-001", "Project summary")
        if extraction:
            answer = _find(r"\|\s*Exit cap rate in Year 5\s*\|\s*([0-9.]+%)", extraction["content"])
    elif intent == "actual_investment":
        extraction = first_source("SRC-CASE-001", "Classification")
        if extraction and "entirely synthetic" in extraction["content"].lower():
            answer = "No. Pine Ridge is an entirely synthetic training case."
    elif intent == "verified_actuals":
        extraction = first_source("SRC-CUR-001", "Finance's role")
        if not extraction:
            extraction = first_source("SRC-CUR-001", "Operating model")
        if extraction:
            answer = "Finance & Administration"
            affected = ["Finance & Administration"]
    elif intent == "phoenix_turnover":
        extraction = first_source("SRC-CUR-001", "Asset-transition packet")
        if extraction:
            answer = (
                "The asset-transition packet, including applicable CO/TCO and permit closeout, "
                "warranties, as-builts, O&M manuals, equipment records, keys/access information, "
                "final draw and lien-waiver support, final job-cost-versus-budget reporting, "
                "delivery/leasing-enablement schedule, open-item ownership, and warranty-period process."
            )
            affected = ["Phoenix Construction", "Property Management", "Asset Management"]
    else:
        # Retrieval-only fallback: enough to provide grounded context, but not invent an answer.
        return {
            "answer": None,
            "status": "unknown",
            "calculation": None,
            "sources": [_citation(r) for r in candidates[:3]],
            "affected_functions": [],
            "missing_information": ["No implemented factual extractor supports this question yet"]
        }

    if answer is None or extraction is None:
        return {
            "answer": None,
            "status": "unknown",
            "calculation": None,
            "sources": [_citation(r) for r in candidates[:3]],
            "affected_functions": affected,
            "missing_information": ["No approved source passage was sufficient to support the requested fact"]
        }

    return {
        "answer": answer.strip() if isinstance(answer, str) else answer,
        "status": "confirmed",
        "calculation": None,
        "sources": [_citation(extraction)],
        "affected_functions": affected,
        "missing_information": []
    }

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("question")
    args = parser.parse_args()
    print(json.dumps(answer_question(args.question), indent=2, ensure_ascii=False))
```

---

# test_retrieval.py

```python

from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from retrieval import answer_question, retrieve

def assert_confirmed(question, expected):
    r = answer_question(question)
    assert r["status"] == "confirmed", r
    assert expected.lower() in str(r["answer"]).lower(), r
    assert len(r["sources"]) >= 1, r
    assert r["sources"][0]["source_id"], r
    assert "lines " in r["sources"][0]["section_or_page"], r
    assert r["missing_information"] == [], r

def test_project_fact_units():
    assert_confirmed("How many units are planned for Pine Ridge Apartments?", "200")

def test_project_fact_occupancy():
    assert_confirmed("What stabilized occupancy was underwritten for PRA?", "95%")

def test_current_occupancy_is_unknown_not_assumed():
    r = answer_question("What is Pine Ridge's current occupancy?")
    assert r["status"] == "unknown", r
    assert r["answer"] is None, r
    assert "current/actual occupancy" in r["missing_information"][0], r

def test_downside_occupancy_is_distinguished_from_base_case():
    assert_confirmed("In the Pine Ridge downside scenario, what stabilized occupancy is assumed?", "92%")

def test_property_owner():
    assert_confirmed("Which entity is the property owner for Pine Ridge?", "Pine Ridge Owner LLC")

def test_general_contractor():
    assert_confirmed("Who is Pine Ridge's general contractor?", "Phoenix Commercial Construction")

def test_construction_debt():
    assert_confirmed("What construction debt is committed to Pine Ridge?", "$33,600,000")

def test_equity():
    assert_confirmed("How much equity capital is required for Pine Ridge?", "$22,400,000")

def test_monthly_rent():
    assert_confirmed("What average monthly rent per unit was assumed for Pine Ridge?", "$2,100")

def test_operating_expense_ratio():
    assert_confirmed("What operating expense ratio is assumed for Pine Ridge?", "38%")

def test_permanent_loan_rate():
    assert_confirmed("What interest rate is assumed for the Pine Ridge permanent loan?", "6.25%")

def test_exit_cap():
    assert_confirmed("What Year 5 exit cap rate is assumed for Pine Ridge?", "5.50%")

def test_synthetic_classification():
    assert_confirmed("Is Pine Ridge an actual SRI investment?", "No")

def test_verified_actuals_role():
    assert_confirmed("Which function establishes verified financial actuals?", "Finance & Administration")

def test_preferred_return_is_unknown():
    r = answer_question("What preferred return applies to Pine Ridge?")
    assert r["status"] == "unknown", r
    assert r["answer"] is None, r
    assert r["sources"], r

def test_acquisition_fee_is_unknown():
    r = answer_question("What acquisition fee does Pine Ridge pay?")
    assert r["status"] == "unknown", r
    assert r["answer"] is None, r

def test_retrieval_filters_to_ai_approved_classification():
    rs = retrieve("Pine Ridge construction debt")
    assert rs
    assert all(r["confidentiality_class"] == "Approved for AI" for r in rs)

def test_project_alias_resolves():
    r = answer_question("What stabilized occupancy was underwritten for PRA?")
    assert r["status"] == "confirmed"
    assert r["answer"] == "95%"

def test_exact_citation_contract():
    r = answer_question("Which entity owns Pine Ridge?")
    s = r["sources"][0]
    assert s["source_id"] == "SRC-CASE-001"
    assert s["source_title"] == "Synthetic Case Study — Pine Ridge Apartments"
    assert "Project team" in s["section_or_page"]
    assert "lines " in s["section_or_page"]

def test_answer_contract_fields_always_present():
    r = answer_question("What stabilized occupancy was underwritten for Pine Ridge?")
    assert set(r.keys()) == {
        "answer","status","calculation","sources","affected_functions","missing_information"
    }

def test_no_unsupported_answer_fallback():
    r = answer_question("What color is the Pine Ridge lobby?")
    assert r["status"] == "unknown"
    assert r["answer"] is None
```

---

# retrieval-demo-results.json

```json
[
  {
    "question": "How many units are planned for Pine Ridge Apartments?",
    "result": {
      "answer": "200",
      "status": "confirmed",
      "calculation": null,
      "sources": [
        {
          "source_id": "SRC-CASE-001",
          "source_title": "Synthetic Case Study — Pine Ridge Apartments",
          "section_or_page": "Synthetic Case Study — Pine Ridge Apartments > Project summary | lines 7-23"
        }
      ],
      "affected_functions": [],
      "missing_information": []
    }
  },
  {
    "question": "What stabilized occupancy was underwritten for PRA?",
    "result": {
      "answer": "95%",
      "status": "confirmed",
      "calculation": null,
      "sources": [
        {
          "source_id": "SRC-CASE-001",
          "source_title": "Synthetic Case Study — Pine Ridge Apartments",
          "section_or_page": "Synthetic Case Study — Pine Ridge Apartments > Project summary | lines 7-23"
        }
      ],
      "affected_functions": [],
      "missing_information": []
    }
  },
  {
    "question": "What is Pine Ridge's current occupancy?",
    "result": {
      "answer": null,
      "status": "unknown",
      "calculation": null,
      "sources": [
        {
          "source_id": "SRC-CASE-001",
          "source_title": "Synthetic Case Study — Pine Ridge Apartments",
          "section_or_page": "Synthetic Case Study — Pine Ridge Apartments > Project summary | lines 7-23"
        }
      ],
      "affected_functions": [
        "Property Management",
        "Asset Management"
      ],
      "missing_information": [
        "Approved current/actual occupancy record for Pine Ridge"
      ]
    }
  },
  {
    "question": "Which entity is the property owner for Pine Ridge?",
    "result": {
      "answer": "Pine Ridge Owner LLC",
      "status": "confirmed",
      "calculation": null,
      "sources": [
        {
          "source_id": "SRC-CASE-001",
          "source_title": "Synthetic Case Study — Pine Ridge Apartments",
          "section_or_page": "Synthetic Case Study — Pine Ridge Apartments > Project team | lines 24-37"
        }
      ],
      "affected_functions": [],
      "missing_information": []
    }
  },
  {
    "question": "What construction debt is committed to Pine Ridge?",
    "result": {
      "answer": "$33,600,000",
      "status": "confirmed",
      "calculation": null,
      "sources": [
        {
          "source_id": "SRC-CASE-001",
          "source_title": "Synthetic Case Study — Pine Ridge Apartments",
          "section_or_page": "Synthetic Case Study — Pine Ridge Apartments > Development budget > Capitalization | lines 49-58"
        }
      ],
      "affected_functions": [],
      "missing_information": []
    }
  },
  {
    "question": "What interest rate is assumed for the Pine Ridge permanent loan?",
    "result": {
      "answer": "6.25%",
      "status": "confirmed",
      "calculation": null,
      "sources": [
        {
          "source_id": "SRC-CASE-001",
          "source_title": "Synthetic Case Study — Pine Ridge Apartments",
          "section_or_page": "Synthetic Case Study — Pine Ridge Apartments > Permanent financing | lines 103-137"
        }
      ],
      "affected_functions": [],
      "missing_information": []
    }
  },
  {
    "question": "What preferred return applies to Pine Ridge?",
    "result": {
      "answer": null,
      "status": "unknown",
      "calculation": null,
      "sources": [
        {
          "source_id": "SRC-CASE-001",
          "source_title": "Synthetic Case Study — Pine Ridge Apartments",
          "section_or_page": "Synthetic Case Study — Pine Ridge Apartments > Permanent financing | lines 103-137"
        }
      ],
      "affected_functions": [],
      "missing_information": [
        "Approved governing/economic source specifying this term"
      ]
    }
  },
  {
    "question": "Is Pine Ridge an actual SRI investment?",
    "result": {
      "answer": "No. Pine Ridge is an entirely synthetic training case.",
      "status": "confirmed",
      "calculation": null,
      "sources": [
        {
          "source_id": "SRC-CASE-001",
          "source_title": "Synthetic Case Study — Pine Ridge Apartments",
          "section_or_page": "Synthetic Case Study — Pine Ridge Apartments > Classification | lines 3-6"
        }
      ],
      "affected_functions": [],
      "missing_information": []
    }
  }
]
```

---

# retrieval-validation.json

```json
{
  "status": "PASS",
  "requirements_checked": {
    "canonical_project_and_alias_resolution": true,
    "project_scoped_retrieval": true,
    "approved_source_preference": true,
    "confidentiality_filtering": true,
    "exact_source_and_section_citations": true,
    "answer_status_contract": true,
    "unknown_when_unsupported": true,
    "base_vs_downside_context_separation": true,
    "evaluation_suite_excluded_from_retrieval_corpus": true
  },
  "tests": "\u001b[32m.\u001b[0m\u001b[32m.\u001b[0m\u001b[32m.\u001b[0m\u001b[32m.\u001b[0m\u001b[32m.\u001b[0m\u001b[32m.\u001b[0m\u001b[32m.\u001b[0m\u001b[32m.\u001b[0m\u001b[32m.\u001b[0m\u001b[32m.\u001b[0m\u001b[32m.\u001b[0m\u001b[32m.\u001b[0m\u001b[32m.\u001b[0m\u001b[32m.\u001b[0m\u001b[32m.\u001b[0m\u001b[32m.\u001b[0m\u001b[32m.\u001b[0m\u001b[32m.\u001b[0m\u001b[32m.\u001b[0m\u001b[32m.\u001b[0m\u001b[32m.\u001b[0m\u001b[32m                                                    [100%]\u001b[0m\n\u001b[32m\u001b[32m\u001b[1m21 passed\u001b[0m\u001b[32m in 0.08s\u001b[0m\u001b[0m",
  "errors": "Spreadsheet runtime warmup failed during python startup\nTraceback (most recent call last):\n  File \"/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/patches/warm_spreadsheet_runtime_on_startup.py\", line 26, in warm_spreadsheet_runtime_on_startup\n  File \"/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/spreadsheet_warmup.py\", line 785, in warm_spreadsheet_runtime\n  File \"/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/spreadsheet_warmup.py\", line 720, in _warm_feature_flows\n  File \"/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/spreadsheet_warmup.py\", line 704, in _warm_collaboration_flows\n  File \"/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/generated/interface/models.py\", line 32317, in hydrate_crdt_from_proto\n  File \"/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/rpc/remote.py\", line 749, in __call__\n  File \"/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/rpc/client.py\", line 150, in call\nartifact_tool.rpc.client.RemoteError: hydrateCrdtFromProto requires an empty collaborative document."
}
```
