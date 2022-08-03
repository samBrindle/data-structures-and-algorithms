from data_structures.invalid_operation_error import InvalidOperationError


class Queue:
    """
    Put docstring here
    """

    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear

    def enqueue(self, value):
        new_rear = Node(value)

        if not self.rear:
            self.rear = new_rear
            self.front = new_rear
        else:
            prev_rear = self.rear
            self.rear = new_rear
            prev_rear.next = new_rear

    def dequeue(self):
        if self.is_empty():
            raise InvalidOperationError("InvalidOperationError")

        prev_rear = self.front
        if self.front is self.rear:
            self.rear = None
        self.front = self.front.next
        prev_rear.next = None
        return prev_rear.value

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.front.value

    def is_empty(self):
        return self.rear is None


class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_
