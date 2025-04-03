# dijkstra
from Infrastructure.Min_Heap import MinHeap

# written in Yifan Li 105205224

# compare order dist,node_id, insertion_order

class CUS1:
    def __init__(self, graph, start, destinations):
        self.graph = graph
        self.start = start
        self.destinations = destinations

    def reconstruct_path(self, prev, start, end):
        path = []  # Path stack
        current = end
        while current != -1:
            path.append(current)  # Backtrace path: end → start
            if current == start:
                break
            current = prev[current]
        if path[-1] != start:
            return []  # If start node is not reached, return empty path
        return path[::-1]  # Reverse path to get start → end

    # Dijkstra’s algorithm for shortest path
    def dijkstra(self, graph, start):
        number = 0
        node_list = graph.get_nodes()  # Retrieve nodes from graph
        visited = set()  # Set of visited nodes
        prev = [-1] * (len(node_list) + 1)  # Previous node for each node
        dist = {node: float('inf') for node in node_list}  # Initialize distances to ∞
        dist[start] = 0

        pq = MinHeap()
        pq.push((0, start))

        while len(pq) > 0:
            current_dist, node = pq.pop()

            if node in visited:
                continue
            visited.add(node)
            number += 1

            for neighbor in graph.get_neighbors(node):  # Relaxation step
                new_dist = current_dist + graph.get_edge_weight(node, neighbor)  # d[v] = min(d[v], d[u] + w(u,v))
                if new_dist < dist[neighbor]:  # If a shorter path is found
                    prev[neighbor] = node
                    dist[neighbor] = new_dist
                    pq.push((new_dist, neighbor))

        return dist, prev, number

    def result(self):
        dist, prev, number_of_nodes = self.dijkstra(self.graph, self.start)  # Run Dijkstra’s algorithm
        print("goal:", self.destinations, "number_of_nodes:", number_of_nodes)
        pathSheet = MinHeap()


        for destination in self.destinations:
            path = self.reconstruct_path(prev, self.start, destination)
            pathSheet.push((dist[destination],path))

        path = pathSheet.pop()


        return path[1][-1],number_of_nodes,path[1]



# Main function for command-line execution
'''
if __name__ == "__main__":
    import sys

    filename = sys.argv[1]  # Get input file name
    method = sys.argv[2]  # Get algorithm method (Dijkstra / A*)

    print(filename, method)

    graph = Graph(filename)  # Initialize graph

    graph, origin, destinations = graph.parse_graph()  # Parse input graph file

    dist, prev, number_of_nodes = dijkstra(graph, origin)  # Run Dijkstra’s algorithm

    print("goal:", destinations, "number_of_nodes:", number_of_nodes)

    print("path: ")
    for destination in destinations:
        path = reconstruct_path(prev, origin, destination)
        for node in path:
            if node is not destination:
                print(node, end="->")
            else:
                print(node, end="\n")
'''