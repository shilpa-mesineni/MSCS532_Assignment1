import random
import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Testing Quick Sort
def test_quick_sort():
    datasets = {
        "sorted": list(range(1, 10001)),
        "reverse_sorted": list(range(10000, 0, -1)),
        "random": [random.randint(1, 10000) for _ in range(10000)]
    }

    results = {}

    for name, data in datasets.items():
        start_time = time.time()
        sorted_data = quick_sort(data)
        end_time = time.time()
        results[name] = end_time - start_time

    return results

if __name__ == "__main__":
    results = test_quick_sort()
    print("Quick Sort Performance:")
    for name, time_taken in results.items():
        print(f"{name}: {time_taken:.6f} seconds")
