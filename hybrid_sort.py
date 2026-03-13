"""
Hybrid Merge and Selection Sort Algorithm
------------------------------------------
- If array size <= THRESHOLD  →  use Selection Sort
- If array size >  THRESHOLD  →  use Merge Sort (recursive)

This reduces the overhead of merging on very small subarrays.
"""

def selection_sort(arr: list) -> list:
    """Sort in-place using Selection Sort. Returns the sorted array."""
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# ─────────────────────────────────────────
#  MERGE helper
# ─────────────────────────────────────────

def _merge(left: list, right: list) -> list:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ─────────────────────────────────────────
#  HYBRID MERGE + SELECTION SORT
# ─────────────────────────────────────────

def hybrid_merge_selection_sort(arr: list, threshold: int = 10) -> list:
    """
    Hybrid sorting algorithm:
      - size <= threshold  →  Selection Sort  (fast for tiny arrays)
      - size >  threshold  →  Merge Sort      (efficient for large arrays)

    Parameters
    ----------
    arr       : list to sort
    threshold : cutoff size (default 10)
    """
    # BASE CASE — small enough, use Selection Sort
    if len(arr) <= threshold:
        return selection_sort(arr[:])      # copy so original stays untouched

    # RECURSIVE CASE — split and merge
    mid   = len(arr) // 2
    left  = hybrid_merge_selection_sort(arr[:mid], threshold)
    right = hybrid_merge_selection_sort(arr[mid:], threshold)

    return _merge(left, right)