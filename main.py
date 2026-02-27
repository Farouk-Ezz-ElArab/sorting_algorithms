import random
import time
import time
import insertion_sort
import selection_sort
import bubble_sort


arr = [1,2,0,13,9,12]
start = time.time()
selection_sort.selection_sort(arr)
end = time.time()

print(arr)

print(f"runtime is {(end - start) * 1000} milliseconds")