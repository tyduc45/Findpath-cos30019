# Use AI to help learn the principles of this algorithm, but do not participate in the actual coding
# Written by Zhongyu Jiang, 105274347

class DFS:
    def __init__(self, graph, start, end):
        self.graph = graph
        self.start = start
        self.end = set(end)
        self.path = []
        self.found = False
        self.nodes_expanded = 0
        self.goal_node = None

    def dfs_calculate(self):
        stack = [(self.start, [self.start], {self.start})]  # (current_node, path, visited_set)

        while stack:
            current_node, path, visited = stack.pop()
            self.nodes_expanded += 1

            if current_node in self.end:
                self.found = True
                self.goal_node = current_node
                self.path = path
                return

            for neighbor in sorted(self.graph.get_neighbors(current_node).keys(), reverse=True):
                if neighbor not in visited:
                    new_visited = visited.copy()
                    new_visited.add(neighbor)
                    stack.append((neighbor, path + [neighbor], new_visited))

    def get_result(self):
        if not self.found:
            return "Unreachable", self.nodes_expanded, self.path
        return self.goal_node, self.nodes_expanded, self.path
