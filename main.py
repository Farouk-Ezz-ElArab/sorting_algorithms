import copy
import random
import time
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
    start = time.time()
    bubble_sort(arr1)
    end = time.time()
    print("Bubble:", (end - start) * 1000, "ms")

    arr2 = copy.deepcopy(original)
    start = time.time()
    selection_sort(arr2)
    end = time.time()
    print("Selection:", (end - start) * 1000, "ms")

    arr3 = copy.deepcopy(original)
    start = time.time()
    insertion_sort(arr3)
    end = time.time()
    print("Insertion:", (end - start) * 1000, "ms")