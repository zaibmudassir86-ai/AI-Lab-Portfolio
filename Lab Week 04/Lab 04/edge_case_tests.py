"""Lab 4 A* regression tests. Run from this folder."""
from lab4_astar_audit import GRAPH, SUPPLIED_H, search, path_cost

normal = search(GRAPH, SUPPLIED_H, "S", "G")
assert normal["status"] == "FOUND"
assert normal["path"] == ["S", "A", "C", "G"]
assert normal["cost"] == path_cost(GRAPH, normal["path"]) == 6

same = search(GRAPH, SUPPLIED_H, "S", "S")
assert same["path"] == ["S"] and same["cost"] == 0

disconnected = {"S": [("A", 1)], "A": [], "G": []}
unreachable = search(disconnected, {"S":0,"A":0,"G":0}, "S", "G")
assert unreachable["status"] == "FAILURE" and unreachable["path"] is None

over_h = dict(SUPPLIED_H)
over_h["C"] = 10
over = search(GRAPH, over_h, "S", "G")
assert over["path"] == ["S", "B", "G"] and over["cost"] == 9

try:
    search(GRAPH, SUPPLIED_H, "UNKNOWN", "G")
except ValueError:
    pass
else:
    raise AssertionError("Unknown start node should be rejected")
print("Lab 4 edge cases passed: optimal path, start=goal, unreachable goal, overestimate and invalid node.")
