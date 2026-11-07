# Lab 1: Rule-Based vs Probability-Based Comparison
# Student Name: Syed Mudassir Zaib
# Roll Number: SU92-BSAIM-F25-232

def rule_based(score, documents_complete):
    return "Review" if documents_complete and score >= 70 else "Hold"


def probability_based(probability):
    return "Review" if probability >= 0.70 else "Hold"


print("Original comparison")
print("Rule-based:", rule_based(76, True))
print("Probability-based:", probability_based(0.76))


def symbolic(score, complete):
    return "Review" if complete and score >= 70 else "Hold"


def threshold(probability):
    return "Review" if probability >= 0.70 else "Hold"


cases = [
    ("complete_high", 82, True, 0.81),
    ("complete_low", 68, True, 0.74),
    ("incomplete_high", 91, False, 0.88),
    ("boundary", 70, True, 0.70),
]

print("\ncase | symbolic | threshold | disagreement")
for name, score, complete, probability in cases:
    symbolic_result = symbolic(score, complete)
    threshold_result = threshold(probability)
    print(name, symbolic_result, threshold_result,
          symbolic_result != threshold_result, sep=" | ")
