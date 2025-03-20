from Infrastructure import Graph

graph = Graph.Graph()

graph, start, target = graph.parse_graph("PathFinder-test.txt")

print(start)
print(target)

neighbors = graph.get_neighbors(2)

print(neighbors,type(neighbors))