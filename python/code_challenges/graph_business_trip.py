from data_structures.graph import Graph


def direct_flights(graph, arr):
    if len(arr) == 0:
        return tuple([False, 0])

    nodes = graph.get_nodes()
    neighbors = None

    for node in nodes:
        if node.value == arr[0]:
            neighbors = graph.get_neighbors(node)
            break

    for neighbor in neighbors:
        if neighbor.vertex.value == arr[1]:
            print(tuple([True, neighbor.weight]))
            return tuple([True, neighbor.weight])

    return tuple([False, 0])
