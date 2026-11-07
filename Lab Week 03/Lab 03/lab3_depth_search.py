"""Lab 3: Depth-Limited Search and Iterative Deepening DFS."""
GRAPH = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": [],
}

def dls(start, goal, limit, graph=GRAPH):
    """Return (status, path, processing_order). Uses a path-local cycle check."""
    order = []

    def visit(node, path, depth):
        order.append(node)
        if node == goal:
            return "FOUND", path
        if depth == limit:
            if any(child not in path for child in graph.get(node, [])):
                return "CUTOFF", None
            return "FAILURE", None

        saw_cutoff = False
        for child in graph.get(node, []):
            if child in path:
                continue
            status, result_path = visit(child, path + [child], depth + 1)
            if status == "FOUND":
                return status, result_path
            if status == "CUTOFF":
                saw_cutoff = True
        return ("CUTOFF", None) if saw_cutoff else ("FAILURE", None)

    status, path = visit(start, [start], 0)
    return status, path, order

def iddfs(start, goal, max_depth, graph=GRAPH):
    """Repeat DLS from depth zero; each iteration gets a fresh path-local check."""
    attempts = []
    for limit in range(max_depth + 1):
        status, path, order = dls(start, goal, limit, graph)
        attempts.append((limit, status, path, order))
        if status == "FOUND":
            return "FOUND", path, attempts
    final_status = attempts[-1][1] if attempts else "FAILURE"
    return final_status, None, attempts

if __name__ == "__main__":
    print("DLS results")
    for limit in (1, 2, 3, 4):
        status, path, order = dls("A", "G", limit)
        print(f"limit={limit} | status={status} | path={path} | processed={order}")

    print("\nIDDFS results")
    for maximum in (1, 2, 3, 4):
        status, path, attempts = iddfs("A", "G", maximum)
        tried = [f"{limit}:{result}" for limit, result, _, _ in attempts]
        print(f"max_depth={maximum} | status={status} | path={path} | attempts={tried}")
