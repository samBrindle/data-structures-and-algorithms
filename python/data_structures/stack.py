from data_structures.invalid_operation_error import InvalidOperationError


class Stack:
    """
    Put docstring here
    """

    def __init__(self, top=None):
        # initialization here
        self.top = top

    def push(self, value):
        # method body here
        node = Node(value, self.top)
        self.top = node

    def pop(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        prev_top = self.top
        self.top = self.top.next
        return prev_top.value

    def is_empty(self):
        return self.top is None

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value

class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_
