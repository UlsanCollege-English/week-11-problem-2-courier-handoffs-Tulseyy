
## main.py
```python
"""
HW02 — Courier Handoffs (BFS Shortest Path)

Implement:
- bfs_path(graph, s, t)
"""

from collections import deque

def bfs_path(graph, s, t):
    """Return a shortest path (fewest edges) from s to t as a list of nodes.

    If s == t, return [s]. If s or t not in graph, return None.

    TODO (8 Steps):
    1) Read & Understand: what is "fewest handoffs" here?
    2) Re-phrase: say the goal in simple words.
    3) Identify I/O: inputs graph, s, t; output list or None.
    4) Break down: queue, visited, parent; loop until found.
    5) Pseudocode: write steps as comments above your code.
    6) Write code with deque.
    7) Debug with prints (locally).
    8) Optimize: state O(V+E) in README.
    """
    # Pseudocode:
    # 1. Validate inputs: s and t must be in graph. If equal, return [s].
    # 2. Use a deque for BFS queue. Track visited set and parent map.
    # 3. Standard BFS: pop node, check neighbors, mark visited and set parent.
    # 4. Stop when we find t. If found, reconstruct path from t to s via parent.
    # 5. If BFS completes without finding t, return None.

    # Input validation
    if graph is None:
        return None
    if s == t:
        # If s equals t, ensure node exists in graph per spec
        return [s] if s in graph else None
    if s not in graph or t not in graph:
        return None

    queue = deque([s])
    visited = {s}
    parent = {s: None}

    while queue:
        node = queue.popleft()
        # iterate neighbors (graph is expected to be a mapping node -> iterable of neighbors)
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

    # t not reachable from s
    return None
