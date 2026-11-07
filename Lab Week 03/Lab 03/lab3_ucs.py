"""Lab 3: Uniform-Cost Search on a documented weighted extension."""
import heapq
from itertools import count
from collections import deque

# Original corridors are retained. C -> G is the added corridor.
# All costs are nonnegative demonstration units.
WEIGHTED_GRAPH = {
    "A": [("B", 1), ("C", 5)],
    "B": [("D", 8), ("E", 1)],
    "C": [("F", 2), ("G", 7)],  # C -> G is the added corridor
    "D": [],
    "E": [("G", 1)],
    "F": [],
    "G": [],
}

def ucs(start, goal, graph=WEIGHTED_GRAPH):
    serial = count()
    frontier = [(0, next(serial), start, [start])]
    best_cost = {start: 0}
    processing_order = []
    while frontier:
        cost, _, node, path = heapq.heappop(frontier)
        if cost != best_cost.get(node):
            continue
        processing_order.append((node, cost))
        if node == goal:
            return path, cost, processing_order
        for nxt, edge_cost in graph.get(node, []):
            new_cost = cost + edge_cost
            if new_cost < best_cost.get(nxt, float("inf")):
                best_cost[nxt] = new_cost
                heapq.heappush(frontier, (new_cost, next(serial), nxt, path + [nxt]))
    return None, float("inf"), processing_order

def bfs_unweighted(start, goal, graph=WEIGHTED_GRAPH):
    """BFS ignores weights and minimizes edge count."""
    queue = deque([(start, [start])])
    seen = {start}
    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        for nxt, _ in graph.get(node, []):
            if nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, path + [nxt]))
    return None

def path_cost(path, graph=WEIGHTED_GRAPH):
    total = 0
    for a, b in zip(path, path[1:]):
        total += dict(graph[a])[b]
    return total

if __name__ == "__main__":
    path, cost, order = ucs("A", "G")
    bfs_path = bfs_unweighted("A", "G")
    print("Weighted edges:")
    for node, edges in WEIGHTED_GRAPH.items():
        for nxt, weight in edges:
            print(f"  {node} -> {nxt}: {weight}")
    print(f"\nUCS path: {' -> '.join(path)}")
    print(f"UCS total cost (algorithm): {cost}")
    print(f"UCS total cost (independent sum): {path_cost(path)}")
    print(f"UCS processing order: {order}")
    print(f"\nBFS path on same topology: {' -> '.join(bfs_path)}")
    print(f"BFS hop count: {len(bfs_path) - 1}")
    print(f"BFS weighted cost: {path_cost(bfs_path)}")
