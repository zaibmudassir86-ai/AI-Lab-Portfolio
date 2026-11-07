"""
Lab 5: Minimax and Alpha-Beta pruning with leaf counters.
The game tree is a complete binary tree. MAX moves at the root.
A leaf is counted only when its utility is actually evaluated.
"""

from math import ceil, log2, inf


def pad_scores(scores):
    if not scores:
        raise ValueError("At least one leaf score is required.")
    depth = ceil(log2(len(scores))) if len(scores) > 1 else 0
    padded = list(scores) + [0] * (2 ** depth - len(scores))
    return padded, depth


def minimax(depth, index, max_turn, scores, target_depth, counter):
    if depth == target_depth:
        counter["leaves"] += 1
        return scores[index]

    if max_turn:
        return max(
            minimax(depth + 1, index * 2, False, scores, target_depth, counter),
            minimax(depth + 1, index * 2 + 1, False, scores, target_depth, counter),
        )
    return min(
        minimax(depth + 1, index * 2, True, scores, target_depth, counter),
        minimax(depth + 1, index * 2 + 1, True, scores, target_depth, counter),
    )


def alphabeta(depth, index, max_turn, scores, target_depth, alpha, beta, counter):
    if depth == target_depth:
        counter["leaves"] += 1
        return scores[index]

    if max_turn:
        value = -inf
        for child in (0, 1):
            value = max(
                value,
                alphabeta(
                    depth + 1, index * 2 + child, False,
                    scores, target_depth, alpha, beta, counter
                ),
            )
            alpha = max(alpha, value)
            if alpha >= beta:
                counter["cutoffs"] += 1
                break
        return value

    value = inf
    for child in (0, 1):
        value = min(
            value,
            alphabeta(
                depth + 1, index * 2 + child, True,
                scores, target_depth, alpha, beta, counter
            ),
        )
        beta = min(beta, value)
        if alpha >= beta:
            counter["cutoffs"] += 1
            break
    return value


def evaluate(scores, reverse_children=False):
    padded, depth = pad_scores(scores)
    if reverse_children:
        # Reverse sibling order at every internal level without changing
        # the tree's underlying minimax values.
        def reverse_at_level(values, level):
            if level == depth:
                return values
            block = 2 ** (depth - level)
            half = block // 2
            result = []
            for start in range(0, len(values), block):
                left = values[start:start + half]
                right = values[start + half:start + block]
                result.extend(reverse_at_level(right, level + 1))
                result.extend(reverse_at_level(left, level + 1))
            return result
        padded = reverse_at_level(padded, 0)

    mm_count = {"leaves": 0}
    ab_count = {"leaves": 0, "cutoffs": 0}
    mm_value = minimax(0, 0, True, padded, depth, mm_count)
    ab_value = alphabeta(0, 0, True, padded, depth, -inf, inf, ab_count)
    return {
        "padded": padded,
        "depth": depth,
        "minimax_value": mm_value,
        "minimax_leaves": mm_count["leaves"],
        "alphabeta_value": ab_value,
        "alphabeta_leaves": ab_count["leaves"],
        "cutoffs": ab_count["cutoffs"],
    }


def main():
    supplied = [3, 5, 2, 9, 0, 7]
    original = evaluate(supplied)
    reversed_order = evaluate(supplied, reverse_children=True)

    print("SUPPLIED TREE")
    print("Input leaf scores:", supplied)
    print("Padded leaf scores:", original["padded"])
    print("Tree depth:", original["depth"])
    print("Minimax root value:", original["minimax_value"])
    print("Minimax evaluated leaves:", original["minimax_leaves"])
    print("Alpha-Beta root value:", original["alphabeta_value"])
    print("Alpha-Beta evaluated leaves:", original["alphabeta_leaves"])
    print("Alpha-Beta cutoffs:", original["cutoffs"])

    print("\nREVERSED SIBLING ORDER")
    print("Reordered leaf scores:", reversed_order["padded"])
    print("Minimax root value:", reversed_order["minimax_value"])
    print("Minimax evaluated leaves:", reversed_order["minimax_leaves"])
    print("Alpha-Beta root value:", reversed_order["alphabeta_value"])
    print("Alpha-Beta evaluated leaves:", reversed_order["alphabeta_leaves"])
    print("Alpha-Beta cutoffs:", reversed_order["cutoffs"])

    print("\nEDGE CASES")
    one_leaf = evaluate([7])
    print("Single leaf, root value:", one_leaf["minimax_value"],
          "Minimax leaves:", one_leaf["minimax_leaves"],
          "Alpha-Beta leaves:", one_leaf["alphabeta_leaves"])
    equal_leaves = evaluate([4, 4, 4, 4])
    print("Equal leaves, root values:", equal_leaves["minimax_value"],
          equal_leaves["alphabeta_value"],
          "evaluated leaves:", equal_leaves["minimax_leaves"],
          equal_leaves["alphabeta_leaves"])


if __name__ == "__main__":
    main()
