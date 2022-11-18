class GraphNode:
    def __init__(self, data):
        self.vertex = data
        self.next  = None

class Graph:
    # Undirected Graph class
    def __init__(self, vertices):
        # Constructor method
        self.vertices = vertices
        self.graph = [None for _ in range(vertices)]

    def add_edge(self, src, dest):
        """
        Function that add a new edge
        """
        node = GraphNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        node = GraphNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node
 
    def print_graph(self):
        """
        Function that return the representation of the graph
        """
        for i in range(self.vertices):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertices), end="")
                temp = temp.next
            print(" \n")