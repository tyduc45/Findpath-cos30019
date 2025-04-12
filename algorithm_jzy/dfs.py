# Use AI to help learn the principles of this algorithm, but do not participate in the actual coding
# Written by Zhongyu Jiang, 105274347

class DFS:
    def __init__(self, graph, start, end):
        self.graph = graph
        self.start = start
        self.end = set(end)  # Convert to a set to speed up lookup
        self.path = []       # Current Path
        self.found = False
        self.nodes_expanded = 0
        self.goal_node = None  # The actual destination

    def dfs_calculate(self, node: int = None, visited: set = None):
        # If the target has been found, return directly to avoid unnecessary recursion
        if self.found:
            return

        if visited is None:
            visited = set()
        if node is None:
            node = self.start

        self.path.append(node)
        visited.add(node)
        self.nodes_expanded += 1

        # If the current node is one of the targets, it is marked successfully and returned
        if node in self.end:
            self.found = True
            self.goal_node = node
            return

        # Recursively traverse adjacent nodes
        for neighbor in sorted(self.graph.get_neighbors(node).keys()):
            if neighbor not in visited:
                self.dfs_calculate(neighbor, visited)
                if self.found:
                    return

        # Backtracking cleanup is performed only when the target is not found to ensure that the final path is not destroyed
        if not self.found:
            self.path.pop()

    def get_result(self):
        if not self.found:
            return "Unreachable", self.nodes_expanded, self.path
        return self.goal_node, self.nodes_expanded, self.path
