# Lab 1: Transparent Scholarship Screening Rules
# Student Name: Syed Mudassir Zaib
# Roll Number: SU92-BSAIM-F25-232

# All thresholds and conditions below are synthetic lab assumptions.
# "Review" means send the application to a human reviewer, not award a scholarship.

SCORE_THRESHOLD = 70


def scholarship_decision(
    score,
    documents_complete,
    income_documents_verified,
    recommendation_received,
):
    conditions = {
        "score_at_least_70": score >= SCORE_THRESHOLD,
        "documents_complete": documents_complete,
        "income_documents_verified": income_documents_verified,
        "recommendation_received": recommendation_received,
    }

    decision = "Review" if all(conditions.values()) else "Hold"
    return decision, conditions


test_cases = [
    {
        "name": "pass_all_conditions",
        "score": 82,
        "documents_complete": True,
        "income_documents_verified": True,
        "recommendation_received": True,
        "expected": "Review",
    },
    {
        "name": "fail_income_verification",
        "score": 82,
        "documents_complete": True,
        "income_documents_verified": False,
        "recommendation_received": True,
        "expected": "Hold",
    },
    {
        "name": "fail_recommendation_condition",
        "score": 82,
        "documents_complete": True,
        "income_documents_verified": True,
        "recommendation_received": False,
        "expected": "Hold",
    },
    {
        "name": "threshold_boundary_score_70",
        "score": 70,
        "documents_complete": True,
        "income_documents_verified": True,
        "recommendation_received": True,
        "expected": "Review",
    },
]


print("Scholarship screening rule tests")
print("All thresholds are synthetic lab assumptions.")
print()

for case in test_cases:
    actual, conditions = scholarship_decision(
        case["score"],
        case["documents_complete"],
        case["income_documents_verified"],
        case["recommendation_received"],
    )
    passed = actual == case["expected"]

    print(f"Case: {case['name']}")
    print(
        "Input: "
        f"score={case['score']}, "
        f"documents_complete={case['documents_complete']}, "
        f"income_documents_verified={case['income_documents_verified']}, "
        f"recommendation_received={case['recommendation_received']}"
    )
    print(f"Expected result: {case['expected']}")
    print(f"Actual result:   {actual}")
    print("Reason:")
    for condition_name, condition_value in conditions.items():
        print(f"  {condition_name}: {condition_value}")
    print(f"Test passed: {passed}")
    print()
