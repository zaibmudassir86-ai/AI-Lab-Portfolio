import re
samples = ["AI, search!", "I can't log in.", "help@example.com", "CS4944", "", "یہ ایک مثال ہے"]
for text in samples:
    ws = text.split()
    words = re.findall(r"\b\w+\b", text, flags=re.UNICODE)
    print("Original:", repr(text))
    print("Whitespace tokens:", ws, "count:", len(ws))
    print("Word-like tokens:", words, "count:", len(words))
    print()
try:
    from transformers import AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
    print("Model subword comparison:")
    for text in samples[:2]:
        print(repr(text), tokenizer.tokenize(text))
except Exception as exc:
    print("Model tokenizer comparison unavailable:", type(exc).__name__, str(exc))
    print("Install sentence-transformers and allow the model tokenizer download to run this optional comparison.")
