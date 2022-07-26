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

    def append(self, value):
        current = self.head
        while current.next is not None:
            current = current.next

        current.next = Node(value)

    # Got help form Ben Small with this layout
    def insert_before(self, value, new_value):
        current = self.head

        if current is None:
            raise TargetError
        elif current.value == value:
            dummy_node = self.head
            self.head = Node(new_value, dummy_node)
        else:
            current = self.head
            while current.next is not None:

                if current.next.value == value:
                    current.next = Node(new_value, current.next)
                    break
                else:
                    current = current.next

            else:
                raise TargetError

    def insert_after(self, value, new_value):
        current = self.head
        while current is not None:

            if current.value == value:
                current.next = Node(new_value, current.next)
                break
            else:
                current = current.next

        else:
            raise TargetError

    def kth_from_end(self, k):
        current = self.head
        node_list = []

        while current is not None:
            node_list.insert(0,current.value)
            current = current.next

        if 0 <= k < len(node_list):
            return node_list[k]
        else:
            raise TargetError

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

class TargetError(Exception):
    pass
