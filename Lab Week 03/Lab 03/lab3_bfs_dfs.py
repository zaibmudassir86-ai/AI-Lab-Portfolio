"""Lab 3: BFS and DFS manual trace verification."""
from collections import deque

GRAPH = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": [],
}

def bfs(start, goal, graph=GRAPH):
    queue = deque([(start, [start])])
    seen = {start}
    order = []
    trace = []
    while queue:
        node, path = queue.popleft()
        order.append(node)
        if node == goal:
            trace.append((node, [item[0] for item in queue]))
            return path, order, trace
        for nxt in graph.get(node, []):
            if nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, path + [nxt]))
        trace.append((node, [item[0] for item in queue]))
    return None, order, trace

def dfs(start, goal, graph=GRAPH):
    stack = [(start, [start])]
    seen = set()
    order = []
    trace = []
    while stack:
        node, path = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        order.append(node)
        if node == goal:
            trace.append((node, [item[0] for item in stack]))
            return path, order, trace
        # Reverse insertion makes the first listed successor pop first.
        for nxt in reversed(graph.get(node, [])):
            if nxt not in seen:
                stack.append((nxt, path + [nxt]))
        trace.append((node, [item[0] for item in stack]))
    return None, order, trace

if __name__ == "__main__":
    for name, search in (("BFS", bfs), ("DFS", dfs)):
        path, order, trace = search("A", "G")
        print(f"{name} path: {' -> '.join(path) if path else 'Not found'}")
        print(f"{name} processing order: {', '.join(order)}")
        print(f"{name} frontier after each processed node:")
        for node, frontier in trace:
            print(f"  after {node}: {frontier}")
        print()
