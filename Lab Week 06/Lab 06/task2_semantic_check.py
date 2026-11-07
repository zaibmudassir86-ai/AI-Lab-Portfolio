from task2_chunks import make_chunks
from lab6_search import Retriever, show_hits
texts = {"it": "A forgotten password can be reset using the recovery link.",
         "assessment": "Assignments are uploaded through the learning portal."}
records = make_chunks(texts, "sentence")
for backend in ["tfidf", "embedding"]:
    print("Backend:", backend)
    try:
        engine = Retriever(records, backend)
    except RuntimeError as exc:
        print("NOT RUN:", exc)
        continue
    show_hits(engine.search("How can I regain access to my account?", k=2))
