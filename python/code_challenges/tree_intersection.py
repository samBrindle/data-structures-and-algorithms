from data_structures.binary_tree import BinaryTree
from data_structures.hashtable import Hashtable


def tree_intersection(tree1, tree2):
    hash = Hashtable()
    mixed_list = tree1.pre_order() + tree2.pre_order()
    matches = []

    for num in mixed_list:
        if hash.contains(chr(num)) and not num in matches:
            matches.append(num)
        else:
            temp = chr(num)
            hash.set(temp, 1)

    return matches


    """
    create hashtable
    create new list equal to post order of tree1 and tre2 combined
    iterate through list and check if hash contains value at index
    """
