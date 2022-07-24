class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        self.head = Node(value, self.head)

    def includes(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            else:
                current = current.next

        return False

    def __str__(self):
        dummy_node = self.head
        string = ""
        # dummyNode helps you keep track of head of linkedList
        # dummyNode = self.head
        # dummyNode.next and so on

        while dummy_node is not None:
            string += "{ " + f"{dummy_node.value}" + " } -> "
            dummy_node = dummy_node.next
        string += "NULL"
        return string


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
