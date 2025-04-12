# Use AI to help learn the principles of this algorithm, but do not participate in the actual coding
# Written by Zhongyu Jiang, 105274347

from Infrastructure.Min_Heap import MinHeap

class GBFS:
    def __init__(self, graph, start: int, ends: list):
        self.graph = graph
        self.start = start
        self.ends = set(ends)
        self.goal = self.select_goal()
        self.heap = MinHeap()
        self.came_from = {}
        self.nodes_expanded = 0
        self.end = None

    def euclidean_distance(self, node1, node2):
        # Calculate the Euclidean distance between two nodes (as a heuristic function)
        x1, y1 = self.graph.get_coordinates(node1)
        x2, y2 = self.graph.get_coordinates(node2)
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5  # Calculate Euclidean distance

    def select_goal(self):
        # Select the target node closest to the starting point
        x0, y0 = self.graph.get_coordinates(self.start)
        min_goal = None
        min_dist = float("inf")
        for end in self.ends:
            x1, y1 = self.graph.get_coordinates(end)
            dist = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
            if dist < min_dist:
                min_dist = dist
                min_goal = end
        return min_goal

    def gbfs_calculate(self) -> bool:
        self.heap.push((0, self.start)) # Initial point into the heap, heuristic value is set to 0
        self.came_from[self.start] = None

        while self.heap:
            # Pop the node with the smallest heuristic value from the heap
            _, current = self.heap.pop()
            self.nodes_expanded += 1

            if current == self.goal:
                self.end = current
                return True

            # Traverse all neighbors of the current node
            for neighbor in sorted(self.graph.get_neighbors(current)):
                if neighbor not in self.came_from:
                    self.came_from[neighbor] = current
                    heuristic = self.euclidean_distance(neighbor, self.goal)
                    self.heap.push((heuristic, neighbor)) # Use heuristic value to push into the heap

        return False

    def get_result(self):
        if self.end is None:
            return "Unreachable", self.nodes_expanded, None

        path = []
        node = self.end
        while node is not None:
            path.append(node)
            node = self.came_from[node]
        path.reverse()
        return self.end, self.nodes_expanded, path
