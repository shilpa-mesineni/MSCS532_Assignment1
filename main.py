def insertion_sort_descending(arr):
   
    for i in range(1, len(arr)):
        key = arr[i]
        
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

array = [12, 11, 13, 5, 6, 43, 23, 7, 56, 23]
sorted_array = insertion_sort_descending(array)
print("Sorted array in monotonically decreasing order:", sorted_array)
