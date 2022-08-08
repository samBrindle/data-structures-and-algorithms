from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue


def breadth_first(tree):
    queue = Queue()
    tree_list = []
    root = tree.root
    queue.enqueue(root)

    if root is None:
        return tree_list
    while not queue.is_empty():
        curr = queue.dequeue()
        tree_list.append(curr.value)
        if curr.left:
            queue.enqueue(curr.left)
        if curr.right:
            queue.enqueue(curr.right)

    return tree_list
