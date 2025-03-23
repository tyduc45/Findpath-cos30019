# Use AI to help learn the principles of this algorithm, but do not participate in the actual coding
class DFS:
    def __init__(self, graph, start, end):
        self.graph = graph
        self.start = start
        self.end = end
        self.path = []  # Store current path
        self.found = False  # Mark whether the path is found

    def dfs_calculate(self, node=None, visited=None):
        if visited is None:
            visited = set()
        if node is None:
            node = self.start

        # Add the current node to the path
        self.path.append(node)
        visited.add(node)

        # If the current node is one of the target nodes
        if node in self.end:
            self.found = True
            return

        # For each neighbor, if not visited, recursively search
        for neighbor in self.graph.get_neighbors(node):
            if neighbor not in visited and not self.found:
                self.dfs_calculate(neighbor, visited)
                if self.found:
                    return

        # If the destination cannot be reached from the current node, backtrack
        self.path.pop()
        visited.remove(node)

    def get_result(self):
        if not self.path or not self.found:
            return "No path found"
        return self.path
