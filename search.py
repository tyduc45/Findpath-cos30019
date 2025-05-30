import sys
from Astar.astar import Astar
from Infrastructure.Graph import Graph
from algorithm_jzy.dfs import DFS
from algorithm_jzy.gbfs import GBFS
from bfs import BFS
from cus1 import CUS1
from cus2 import CUS2

ALGORITHMS = {
    "DFS": DFS,
    "BFS": BFS,
    "GBFS": GBFS,
    "AS": Astar,
    "CUS1": CUS1,
    "CUS2": CUS2
}

def main():
    global goal, count, path
    if len(sys.argv) != 3:
        print("Usage: python search.py <filename> <method>")
        sys.exit(1)

    filename = sys.argv[1]
    method = sys.argv[2].upper()

    if method not in ALGORITHMS:
        print(f"Invalid method: {method}. Choose from {', '.join(ALGORITHMS.keys())}")
        sys.exit(1)

    graph = Graph(filename)
    graph, origin, destinations = graph.parse_graph()

    if graph is None:
        print("Error parsing graph. Exiting.")
        sys.exit(1)

    if method == "DFS":
        search_algo = DFS(graph, origin, destinations)
        search_algo.dfs_calculate()
        goal, count, path = search_algo.get_result()
    elif method == "BFS":
        search_algo = BFS(graph, origin, destinations)
        search_algo.bfs_calculate()
        goal, count, path = search_algo.get_result()
    elif method == "GBFS":
        search_algo = GBFS(graph, origin, destinations)
        search_algo.gbfs_calculate()
        goal, count, path = search_algo.get_result()
    elif method == "AS":
        search_algo = Astar(graph, origin, destinations)
        search_algo.search()
        goal, count, path = search_algo.get_result()
    elif method == "CUS1":
        search_algo = CUS1(graph, origin, destinations)
        goal, count, path = search_algo.result()
    elif method == "CUS2":
        search_algo = CUS2(graph, origin, destinations)
        goal, count, path = search_algo.result()

    else:
        print(f"Invalid method: {method}. Choose from DFS, BFS, GBFS, AS, CUS1, CUS2")
        sys.exit(1)

    print(f"{filename} {method}")
    print(f"{goal} {count}")
    if path:
        print(path)
    else:
        print("No path found.")

if __name__ == "__main__":
    main()