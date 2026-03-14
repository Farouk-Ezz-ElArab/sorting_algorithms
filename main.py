import copy
import random
import timeit
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort

sizes = [2500, 5000, 10000, 15000, 20000, 25000]

for size in sizes:

    print(f"\nArray Size: {size}")

    original = []
    for i in range(size):
        num = random.randint(0, 100000)
        original.append(num)

    arr1 = copy.deepcopy(original)
    time_bubble = timeit.timeit(lambda: bubble_sort(arr1), number=1)
    print("Bubble:", time_bubble * 1000, "ms")

    arr2 = copy.deepcopy(original)
    time_selection = timeit.timeit(lambda: selection_sort(arr2), number=1)
    print("Selection:", time_selection * 1000, "ms")

    arr3 = copy.deepcopy(original)
    time_insertion = timeit.timeit(lambda: insertion_sort(arr3), number=1)
    print("Insertion:", time_insertion * 1000, "ms")