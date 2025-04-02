# we increase the threshold step by step (iterative deepening)
# every time we select the minium exceed value for new threshold
# once we found we stop
# so once we found,f(n) has to be the smallest,because lower than this were all impossible, and this one happens to be the case to find one

# both start and goal are tuple
# m_distance in this case is better than using euclid distance

# written in Yifan Li 105205224


class CUS2:
    def __init__(self, graph, start, destinations):
        self.graph = graph
        self.start = start
        self.destinations = destinations

    def h_func(self,start, goal):
        return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

    def Ida_star(self,start, goal, graph):
        visited_node = 0
        path = [start]

        visited_set = {start}

        start_Cor = graph.get_position(start)
        goal_Cor = graph.get_position(goal)

        threshold = self.h_func(start_Cor, goal_Cor)

        def dfs(node, g_func, threshold):
            nonlocal visited_node, min_threshold

            node_Cor = graph.get_position(node)
            f_func = g_func + self.h_func(node_Cor, goal_Cor)

            if f_func > threshold:
                return f_func
            if node == goal:
                return "FOUND"

            for neighbor in graph.get_neighbors(node):
                if neighbor in path:
                    continue

                if neighbor in visited_set:
                    continue
                visited_set.add(neighbor)
                visited_node += 1

                path.append(neighbor)
                weight = graph.get_edge_weight(node, neighbor)

                temp = dfs(neighbor, g_func + weight, threshold)
                if temp == "FOUND":
                    return "FOUND"
                if isinstance(temp, (int, float)) and temp < min_threshold:
                    min_threshold = temp
                path.pop()  # not found in [A,B,C], then we back track to [A,B]
                visited_set.remove(neighbor)  # delete access record
            return min_threshold

        while True:
            min_threshold = float('inf')  # record the smallest exceed value
            temp = dfs(start, 0, threshold)
            if temp == "FOUND":
                return path[:], visited_node
            if temp == float("inf"):
                print("no solution")
                return [], visited_node  # no solution
            threshold = temp  # iterative deepen

    def result(self):
        pathSheet = []
        total = 0

        for destination in self.destinations:
            path, visited_nodes = self.Ida_star(self.start, destination, self.graph)
            pathSheet.append(path)
            total += visited_nodes

        print("goal:", self.destinations, "number_of_nodes: ", total)

        print("path: ")
        for path in pathSheet:
            for node in path:
                if node != path[-1]:
                    print(node, end="->")
                else:
                    print(node, end=" ")
            print("\n")


'''
if __name__ == "__main__":
    import sys

    filename = sys.argv[1]
    method = sys.argv[2]

    print(filename, method)

    graph = Graph(filename)

    graph, origin, destinations = graph.parse_graph()

    pathSheet = []
    total = 0

    for destination in destinations:
       path, visited_nodes = Ida_star(origin, destination, graph, filename)
       pathSheet.append(path)
       total += visited_nodes

    print("goal:",destinations,"number_of_nodes: ", total)

    print("path: ")
    for path in pathSheet:
       for node in path:
           if node != path[-1]:
               print(node,end="->")
           else:
               print(node,end=" ")
       print("\n")
'''