from data_structures.kary_tree import KaryTree, Node
from data_structures.queue import Queue


def fizz_buzz_tree(og_tree):
    tree = og_tree.clone()

    breadth = Queue()
    breadth.enqueue(tree.root)

    while not breadth.is_empty():
        front = breadth.dequeue()
        if front.value % 3 == 0 and front.value % 5 == 0:
            front.value = "FizzBuzz"
        elif front.value % 3 == 0:
            front.value = "Fizz"
        elif front.value % 5 == 0:
            front.value = "Buzz"
        else:
            front.value = str(front.value)

        for child in front.children:
            breadth.enqueue(child)

    return tree
