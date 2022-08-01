from data_structures.stack import Stack
from data_structures.invalid_operation_error import InvalidOperationError


class PseudoQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        if self.stack1.is_empty():
            self.stack1.push(value)
            return
        else:
            while not self.stack1.is_empty():
                popped = self.stack1.pop()
                self.stack2.push(popped)

            self.stack1.push(value)

            while not self.stack2.is_empty():
                popped = self.stack2.pop()
                self.stack1.push(popped)

    def dequeue(self):
        return self.stack1.pop()

