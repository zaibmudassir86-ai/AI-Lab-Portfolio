import json
from task2_chunks import make_chunks
from lab6_search import Retriever
if __name__ == "__main__":
    with open("corpus.json", encoding="utf-8") as f:
        docs = json.load(f)
    backend = "tfidf"
    try:
        engine = Retriever(make_chunks(docs, "10"), backend)
    except Exception as exc:
        print("Could not start retrieval:", exc)
        raise SystemExit(1)
    print("Evidence assistant using TF-IDF with 40 word windows and 10 word overlap. Type exit to stop.")
    while True:
        try:
            query = input("Question: ")
        except (EOFError, KeyboardInterrupt):
            break
        if query.strip().lower() == "exit":
            break
        if not query.strip():
            print("Please enter a question.")
            continue
        hits = engine.search(query)
        if not hits:
            print("No candidate evidence; rephrase or contact a human.")
            continue
        print("Candidate evidence; relevance must be checked:")
        for number, (record, score) in enumerate(hits, 1):
            print(number, record["id"], f"{score:.3f}",
                  "characters", record["start"], record["end"])
        chosen = input("Choose 1 to 3 to inspect; Enter if none apply: ")
        if not chosen.isdigit() or not 1 <= int(chosen) <= len(hits):
            print("No answer selected. Rephrase or contact a human.")
            continue
        record, score = hits[int(chosen)-1]
        print("Retrieved passage:", record["text"])
        print("Source:", record["source"], "characters", record["start"], record["end"])
