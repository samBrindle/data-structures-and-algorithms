from data_structures.linked_list import LinkedList, Node, TargetError


def zip_lists(a, b):
    list1 = a.head
    list2 = b.head
    list3 = LinkedList()
    switch = True

    if list1:
        list3.insert(list1.value)
        list1 = list1.next
    elif list2:
        list3.insert(list2.value)
        list2 = list2.next

    current = list3.head

    while list1 is not None or list2 is not None:
        if switch and list2 is not None:
            list3.insert_after(current.value, list2.value)
            list2 = list2.next
            current = current.next

        if not switch and list1 is not None:
            list3.insert_after(current.value, list1.value)
            list1 = list1.next
            current = current.next

        if switch:
            switch = False
        else:
            switch = True

    return list3
