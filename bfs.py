from collections import deque
from data import graph


def bfs(graph, start, goal):
    queue = deque([start])
    visited = []
    visited_set = set([start])
    parents = {start: None}

    while queue:
        current_node = queue.popleft()
        visited.append(current_node)

        if current_node == goal:
            break

        for children in graph[current_node]:
            if children not in visited_set:
                queue.append(children)
                visited_set.add(children)
                if children not in parents:
                    parents[children] = current_node

    if goal in parents:
        path = []
        while goal:
            path.append(goal)
            goal = parents[goal]

        path.reverse()
        return path, visited

    else:
        return None, visited


