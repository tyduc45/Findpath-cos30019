# Use AI to help learn the principles of this algorithm, but do not participate in the actual coding
from Infrastructure.Min_Heap import MinHeap

class GBFS:
    def __init__(self, graph, start, ends):
        self.graph = graph
        self.start = start
        self.ends = set(ends)
        self.heap = MinHeap()
        self.came_from = {}
        self.nodes_created = 0
        self.result_path = None
        self.end = None  # 将在 search 中设置为实际到达的目标点

    def gbfs_calculate(self):
        self.heap.push((0, self.start))
        self.came_from[self.start] = None

        while len(self.heap) > 0:
            current_cost, current_node = self.heap.pop()
            self.nodes_created += 1  # 访问节点数增加

            if current_node in self.ends:
                self.end = current_node
                return True

            for neighbor, cost in self.graph.get_neighbors(current_node).items():
                if neighbor not in self.came_from:
                    self.came_from[neighbor] = current_node
                    self.heap.push((cost, neighbor))  # 这里只用 cost 做启发排序

        return False

    def get_result(self):
        if self.end is None:
            return None, None, self.nodes_created

        path = []
        step = self.end
        while step is not None:
            path.append(step)
            step = self.came_from.get(step)
        path.reverse()

        self.result_path = path
        return self.end, self.nodes_created, path
