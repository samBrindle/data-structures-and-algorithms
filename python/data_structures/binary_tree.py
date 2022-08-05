class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self, root=None):
        self.root = root

    def pre_order(self):
        values = []

        def stroll(root):
            if root is None:
                return

            values.append(root.value)

            stroll(root.left)

            stroll(root.right)

        stroll(self.root)

        return values

    def in_order(self):
        values = []

        def stroll(root):
            if root is None:
                return

            # left
            stroll(root.left)

            # root
            values.append(root.value)

            # right
            stroll(root.right)

        stroll(self.root)

        return values

    def post_order(self):
        values = []

        def stroll(root):
            if root is None:
                return

            # left
            stroll(root.left)

            # right
            stroll(root.right)

            # root
            values.append(root.value)

        stroll(self.root)

        return values


class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


