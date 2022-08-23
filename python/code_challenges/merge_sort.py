def merge_sort(list):
    length = len(list)

    if length > 1:
        mid = length // 2
        left = list[:mid]
        right = list[mid:]

        merge_sort(left)

        merge_sort(right)

        merge(left, right, list)

    return list

def merge(left, right, list):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            list[k] = left[i]
            i += 1
        else:
            list[k] = right[j]
            j += 1

        k += 1

    if i == len(left):
        list[k:] = right[j:]
    else:
        list[k:] = left[i:]


if __name__ == "__main__":
    nums = [8, 4, 23, 42, 16, 15]
    print(merge_sort(nums))
