from data_structures.graph import Graph


def direct_flights(graph, arr):
    if len(arr) == 0:
        return tuple([False, 0])

    nodes = graph.get_nodes()
    neighbors = None
    cost = 0

    for i in range(len(arr)-1):
        for node in nodes:
            if node.value == arr[i]:
                neighbors = graph.get_neighbors(node)
                break

        for neighbor in neighbors:
            if neighbor.vertex.value == arr[i+1]:
                cost += neighbor.weight

    if cost == 0:
        return tuple([False, cost])
    else:
        return tuple([True, cost])
