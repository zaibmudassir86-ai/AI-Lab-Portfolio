"""Lab 3 edge cases for BFS, DFS, DLS, IDDFS and UCS. Run from this folder."""
from lab3_bfs_dfs import bfs, dfs
from lab3_depth_search import dls, iddfs
from lab3_ucs import ucs

# Start already equals goal.
assert bfs("G", "G")[0] == ["G"]
assert dfs("G", "G")[0] == ["G"]
assert dls("G", "G", 0)[0:2] == ("FOUND", ["G"])
assert iddfs("G", "G", 0)[0:2] == ("FOUND", ["G"])
assert ucs("G", "G")[0:2] == (["G"], 0)

# Unreachable goal.
disconnected = {"A": ["B"], "B": [], "X": []}
assert bfs("A", "X", disconnected)[0] is None
assert dfs("A", "X", disconnected)[0] is None
assert dls("A", "X", 3, disconnected)[0] == "FAILURE"
weighted_disconnected = {"A": [("B", 1)], "B": [], "X": []}
assert ucs("A", "X", weighted_disconnected)[0] is None

# Cycle must not trap the search.
cycle = {"A": ["B"], "B": ["A", "G"], "G": []}
assert bfs("A", "G", cycle)[0] == ["A", "B", "G"]
assert dfs("A", "G", cycle)[0] == ["A", "B", "G"]
assert dls("A", "G", 2, cycle)[0:2] == ("FOUND", ["A", "B", "G"])
print("Lab 3 edge cases passed: start=goal, unreachable goal, and cycle handling.")
