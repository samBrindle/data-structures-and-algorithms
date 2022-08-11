from data_structures.queue import Queue


class KaryTree:
    def __init__(self, root=None):
        self.root = root

    def clone(self):
        if not self.root:
            return KaryTree()

        breadth = Queue()
        clone_queue = Queue()
        breadth.enqueue(self.root)
        clone_root = Node(self.root.value)
        clone_queue.enqueue(clone_root)

        while not breadth.is_empty():
            front = breadth.dequeue()
            cloned_node = clone_queue.dequeue()
            for child in front.children:
                breadth.enqueue(child)
                clone_node = Node(child.value)
                clone_queue.enqueue(clone_node)
                clone_root.children.append(clone_node)

        return KaryTree(root=clone_root)

    def breadth_first(self):
        queue = Queue()

        collection = []

        queue.enqueue(self.root)

        while not queue.is_empty():
            node = queue.dequeue()
            collection.append(node.value)
            for child in node.children:
                queue.enqueue(child)

        return collection


class Node:
    """K-Ary Tree Node"""

    def __init__(self, value):
        self.value = value
        self.children = []
