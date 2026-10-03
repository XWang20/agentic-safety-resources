import json
import re
from pathlib import Path
from urllib.parse import urlparse

root = Path(__file__).resolve().parents[1]
records = json.loads((root / "data/resources.json").read_text(encoding="utf-8"))
required = {"id", "title", "category", "source_url", "purpose", "source_type", "limitations", "runtime_status", "license_notes"}
ids = [r["id"] for r in records]
assert len(ids) == len(set(ids)), "Duplicate resource ids"
for r in records:
    assert required <= r.keys(), (r.get("id"), required - r.keys())
    assert r["category"] in {"training", "lifecycle", "evaluation", "boundaries"}
    assert r["runtime_status"] == "not_reproduced", "Runtime claims need documented replication evidence"
    for url in [r["source_url"], *r.get("code_urls", []), *r.get("data_urls", [])]:
        parsed = urlparse(url)
        assert parsed.scheme in {"http", "https"} and parsed.netloc, url
for file in root.rglob("*.md"):
    text = file.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
        if target.startswith(("http://", "https://", "#")):
            continue
        path = target.split("#", 1)[0]
        assert (file.parent / path).exists(), (str(file.relative_to(root)), target)
print(json.dumps({"resources": len(records), "categories": sorted({r["category"] for r in records}), "status": "valid"}, ensure_ascii=False))
