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

    # Debuging use, Please delete after entire debugging
    print(f"Parsed Graph from {filename}")
    print(f"Origin: {origin}, Destinations: {destinations}")
    print("Graph structure:")
    graph.print_graph()

    if method == "DFS":
        search_algo = DFS(graph, origin, destinations)
        search_algo.dfs_calculate()
        result = search_algo.get_result()
    elif method == "BFS":
        search_algo = BFS(graph, origin, destinations)
        search_algo.bfs_calculate()
        result = search_algo.get_result()
    elif method == "GBFS":
        search_algo = GBFS(graph, origin, destinations)
        search_algo.gbfs_calculate()
        result = search_algo.get_result()
    elif method == "AS":
        search_algo = Astar(graph, origin, destinations)
        result = search_algo.search()
    # Didn't add 2 cus logic
    elif method == "CUS1":
        search_algo = CUS1(graph, origin, destinations)
        result = search_algo.result()
    elif method == "CUS2":
        search_algo = CUS2(graph, origin, destinations)
        result = search_algo.result()
    else:
        print(f"Invalid method: {method}. Choose from DFS, BFS, GBFS, AS, CUS1, CUS2")
        sys.exit(1)

if __name__ == "__main__":
    main()