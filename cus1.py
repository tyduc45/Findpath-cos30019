# dijkstra
from Infrastructure import min_heap
# graph: node list     start : start node index
def dijkstra(self, graph ,start):
    visited = set()       # known shortest
    dist = {node : float('inf') for node in graph}  # initialize to be inf
    dist[start] = 0

    pq = min_heap.MinHeap()
    pq.push((0, start))
    #dist to start is 0
    while len(pq.data) > 0:
        node, current_dist = pq.pop()

        if node in visited: continue
        visited.add(node)

        for neighbor in graph.get_neighbors(node):   # NEIGHBOR IS DICTIONARY
            new_dist = dist[node] + neighbor[1]
            if new_dist < dist[neighbor[0]]:          # relaxation progress
                dist[neighbor[0]] = new_dist
                pq.push((new_dist,neighbor))

    return dist





