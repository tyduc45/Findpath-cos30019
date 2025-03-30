from collections import deque

class BFS:
    def __init__(self, graph, origin, destinations):
        self.graph = graph
        self.origin = origin
        self.destinations = destinations
        self.path = None  # 只保存路径

    def bfs_calculate(self):
        visited = set()
        queue = deque()
        queue.append((self.origin, [self.origin]))  # (当前节点, 路径)

        while queue:
            current, path = queue.popleft()
            if current in visited:
                continue
            visited.add(current)

            if current in self.destinations:
                self.path = path
                return

            for neighbor in sorted(self.graph.get_neighbors(current)):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

        self.path = []  # 没找到路径

    def get_result(self):
        return self.path