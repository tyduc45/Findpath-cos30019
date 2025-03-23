# Astar.py -- A* Search Algorithm using Custom MinHeap
# ----------------------------------------------------------------------------------------
# This module implements the A* search algorithm for finding the shortest path in a graph.
# The algorithm uses a custom MinHeap as a priority queue, ensuring that nodes with
# the lowest total cost `f(n) = g(n) + h(n)` are expanded first.
#
# Implemented Features:
# 1. `search()`: Runs the A* algorithm to find the shortest path.
# 2. `heuristic(node, goal)`: Computes the heuristic function `h(n)`.
# 3. `abs_val(x)`: Computes the absolute value without using the math module.
# 4. `sqrt(n)`: Computes the square root using Newton's method.
# 5. Tie-breaking rule: If multiple paths have the same cost, the path with
#    the lexicographically smallest sequence of nodes is chosen.
# 6. `Counter`: Custom counter to replace `itertools.count()` for unique ordering.
#
# This implementation works with the `Graph` class, where nodes are connected by weighted edges.
# It ensures that when paths have the same cost, paths with numerically smaller nodes are preferred.
#
# In This Code, AI HAS BEEN USED TO HELP AND STUDY WHAT IS A* ALGORITHM.
#
# ----------------------------------------------------------------------------------------
# Written by Xiaonan Li, 105206175
# Date: 23/03/2025
#

from Infrastructure.Min_Heap import MinHeap
from Infrastructure.Itertools import Counter

class Astar:
    # Initialize A* search parameters.
    # param graph: Graph instance
    # param start: Start node
    # param destinations: List of possible goal nodes
    def __init__(self, graph, start, destinations):
        self.graph = graph
        self.start = start
        self.destinations = destinations
        # Select the nearest goal using the heuristic function
        self.goal = min(destinations, key=lambda d: self.heuristic(start, d))
        # Unique counter for tie-breaking using our custom Counter
        self.tiebreaker = Counter()

    # Returns the absolute value of a number
    def abs_val(self, x):
        return x if x >= 0 else -x

    # Compute heuristic h(n).
    # For numeric nodes, use absolute difference.
    # If nodes are coordinates (tuple), use Euclidean distance.
    def heuristic(self, node, goal):
        if isinstance(node, tuple):
            x1, y1 = node
            x2, y2 = goal
            return self.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        return self.abs_val(node - goal)

    # Compute the square root using Newton's method.
    def sqrt(self, n, precision=1e-10):
        if n < 0:
            raise ValueError("Cannot compute square root of a negative number")
        if n == 0:
            return 0
        x = n  # Initial guess
        while self.abs_val(x * x - n) > precision:
            x = (x + n / x) / 2
        return x

    # A* search algorithm that finds the shortest path from start to goal.
    # When paths have the same total cost, the path with lexicographically smaller node sequence is chosen.
    # return: List of nodes representing the shortest path, or None if no path is found.
    def search(self):
        heap = MinHeap()
        # Push initial node:
        # f = 0, g = 0, path_tuple = empty tuple, tie = next counter, node = start, path = empty list
        heap.push((0, 0, tuple([]), self.tiebreaker.next(), self.start, []))

        # Dictionary to store the best g(n) for each node
        g_costs = {self.start: 0}

        while len(heap) > 0:
            # Pop the node with smallest f; tie-breaker ensures that if f and g are same, lex order of path is used,
            # and if still equal, the insertion order is used.
            f, g, path_tuple, tie, node, path = heap.pop()
            new_path = path + [node]  # Create a new path list

            # If current node is a goal, return the path
            if node in self.destinations:
                return new_path

            # Expand neighbors
            for neighbor, cost in self.graph.get_neighbors(node).items():
                new_g = g + cost  # Cost from start to neighbor via current node
                # Only consider this neighbor if we found a better path to it
                if neighbor not in g_costs or new_g < g_costs[neighbor]:
                    g_costs[neighbor] = new_g
                    new_f = new_g + self.heuristic(neighbor, self.goal)
                    new_path_tuple = tuple(new_path + [neighbor])  # For lexicographical tie-breaking
                    heap.push((new_f, new_g, new_path_tuple, self.tiebreaker.next(), neighbor, new_path))

        # No path found
        return None