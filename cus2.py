# we increase the threshold step by step (iterative deepening)
# every time we select the minium exceed value for new threshold
# once we found we stop
# so once we found,f(n) has to be the smallest,because lower than this were all impossible, and this one happens to be the case to find one

# both start and goal are tuple
# m_distance in this case is better than using euclid distance

# written in Yifan Li 105205224

from Infrastructure.Min_Heap import MinHeap


class CUS2:
    def __init__(self, graph, start, destinations):
        self.graph = graph
        self.start = start
        self.destinations = destinations

    def sqrt(self, n, precision=1e-10):
        if n < 0:
            raise ValueError("Cannot compute square root of a negative number")
        if n == 0:
            return 0
        x = n  # Initial guess
        while abs(x * x - n) > precision:
            x = (x + n / x) / 2
        return x

    def h_func(self,start, goal):
        return self.sqrt((start[0] - goal[0])*(start[0] - goal[0]) + (start[1] - goal[1])*(start[1] - goal[1]))

    def Ida_star(self,start, goal, graph):
        visited_node = 0
        path = [start]
        visited_set = set()



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
                visited_node += 1
                return "FOUND"

            for neighbor in graph.get_neighbors(node):
                if node not in visited_set:
                    visited_set.add(node)
                    visited_node += 1
                    # print("node added:",node,"current visited node:",visited_node)

                if neighbor in path:
                    continue
                path.append(neighbor)

                weight = graph.get_edge_weight(node, neighbor)

                temp = dfs(neighbor, g_func + weight, threshold)
                if temp == "FOUND":
                    return "FOUND"
                if isinstance(temp, (int, float)) and temp < min_threshold:
                    min_threshold = temp
                path.pop()  # not found in [A,B,C], then we back track to [A,B]
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

    def calculate_cost(self,path):
        cost = 0
        for i in range(len(path) - 1):
            cost += self.graph.get_edge_weight(path[i], path[i+1])
        return cost

    def result(self):
        pathSheet = MinHeap()
        total = 0

        for destination in self.destinations:
            path, visited_nodes = self.Ida_star(self.start, destination, self.graph)
            dist = self.calculate_cost(path)
            pathSheet.push((dist,path,visited_nodes))

        path = pathSheet.pop()

        return path[1][-1], path[2], path[1]


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