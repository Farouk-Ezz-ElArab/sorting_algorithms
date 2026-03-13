def partition(arr: list, low: int, high: int) -> int:
    """Lomuto partition — same function used in QuickSort."""
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def kth_smallest(arr: list, k: int) -> int:
    """
    Find the Kth smallest element using QuickSelect.

    Key idea:
      - After partition(), pivot lands at its FINAL sorted index.
      - If pivot_index == k-1  → pivot IS the kth smallest ✓
      - If pivot_index >  k-1  → search LEFT half
      - If pivot_index <  k-1  → search RIGHT half
    """
    if k < 1 or k > len(arr):
        raise ValueError(f"k={k} is out of range for array of size {len(arr)}")

    arr = arr[:]          # work on a copy to avoid mutating the original
    low, high = 0, len(arr) - 1

    while low <= high:
        pivot_index = partition(arr, low, high)

        if pivot_index == k - 1:
            return arr[pivot_index]          # found it!
        elif pivot_index > k - 1:
            high = pivot_index - 1           # go left
        else:
            low = pivot_index + 1            # go right