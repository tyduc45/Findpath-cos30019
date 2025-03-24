# dijkstra
from Infrastructure import min_heap
from Infrastructure.Graph import Graph

# written in Yifan Li 105205224

# compare order dist,node_id, insertion_order

def reconstruct_path(prev, start, end):                # prev is an array for pre-index
    path = []                                          # vertex stack
    current = end
    while current != -1:
        path.append(current)                           # current path: from end -> start
        if current == start:
            break
        current = prev[current]
    if path[-1] != start:
        return []                                       # cannot reach
    return path[::-1]                                   # reverse the path so that we can get start->end

# graph: node list     start : start node index
def dijkstra(graph,start):
    number = 0
    node_list = graph.get_nodes()                       # get nodes from graph
    visited = set()                                     # known shortest
    prev = [-1] * (len(node_list)+1)         # get previous node
    dist =  {node : float('inf') for node in node_list} # initialize to be inf
    dist[start] = 0

    pq = min_heap.MinHeap()
    pq.push((0,start))                                 #dist to start is 0
    while len(pq.data) > 0:
        current_dist, node = pq.pop()                   # current_dist : d[u]

        if node in visited:
            continue
        visited.add(node)
        number += 1

        for neighbor in graph.get_neighbors(node):                            # relaxation progress
            new_dist = current_dist + graph.get_edge_weight(node,neighbor)    # d[v] = min{d[v],d[u] + w(u, v)}
            if new_dist < dist[neighbor]:                                     # set prev of neighbor to node
                prev[neighbor] = node
                dist[neighbor] = new_dist
                pq.push((new_dist,neighbor))

    return dist,prev,number

if __name__ == "__main__":
    import sys

    filename = sys.argv[1]
    method = sys.argv[2]

    print(filename, method)

    graph = Graph()

    graph, origin, destinations = graph.parse_graph(filename)

    dist,prev,number_of_nodes = dijkstra(graph,origin)

    print("goal:",destinations,"number_of_nodes: ",number_of_nodes)

    print("path: ")
    for destination in destinations:
       path = reconstruct_path(prev,origin,destination)
       for node in path:
           if node is not destination:
               print(node, end="->")
           else:
               print(node, end="\n")












