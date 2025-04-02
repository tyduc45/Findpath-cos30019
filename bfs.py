from collections import deque

class BFS:
    def __init__(self, graph, origin, destinations):
        self.graph = graph
        self.origin = origin
        self.destinations = destinations
        self.path = None

    def bfs_calculate(self):
        visited = set()
        queue = deque()
        queue.append((self.origin, [self.origin]))

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

        self.path = []

    def get_result(self):
        return self.path