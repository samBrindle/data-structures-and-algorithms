def quick_sort(list, left, right):
    if left < right:
        position = partition(list, left, right)

        quick_sort(list, left, position - 1)

        quick_sort(list, position + 1, right)

    return list


def partition(list, left, right):
    pivot = list[right]
    low = left - 1

    for i in range(left, right):
        if list[i] <= pivot:
            low += 1
            swap(list, i, low)

    swap(list, right, low + 1)

    return low + 1


def swap(list, i, low):
    temp = list[i]
    list[i] = list[low]
    list[low] = temp


if __name__ == "__main__":
    nums = [8, 23, 4, 16]
    print(quick_sort(nums, 0, len(nums)-1))
