def insertion_sort(list):
    print(f"Original List: {list}")
    for i in range(1, len(list)):
        value = list[i]

        j = i-1
        while j >= 0 and value < list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = value

    print(f"Sorted List: {list}")
    return list


arr = [16, 8, 12, 4, 2]

insertion_sort(arr)
