class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            self.value = Node(value)

    def __str__(self):
        string = "{ "
        # dummyNode helps you keep track of head of linkedList
        # dummyNode = self.head
        # dummyNode.next and so on

        if self.head is None:
            return "NULL"
        else:
            dummy_node = self.head
            while dummy_node.value.next is not None:
                string + f"{dummy_node.value}" + " } -> "

            return string + " NULL"
            # while self.head.value != None:
            #     string + f"{ self.head.value } -> "
            # return string + "NULL"
            # return"{ " + f"{self.head.value}" + " } -> NULL"


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class TargetError:
    pass
