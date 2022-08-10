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

    def find_maximum_value(self):
        max_value = 0

        def find_max(root):
            nonlocal max_value

            if root:
                if root.value > max_value:
                    max_value = root.value
                    if root.left:
                        find_max(root.left)
                    if root.right:
                        find_max(root.right)
                    return max_value
                if root.value < max_value:
                    if root.left:
                        find_max(root.left)
                    if root.right:
                        find_max(root.right)
                    return max_value
            else:
                return max_value

        max_value = find_max(self.root)

        return max_value


class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


