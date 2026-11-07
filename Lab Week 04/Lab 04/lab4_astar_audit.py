"""
Lab 4: A* heuristic audit, UCS control, and overestimate experiment.

Priority order is (f, g, node, path), using Python heapq tuple ordering.
A node is counted as expanded only when its successors are examined.
The goal is logged as processed but is not counted as expanded.
"""
import heapq
from math import inf

GRAPH = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": [],
}

SUPPLIED_H = {"S": 5, "A": 4, "B": 4, "C": 2, "G": 0}


def search(graph, heuristic, start, goal):
    if start not in graph:
        raise ValueError(f"Unknown start node: {start}")
    if goal not in graph:
        raise ValueError(f"Unknown goal node: {goal}")

    frontier = [(heuristic.get(start, 0), 0, start, [start])]
    best_g = {start: 0}
    processed = []
    expanded = []
    stale_skips = []

    while frontier:
        f, g, node, path = heapq.heappop(frontier)

        if g != best_g.get(node, inf):
            stale_skips.append((node, g, best_g.get(node)))
            continue

        processed.append((node, g, heuristic.get(node, 0), f))
        if node == goal:
            return {
                "path": path,
                "cost": g,
                "processed": processed,
                "expanded": expanded,
                "expansion_count": len(expanded),
                "stale_skips": stale_skips,
                "status": "FOUND",
            }

        expanded.append(node)
        for nxt, weight in graph.get(node, []):
            new_g = g + weight
            if new_g < best_g.get(nxt, inf):
                best_g[nxt] = new_g
                new_f = new_g + heuristic.get(nxt, 0)
                heapq.heappush(frontier, (new_f, new_g, nxt, path + [nxt]))

    return {
        "path": None,
        "cost": inf,
        "processed": processed,
        "expanded": expanded,
        "expansion_count": len(expanded),
        "stale_skips": stale_skips,
        "status": "FAILURE",
    }


def path_cost(graph, path):
    if not path:
        return None
    total = 0
    for u, v in zip(path, path[1:]):
        matches = [w for nxt, w in graph.get(u, []) if nxt == v]
        if not matches:
            raise ValueError(f"No edge {u} -> {v}")
        total += matches[0]
    return total


def show_result(label, result, graph):
    print(f"\n{label}")
    print("Status:", result["status"])
    print("Path:", " -> ".join(result["path"]) if result["path"] else "None")
    print("Returned cost:", result["cost"])
    print("Independently summed cost:", path_cost(graph, result["path"]))
    print("Processed trace (node, g, h, f):", result["processed"])
    print("Expanded nodes:", result["expanded"])
    print("Expansion count:", result["expansion_count"])
    print("Stale entries skipped:", result["stale_skips"])


def main():
    astar = search(GRAPH, SUPPLIED_H, "S", "G")
    ucs = search(GRAPH, {node: 0 for node in GRAPH}, "S", "G")

    overestimated_h = dict(SUPPLIED_H)
    overestimated_h["C"] = 10
    over = search(GRAPH, overestimated_h, "S", "G")

    show_result("A* with supplied heuristic", astar, GRAPH)
    show_result("UCS control (h = 0)", ucs, GRAPH)
    show_result("A* with overestimate h(C) = 10", over, GRAPH)

    print("\nHeuristic audit")
    true_remaining = {"S": 6, "A": 5, "B": 5, "C": 3, "G": 0}
    for node in GRAPH:
        h = SUPPLIED_H[node]
        print(f"{node}: h={h}, true remaining={true_remaining[node]}, admissible={h <= true_remaining[node]}")
    consistency_checks = []
    for node, edges in GRAPH.items():
        for nxt, weight in edges:
            ok = SUPPLIED_H[node] <= weight + SUPPLIED_H[nxt]
            consistency_checks.append(ok)
            print(f"{node}->{nxt}: {SUPPLIED_H[node]} <= {weight} + {SUPPLIED_H[nxt]} : {ok}")
    print("All supplied edge consistency checks pass:", all(consistency_checks))

    print("\nEdge case: start equals goal")
    same = search(GRAPH, SUPPLIED_H, "S", "S")
    show_result("A* start=goal", same, GRAPH)

    print("\nEdge case: unreachable goal")
    disconnected = {"S": [("A", 1)], "A": [], "G": []}
    unreachable = search(disconnected, {"S": 0, "A": 0, "G": 0}, "S", "G")
    show_result("UCS unreachable goal", unreachable, disconnected)


if __name__ == "__main__":
    main()
