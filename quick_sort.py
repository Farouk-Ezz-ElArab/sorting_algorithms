def quick_sort(arr: list, low: int = 0, high: int = None) -> list:
    """
    Quick Sort — In-place, divide and conquer.
    Time:  O(n log n) average, O(n²) worst case
    """
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_index = _partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

    return arr


def _partition(arr: list, low: int, high: int) -> int:
    """Lomuto partition scheme — pivot is the last element."""
    pivot = arr[high]
    i = low - 1  # index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in its correct sorted position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1