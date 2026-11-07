from guided_chatbot import build_bot

try:
    engine = build_bot("embedding")
except RuntimeError as exc:
    print("NOT RUN:", exc)
    print("Install the packages in requirements.txt and allow the model download, then run this script again.")
else:
    query = "assignment upload"
    print("Suggested questions:")
    for record, score in engine.search(query, k=3):
        if score > 0:
            print(record["question"], f"({score:.3f})")
