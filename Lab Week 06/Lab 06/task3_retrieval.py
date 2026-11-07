import csv, json, time
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from task2_chunks import make_chunks

def metrics(score_rows, chunks, items):
    hits, reciprocal = [], []
    for row, query in zip(score_rows, items):
        if query["doc"] is None:
            continue
        top = np.argsort(-row, kind="stable")[:3]
        good = [rank for rank, index in enumerate(top, 1)
                if chunks[index]["doc"] == query["doc"]
                and query["evidence"] in chunks[index]["text"]]
        hits.append(bool(good))
        reciprocal.append(1 / good[0] if good else 0)
    if not hits:
        return None, None
    return float(np.mean(hits)), float(np.mean(reciprocal))

def main():
    with open("corpus.json", encoding="utf-8") as f:
        docs = json.load(f)
    with open("queries.json", encoding="utf-8") as f:
        items = json.load(f)
    assert len(docs) >= 5 and len([q for q in items if q["doc"]]) >= 8
    for q in items:
        assert q["split"] in {"dev", "test"}
        if q["doc"] is not None:
            assert q["evidence"] in docs[q["doc"]]
    logs, summary = [], []
    for strategy in ["0", "10", "sentence"]:
        chunks = make_chunks(docs, strategy)
        texts = [c["text"] for c in chunks]
        for method in ["tfidf", "embedding"]:
            if method == "tfidf":
                t = time.perf_counter()
                vectorizer = TfidfVectorizer()
                C = vectorizer.fit_transform(texts)
                Q = vectorizer.transform([q["query"] for q in items])
                encode_seconds = time.perf_counter() - t
                t = time.perf_counter()
                score_matrix = (Q @ C.T).toarray()
                search_seconds = time.perf_counter() - t
            else:
                try:
                    from sentence_transformers import SentenceTransformer
                    t = time.perf_counter()
                    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", device="cpu")
                    model_load_seconds = time.perf_counter() - t
                    all_text = texts + [q["query"] for q in items]
                    token_lengths = [len(model.tokenizer(x, truncation=False)["input_ids"]) for x in all_text]
                    if max(token_lengths) > model.max_seq_length:
                        raise ValueError("Model token limit exceeded")
                    t = time.perf_counter()
                    C = model.encode(texts, normalize_embeddings=True)
                    Q = model.encode([q["query"] for q in items], normalize_embeddings=True)
                    encode_seconds = time.perf_counter() - t
                    t = time.perf_counter()
                    score_matrix = Q @ C.T
                    search_seconds = time.perf_counter() - t
                except Exception as exc:
                    summary.append({"strategy":strategy,"method":"embedding","split":"not_run",
                                    "hit_at_3":"","mrr_at_3":"","chunks":len(chunks),
                                    "encode_seconds":"","search_seconds":"",
                                    "model_load_seconds":"","status":f"NOT RUN: {type(exc).__name__}: {exc}"})
                    print(strategy, "embedding NOT RUN:", type(exc).__name__, exc)
                    continue
            for split in ["dev", "test"]:
                indices = [i for i,q in enumerate(items) if q["split"] == split and q["doc"] is not None]
                hit, mrr = metrics(score_matrix[indices], chunks, [items[i] for i in indices])
                summary.append({"strategy":strategy,"method":method,"split":split,
                                "hit_at_3":hit,"mrr_at_3":mrr,"chunks":len(chunks),
                                "encode_seconds":encode_seconds,"search_seconds":search_seconds,
                                "model_load_seconds":"not applicable" if method=="tfidf" else model_load_seconds,
                                "status":"COMPLETED"})
                print(strategy, method, split, f"Hit@3={hit:.3f}", f"MRR@3={mrr:.3f}",
                      "chunks",len(chunks),"encode/index",f"{encode_seconds:.6f}s",
                      "search",f"{search_seconds:.6f}s")
            for row, q in zip(score_matrix, items):
                for rank, index in enumerate(np.argsort(-row, kind="stable")[:3], 1):
                    c = chunks[index]
                    logs.append({"strategy":strategy,"method":method,"query":q["query"],
                                 "split":q["split"],"rank":rank,"score":float(row[index]),
                                 "chunk_id":c["id"],"doc":c["doc"],"source":c["source"],
                                 "start":c["start"],"end":c["end"],"text":c["text"],
                                 "answerable":q["doc"] is not None,
                                 "evidence_complete":bool(q["doc"] is not None and c["doc"]==q["doc"] and q["evidence"] in c["text"])})
    if logs:
        with open("retrieval_log.csv","w",newline="",encoding="utf-8") as f:
            writer=csv.DictWriter(f,fieldnames=list(logs[0])); writer.writeheader(); writer.writerows(logs)
    with open("retrieval_summary.csv","w",newline="",encoding="utf-8") as f:
        writer=csv.DictWriter(f,fieldnames=list(summary[0])); writer.writeheader(); writer.writerows(summary)
    print("Wrote retrieval_log.csv and retrieval_summary.csv")
    print("Unanswerable queries are logged in top-three results but excluded from Hit@3 and MRR@3.")
if __name__ == "__main__":
    main()
