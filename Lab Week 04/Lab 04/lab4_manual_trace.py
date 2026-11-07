"""
Lab 4: Reproducible manual frontier audit for supplied A* graph.
"""
from lab4_astar_audit import GRAPH, SUPPLIED_H

def frontier_after_expansion(start, goal, graph, h, expansions_to_show=3):
    import heapq
    pq = [(h[start], 0, start, [start])]
    best = {start: 0}
    for step in range(1, expansions_to_show + 1):
        f, g, node, path = heapq.heappop(pq)
        print(f"Expansion {step}: selected {node}, g={g}, h={h[node]}, f={f}")
        for nxt, w in graph[node]:
            ng = g + w
            if ng < best.get(nxt, float("inf")):
                best[nxt] = ng
                heapq.heappush(pq, (ng + h[nxt], ng, nxt, path + [nxt]))
        print("Frontier:", [(item[2], item[1], h[item[2]], item[0]) for item in sorted(pq)])

if __name__ == "__main__":
    frontier_after_expansion("S", "G", GRAPH, SUPPLIED_H)
