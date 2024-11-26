import numpy as np
import time

np.random.seed(40)
bilangan = np.random.randint(0, 101, size=50)

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

start_time = time.time()
bilangan_copy = bilangan.copy()
merge_sort(bilangan_copy)
execution_time = time.time() - start_time

print("Bilangan sebelum disorting:", bilangan)
print("Bilangan setelah disorting (Merge Sort):", bilangan_copy)
print("Waktu eksekusi:", execution_time, "detik")