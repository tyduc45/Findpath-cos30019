# Dev_Test.py -- A Testing program during development
# ----------------------------------------------------------------------------------------
# This script is a development testing program that simulates the control file
# for calling the `Graph` class. It is used to verify that the graph parsing
# works correctly before integrating it with search algorithms.
#
# Functionality:
# 1. Calls the `Graph` class to parse `test_map.txt`.
# 2. Retrieves and prints:
#    - Graph structure (nodes and edges)
#    - Origin node (starting point)
#    - Destination nodes (goal nodes)
# 3. Other components (e.g., search algorithms) only need to import `Graph`
#    and call `parse_graph()` to get the required data.
#
# ----------------------------------------------------------------------------------------
# Written by Xiaonan Li, 105206175
# Date: 19/03/2025
#

from Graph import Graph
from Astar.astar import Astar

def main():
    test_map = "test_map.txt"

    graph = Graph()
    graph, origin, destinations = graph.parse_graph(test_map)

    astar = Astar(graph, origin, destinations)
    result = astar.search()

    if graph is None:
        print("Failed to load graph from file")
        return

    print("Graph loaded.\n")
    print("Origin:", origin)
    print("Destinations:", destinations)

    graph.print_graph()

    print("Result:", result)

if __name__ == "__main__":
    main()