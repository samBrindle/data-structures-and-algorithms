from data_structures.queue import Queue
from data_structures.stack import Stack

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
        return list(self.adjacency_list.keys())

    def get_neighbors(self, vertex):
        return self.adjacency_list[vertex]

    def breadth_first(self, vertex):
        nodes = []
        breadth = Queue()
        visited = set()

        breadth.enqueue(vertex)
        visited.add(vertex)

        while not breadth.is_empty():
            front = breadth.dequeue()
            nodes.append(front.value)

            for neighbor in self.get_neighbors(front):
                if neighbor.vertex not in visited:
                    visited.add(neighbor.vertex)
                    breadth.enqueue(neighbor.vertex)

        return nodes

    def depth_first_search(self, vertex):
        nodes = []
        depth = Stack()
        visited = set()

        if len(self.get_nodes()) == 0:
            return nodes

        depth.push(vertex)
        visited.add(vertex)

        while not depth.is_empty():
            top = depth.pop()
            nodes.append(top.value)

            for neighbor in reversed(self.get_neighbors(top)):
                if neighbor.vertex not in visited:
                    visited.add(neighbor.vertex)
                    depth.push(neighbor.vertex)

        return nodes


class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
