"""Lab 5 Minimax and Alpha-Beta edge-case checks."""
from lab5_minimax_alphabeta import evaluate, pad_scores

base = evaluate([3, 5, 2, 9, 0, 7])
reordered = evaluate([3, 5, 2, 9, 0, 7], reverse_children=True)
assert base["minimax_value"] == base["alphabeta_value"]
assert reordered["minimax_value"] == reordered["alphabeta_value"]
assert base["minimax_value"] == reordered["minimax_value"]
assert base["minimax_leaves"] == 8
assert base["alphabeta_leaves"] <= base["minimax_leaves"]
assert reordered["alphabeta_leaves"] <= reordered["minimax_leaves"]

one = evaluate([7])
assert one["minimax_value"] == one["alphabeta_value"] == 7
assert one["minimax_leaves"] == one["alphabeta_leaves"] == 1

try:
    pad_scores([])
except ValueError:
    pass
else:
    raise AssertionError("Empty leaf list should be rejected")
print("Lab 5 edge cases passed: matching values, reordered branches, one leaf and empty input.")
