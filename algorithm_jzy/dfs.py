# Use AI to help learn the principles of this algorithm, but do not participate in the actual coding
class DFS:
    def __init__(self, graph, start, end):
        self.graph = graph
        self.start = start
        self.end = set(end)  # 转换为集合加速查找
        self.path = []       # 当前路径
        self.found = False   # 是否找到路径
        self.nodes_visited = 0
        self.goal_node = None  # 实际到达的目标点

    def dfs_calculate(self, node=None, visited=None):
        if visited is None:
            visited = set()
        if node is None:
            node = self.start

        self.path.append(node)
        visited.add(node)
        self.nodes_visited += 1

        if node in self.end:
            self.found = True
            self.goal_node = node
            return

        for neighbor in self.graph.get_neighbors(node):
            if neighbor not in visited and not self.found:
                self.dfs_calculate(neighbor, visited)
                if self.found:
                    return

        self.path.pop()
        visited.remove(node)

    def get_result(self):
        if not self.found:
            return None, self.nodes_visited, self.path
        return self.goal_node, self.nodes_visited, self.path,
