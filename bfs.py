from collections import deque

class BFS:
    def __init__(self, graph, origin, destinations):
        self.graph = graph
        self.origin = origin
        self.destinations = destinations
        self.result = None  # (goal_node, expanded_count, path)

    def bfs_calculate(self):
        visited = set()
        queue = deque()
        queue.append((self.origin, [self.origin]))
        nodes_expanded = 0  # 用于统计被“扩展”的节点数量

        while queue:
            current, path = queue.popleft()
            if current in visited:
                continue
            visited.add(current)
            nodes_expanded += 1  # 每次真正扩展一个节点就 +1

            if current in self.destinations:
                self.result = (current, nodes_expanded, path)
                return

            for neighbor in sorted(self.graph.get_neighbors(current)):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

        self.result = (None, nodes_expanded, [])

    def get_result(self):
        return self.result

