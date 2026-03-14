from merge_sort import merge
from selection_sort import selection_sort


def hybrid_sort(arr, threshold):
    if len(arr) <= threshold:
        return selection_sort(arr[:])

    mid = len(arr) // 2
    left = hybrid_sort(arr[:mid], threshold)
    right = hybrid_sort(arr[mid:], threshold)

    return merge(left, right)