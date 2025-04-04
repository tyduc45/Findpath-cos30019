# Use AI to help learn the principles of this algorithm, but do not participate in the actual coding
# Written by Zhongyu Jiang, 105274347

from Infrastructure.Min_Heap import MinHeap

class GBFS:
    def __init__(self, graph, start: int, ends: list):
        self.graph = graph
        self.start = start
        self.ends = set(ends)  # Convert to a set to speed up lookup
        self.heap = MinHeap()
        self.came_from = {}  # Record the predecessor of each node
        self.nodes_expanded = 0  # Record the number of visited (expanded) nodes
        self.end = None

    def gbfs_calculate(self) -> bool:
        # Use MinHeap to search nodes sorted by heuristic value until any target node is found.
        # Returns True if the target node is found, otherwise returns False.
        self.heap.push((0, self.start))
        self.came_from[self.start] = None

        while self.heap:
            current_cost, current_node = self.heap.pop()
            self.nodes_expanded += 1

            if current_node in self.ends:
                self.end = current_node
                return True

            for neighbor, cost in self.graph.get_neighbors(current_node).items():
                if neighbor not in self.came_from:
                    self.came_from[neighbor] = current_node
                    self.heap.push((cost, neighbor))  # Use only cost for heuristic sorting

        return False

    def get_result(self):
        if self.end is None:
            return None, None, self.nodes_expanded

        path = []
        step = self.end
        while step is not None:
            path.append(step)
            step = self.came_from.get(step)
        path.reverse()

        return self.end, self.nodes_expanded, path
