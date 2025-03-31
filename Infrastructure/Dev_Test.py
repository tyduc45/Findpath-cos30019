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
from algorithm_jzy.dfs import DFS
from algorithm_jzy.gbfs import GBFS
from bfs import BFS

def main():
    test_map = "test_map.txt"

    graph = Graph(test_map)
    graph, origin, destinations = graph.parse_graph()

    dfs = DFS(graph, origin, destinations)
    dfs.dfs_calculate()
    result = dfs.get_result()

    gbfs = GBFS(graph, origin, destinations)
    gbfs.gbfs_calculate()
    result2 = gbfs.get_result()

    astar = Astar(graph, origin, destinations)
    result3 = astar.search()

    bfs = BFS(graph, origin, destinations)
    bfs.bfs_calculate()
    result4 = bfs.get_result()

    if graph is None:
        print("Failed to load graph from file")
        return

    print("Graph loaded.\n")
    print("Origin:", origin)
    print("Destinations:", destinations)

    graph.print_graph()

    print("\nDFS Result:", result)
    print("\nGBFS Result:", result2)
    print("\nA* Result:", result3)
    print("\nBFS Result:", result4)

if __name__ == "__main__":
    main()