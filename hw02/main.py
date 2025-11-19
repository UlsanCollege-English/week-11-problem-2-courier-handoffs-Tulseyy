"""HW02 — Courier Handoffs (BFS Shortest Path)

Module placed under the `hw02` package so tests can import `hw02.main`.
"""

from collections import deque


def bfs_path(graph, s, t):
    """Return a shortest path (fewest edges) from s to t as a list of nodes.

    If s == t, return [s]. If s or t not in graph, return None.
    """
    # Input validation
    if graph is None:
        return None
    if s == t:
        return [s] if s in graph else None
    if s not in graph or t not in graph:
        return None

    queue = deque([s])
    visited = {s}
    parent = {s: None}

    while queue:
        node = queue.popleft()
        for nbr in graph.get(node, []):
            if nbr not in visited:
                visited.add(nbr)
                parent[nbr] = node
                if nbr == t:
                    # reconstruct path
                    path = [t]
                    cur = t
                    while parent[cur] is not None:
                        cur = parent[cur]
                        path.append(cur)
                    path.reverse()
                    return path
                queue.append(nbr)

    return None
