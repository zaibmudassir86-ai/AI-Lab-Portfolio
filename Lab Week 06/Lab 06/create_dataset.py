"""Check that the expanded synthetic dataset is present without overwriting it."""
from pathlib import Path
import json

required = ("corpus.json", "queries.json")
for name in required:
    path = Path(name)
    if not path.is_file():
        raise FileNotFoundError(f"{name} is missing. Restore the supplied dataset before evaluation.")

corpus = json.loads(Path("corpus.json").read_text(encoding="utf-8"))
queries = json.loads(Path("queries.json").read_text(encoding="utf-8"))
assert len(corpus) >= 5
assert len([q for q in queries if q.get("doc") is not None]) >= 8
assert len([q for q in queries if q.get("doc") is None]) >= 2
print("Expanded corpus.json and queries.json are ready. Existing data was not overwritten.")
