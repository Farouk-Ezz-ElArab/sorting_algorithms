import random
import time
import time
import insertion_sort
import selection_sort
import bubble_sort


arr = [1,2,13,9,12]
arr1 = [9,5,8,3,5]
arr2 = [12,4,56,78,34]
start = time.time()
selection_sort.selection_sort(arr)
end = time.time()

print(arr)

print(f"runtime of selection is {(end - start) * 1000} milliseconds")

start1 = time.time()
insertion_sort.insertion_sort(arr1)
end1 = time.time()

print(arr1)

print(f"runtime of insersion is {(end1 - start1) * 1000} milliseconds")

start2 = time.time()
bubble_sort.bubble_sort(arr2)
end2 = time.time()

print(arr2)

print(f"runtime of bubble is {(end2 - start2) * 1000} milliseconds")