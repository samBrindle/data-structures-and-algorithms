from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """

    # def __init__(self):
    #     # initialization here
    #     super().__init__()

    def add_to_empty(self, value):
        """
        wrap value in a Node and add it at correct spot
        """
        self.root = Node(value)

    def add(self, value):

        node = Node(value)

        if not self.root:
            self.root = node

        def walk(root, node_to_add):
            if root is None:
                return

            if node_to_add.value < root.value:
                if not root.left:
                    root.left = node_to_add
                else:
                    walk(root.left, node_to_add)

            if node_to_add.value > root.value:
                if not root.right:
                    root.right = node_to_add
                else:
                    walk(root.right, node_to_add)

        walk(self.root, node)

    def contains(self, target):

        def walk(root):
            if root is None:
                return False

            if root.value == target:
                return True

            if root.value > target:
                return walk(root.left)
            else:
                return walk(root.right)

        return walk(self.root)
