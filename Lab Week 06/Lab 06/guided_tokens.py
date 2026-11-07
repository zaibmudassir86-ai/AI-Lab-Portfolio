import re
samples = [
    "AI, search!",
    "I can't log in.",
    "help@example.com",
    "CS4944",
    "",
    "یہ ایک مثال ہے",
    "2.1 version 4944CS"
]
for text in samples:
    whitespace = text.split()
    word_like = re.findall(r"\b\w+\b", text, flags=re.UNICODE)
    print("Original:", repr(text))
    print("Whitespace:", whitespace, len(whitespace))
    print("Word-like:", word_like, len(word_like))
    print()
