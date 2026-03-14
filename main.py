import copy
import random
import timeit
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from heap_sort import heap_sort
from merge_sort import merge_sort
from quick_sort import quick_sort

sizes = [2500, 5000, 10000, 15000, 20000, 25000]
RUNS = 3

for size in sizes:

    print(f"\nArray Size: {size}")

    original = []
    for i in range(size):
        num = random.randint(0, 100000)
        original.append(num)

    time_bubble = timeit.timeit(lambda: bubble_sort(copy.deepcopy(original)), number=RUNS) / RUNS
    print("Bubble:", time_bubble * 1000, "ms")

    time_selection = timeit.timeit(lambda: selection_sort(copy.deepcopy(original)), number=RUNS) / RUNS
    print("Selection:", time_selection * 1000, "ms")

    time_insertion = timeit.timeit(lambda: insertion_sort(copy.deepcopy(original)), number=RUNS) / RUNS
    print("Insertion:", time_insertion * 1000, "ms")

    time_heap = timeit.timeit(lambda: heap_sort(copy.deepcopy(original)), number=RUNS) / RUNS
    print("Heap:", time_heap * 1000, "ms")

    time_merge = timeit.timeit(lambda: merge_sort(copy.deepcopy(original)), number=RUNS) / RUNS
    print("Merge:", time_merge * 1000, "ms")

    time_quick = timeit.timeit(lambda: quick_sort(copy.deepcopy(original), 0, len(original) - 1), number=RUNS) / RUNS
    print("Quick:", time_quick * 1000, "ms")