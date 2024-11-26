import numpy as np
import time

np.random.seed(40)
bilangan = np.random.randint(0, 101, size=50)

def naive_sort(arr):
    max_value = max(arr)
    bucket = [0] * (max_value + 1)

    for num in arr:
        bucket[num] += 1

    sorted_arr = []
    for i, count in enumerate(bucket):
        sorted_arr.extend([i] * count)

    return sorted_arr

start_time = time.time()
sorted_numbers = naive_sort(bilangan)
execution_time = time.time() - start_time

print("Bilangan sebelum disorting:", bilangan)
print("Bilangan setelah disorting (Naive Sort):", sorted_numbers)
print("Waktu eksekusi:", execution_time, "detik")
