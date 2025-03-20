import sys
import subprocess
from Graph import Graph

# 设定支持的搜索算法
ALGORITHMS = {
    "DFS": "dfs.py",
    "BFS": "bfs.py",
    "GBFS": "gbfs.py",
    "AS": "astar.py",
    "CUS1": "cus1.py",
    "CUS2": "cus2.py"
}

def main():
    # 命令行参数校验
    if len(sys.argv) != 3:
        print("Usage: python search.py <filename> <method>")
        sys.exit(1)

    filename = sys.argv[1]  # 读取图文件
    method = sys.argv[2].upper()  # 读取搜索方法并转换为大写

    # 检查搜索方法是否合法
    if method not in ALGORITHMS:
        print(f"Invalid method: {method}. Choose from {', '.join(ALGORITHMS.keys())}")
        sys.exit(1)

    # 解析图文件
    graph = Graph()
    graph, origin, destinations = graph.parse_graph(filename)

    if graph is None:
        print("Error parsing graph. Exiting.")
        sys.exit(1)

    print(f"Parsed Graph from {filename}")
    print(f"Origin: {origin}, Destinations: {destinations}")
    print("Graph structure:")
    graph.print_graph()  # 打印解析出的图结构，方便调试

    # 运行相应的搜索算法
    subprocess.run(["python", ALGORITHMS[method], filename, method])

if __name__ == "__main__":
    main()