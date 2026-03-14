from quick_sort import partition


def kth_smallest(arr, k):
    arr = arr[:]
    low = 0
    high = len(arr) - 1

    while low <= high:
        pivot_index = partition(arr, low, high)

        if pivot_index == k - 1:
            return arr[pivot_index]
        elif pivot_index > k - 1:
            high = pivot_index - 1
        else:
            low = pivot_index + 1

    return -1