import random
import time

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# Testing Merge Sort
def test_merge_sort():
    datasets = {
        "sorted": list(range(1, 10001)),
        "reverse_sorted": list(range(10000, 0, -1)),
        "random": [random.randint(1, 10000) for _ in range(10000)]
    }

    results = {}

    for name, data in datasets.items():
        start_time = time.time()
        merge_sort(data)
        end_time = time.time()
        results[name] = end_time - start_time
    
    return results

if __name__ == "__main__":
    results = test_merge_sort()
    print("Merge Sort Performance:")
    for name, time_taken in results.items():
        print(f"{name}: {time_taken:.6f} seconds")
