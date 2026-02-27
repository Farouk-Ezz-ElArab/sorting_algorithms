def bubble_sort(arr):
    sorted = False
    n = len(arr)
    for i in range (n):
        sorted = True
        for j in range (0,n-i-1):
            if arr[j] > arr[j+1]:
                sorted = False
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if sorted:
            break
    return arr
arr = [64, 34, 25, 1, 22, 11, 90]
print("Sorted array is:", bubble_sort(arr))