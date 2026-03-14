def bubble_sort(arr):
    is_sorted = False
    n = len(arr)
    for i in range (n):
        is_sorted = True
        for j in range (0,n-i-1):
            if arr[j] > arr[j+1]:
                is_sorted = False
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if is_sorted:
            break
    return arr