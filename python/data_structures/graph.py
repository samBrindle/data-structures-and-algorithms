class Graph:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.adjacency_list = {}

    def add_node(self, value):
        vertex = Vertex(value)

        self.adjacency_list[vertex] = []

        return vertex

    def size(self):
        return len(self.adjacency_list)

    def add_edge(self, start, end, weight=0):
        edge = Edge(end, weight)

        if end not in self.adjacency_list:
            raise KeyError

        self.adjacency_list[start].append(edge)

    def get_nodes(self):
        return self.adjacency_list.keys()

    def get_neighbors(self, vertex):
        return self.adjacency_list[vertex]


class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
