# Graph.py -- Graph Parsing and Data Handling Class
# ----------------------------------------------------------------------------------------
# This module provides the `Graph` class, which is responsible for
# parsing a map file and storing the graph data structure.
#
# Main functionalities:
# 1. Parse the map file and extract:
#    - Nodes (Nodes) with associated (x, y) coordinates.
#    - Edges (Edges) (both directed & undirected) with weights.
#    - Origin (starting node).
#    - Destinations (goal nodes).
# 2. Store the graph using an adjacency list (Adjacency List) for efficient traversal.
# 3. Load node coordinates only once from the file to optimize performance.
# 4. Provide query functions:
#    - `get_neighbors(node)`: Retrieve the neighbors of a node.
#    - `get_edges()`: Get all edges in the graph.
#    - `has_edge(node1, node2)`: Check if an edge exists between two nodes.
#    - `get_edge_weight(node1, node2)`: Get the weight of an edge.
#    - `get_coordinates(node)`: Get the (x, y) coordinates of a node.
# ----------------------------------------------------------------------------------------
#
# Written by Xiaonan Li, 105206175
# Date: 18/03/2025
#

class Graph:
    # Initialize the adjacency list
    def __init__(self, filename):
        self.nodes = {}
        self.origin = None
        self.destinations = []
        self.filename = filename
        self.node_positions = self.load_positions()

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
    def parse_graph(self):
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
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
                i += 1
                if i < len(lines):
                    self.origin = int(lines[i].strip())
            elif line.startswith("Destinations:"):
                i += 1
                if i < len(lines):
                    self.destinations = list(map(int, lines[i].strip().split(";")))
            elif reading_nodes:
                try:
                    node_id, position = self.get_X_Y(line)  # Extract node ID and position
                    if node_id is not None:
                        self.add_node(node_id)
                        self.node_positions[node_id] = position  # Store positions
                except ValueError:
                    print(f"Warning: Skipping invalid node entry in file -> {line}")
            elif reading_edges:
                try:
                    edge_info, weight = line.split(":")
                    node1, node2 = map(int, edge_info.strip("()").split(","))
                    weight = int(weight.strip())
                    self.add_edge(node1, node2, weight, directed=True)
                except ValueError:
                    print(f"Warning: Skipping invalid edge entry in file -> {line}")

            i += 1

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

    def get_X_Y(self, line):
        if line is None:
            return None,None
        try:
            index = int(line.split(":")[0].strip())
            after_colon = line.split(":")[1].strip()

            if not after_colon.startswith("(") or not after_colon.endswith(")"):
                raise ValueError(f"Invalid coordinate format: {line}")

            inner = after_colon[1:-1]
            _X_Y_Cor = tuple(int(x) for x in inner.split(","))
            return index, _X_Y_Cor
        except (IndexError, ValueError):
            print(f"Error: Invalid node coordinate format -> {line}")
            return None, None

    # Returns the (x, y) coordinates of a node, if available.
    def get_position(self, node_index):
        return self.node_positions.get(node_index, (None, None))

    # Retrieve the coordinates of a given node
    # Ensures that the node position has been loaded from the map file
    # Returns the (x, y) coordinates of a node if available
    def get_coordinates(self, node):
        return self.node_positions.get(node, (None, None))

    # Load all node positions from the graph file
    # This function reads node coordinates only once and stores them in a dictionary
    def load_positions(self):
        node_positions = {}

        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
            return node_positions

        getting_position = False
        for line in lines:
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            if line.startswith("Nodes:"):
                getting_position = True
                continue

            if line.startswith("Edges:"):
                getting_position = False
                break

            if getting_position:
                index, position = self.get_X_Y(line)
                if index is not None:
                    node_positions[index] = position

        return node_positions