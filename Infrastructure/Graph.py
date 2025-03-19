# Graph.py -- Graph Parsing Class
# ----------------------------------------------------------------------------------------
# This module provides the `Graph` class, which is responsible for
# parsing a map file and storing the graph data structure.
#
# Main functionalities:
# 1. Parse the map file and extract:
#    - Nodes (Nodes)
#    - Edges (Edges) (both directed & undirected)
#    - Origin (starting node)
#    - Destinations (goal nodes)
# 2. Store the graph using an adjacency list (Adjacency List)
# 3. Provide query functions:
#    - `get_neighbors(node)`: Retrieve the neighbors of a node
#    - `get_edges()`: Get all edges in the graph
#    - `has_edge(node1, node2)`: Check if an edge exists between two nodes
#    - `get_edge_weight(node1, node2)`: Get the weight of an edge
# ----------------------------------------------------------------------------------------
# Written by Xiaonan Li, 105206175
# Date: 18/03/2025
#

class Graph:
    # Initialize the adjacency list
    def __init__(self):
        self.nodes = {}
        self.origin = None
        self.destinations = []

    # Add a node if it does not exist
    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = {}

    # Add an edge between two nodes (default is directed)
    def add_edge(self, node1, node2, weight, directed=True):
        self.add_node(node1)
        self.add_node(node2)
        #  Add an edge between two nodes
        self.nodes[node1][node2] = weight
        if not directed:
            # Undirected edge (add both directions)
            self.nodes[node2][node1] = weight

    # Parse the graph file and store the data
    def parse_graph(self, filename):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            # Return None if the file is missing
            return None, None, None

        reading_nodes = False
        reading_edges = False

        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if not line or line.startswith("#"):
                i += 1
                continue  # Skip empty lines and comments
            if line.startswith("Nodes:"):
                reading_nodes = True
                reading_edges = False
            elif line.startswith("Edges:"):
                reading_nodes = False
                reading_edges = True
            elif line.startswith("Origin:"):
                i += 1  # Move to the next line
                if i < len(lines):
                    self.origin = int(lines[i].strip())  # Read the next line as the origin
            elif line.startswith("Destinations:"):
                i += 1  # Move to the next line
                if i < len(lines):
                    self.destinations = list(map(int, lines[i].strip().split(";")))  # Read next line as destinations
            elif reading_nodes:
                node_id = int(line.split(":")[0].strip())
                self.add_node(node_id)
            elif reading_edges:
                edge_info, weight = line.split(":")
                node1, node2 = map(int, edge_info.strip("()").split(","))
                weight = int(weight.strip())
                self.add_edge(node1, node2, weight, directed=True)

            i += 1  # Move to the next line

        return self, self.origin, self.destinations  # Parsing complete, return origin and destination nodes

    # Retrieve all nodes in the graph
    def get_nodes(self):
        return list(self.nodes.keys())

    # Retrieve all edges in the graph
    def get_edges(self):
        edges = []
        for node, neighbors in self.nodes.items():
            for neighbor, weight in neighbors.items():
                edges.append((node, neighbor, weight))
        return edges

    # Retrieve the neighbors of a given node
    def get_neighbors(self, node):
        return self.nodes.get(node, {})

    # Check if an edge exists between two nodes
    def has_edge(self, node1, node2):
        return node2 in self.nodes.get(node1, {})

    # Retrieve the weight of an edge
    def get_edge_weight(self, node1, node2):
        return self.nodes.get(node1, {}).get(node2, None)

    # Print the structure of the graph
    def print_graph(self):
        print("Graph structure:")
        for node, neighbors in self.nodes.items():
            print(f"  Node {node}: {neighbors}")


