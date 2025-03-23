# Use AI to help learn the principles of this algorithm, but do not participate in the actual coding
from Infrastructure.Min_Heap import MinHeap

class GBFS:
    def __init__(self, graph, start, ends):
        self.graph = graph
        self.start = start
        self.ends = set(ends)  # Convert end nodes to a set for faster lookup
        self.heap = MinHeap()
        self.came_from = {}  # Store the path
        self.end = None  # Mark the destination node once found

    def gbfs_calculate(self):
        # Initialize the heap with the start node and an initial cost of 0
        self.heap.push((0, self.start))
        self.came_from[self.start] = None

        while len(self.heap) > 0:
            current_cost, current_node = self.heap.pop()

            # If the current node is one of the target nodes
            if current_node in self.ends:
                self.end = current_node
                return True

            # For each neighbor not yet visited
            for neighbor, cost in self.graph.get_neighbors(current_node).items():
                if neighbor not in self.came_from:
                    self.came_from[neighbor] = current_node

                    # Estimate cost using a simple heuristic to the closest end node
                    heuristic_cost = min(
                        [self.graph.get_edge_weight(neighbor, end) or float('inf') for end in self.ends]
                    )
                    total_cost = current_cost + cost
                    self.heap.push((heuristic_cost + total_cost, neighbor))

        # If no path was found
        return False

    def get_result(self):
        # Reconstruct the path from end to start using came_from
        path = []
        step = self.end
        while step is not None:
            path.append(step)
            step = self.came_from.get(step)

        path.reverse()  # Return path from start to end
        return path
