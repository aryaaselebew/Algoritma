# Arya Nanda Putra | F55123087
import time

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Data
A = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
B = [0, 1, 2, 3, 4, 9, 8, 7, 6, 5]

# Menghitung waktu komputasi Bubble Sort untuk A
start_time = time.time()
bubble_sorted_A = bubble_sort(A.copy())
bubble_sort_time_A = time.time() - start_time

# Menghitung waktu komputasi Quick Sort untuk A
start_time = time.time()
quick_sorted_A = quick_sort(A.copy())
quick_sort_time_A = time.time() - start_time

# Menghitung waktu komputasi Bubble Sort untuk B
start_time = time.time()
bubble_sorted_B = bubble_sort(B.copy())
bubble_sort_time_B = time.time() - start_time

# Menghitung waktu komputasi Quick Sort untuk B
start_time = time.time()
quick_sorted_B = quick_sort(B.copy())
quick_sort_time_B = time.time() - start_time

# Output hasil
print("Hasil Sorting A dengan Bubble Sort:", bubble_sorted_A)
print("Hasil Sorting A dengan Quick Sort:", quick_sorted_A)
print(f"Time Bubble Sort untuk A: {bubble_sort_time_A:.8f} detik")
print(f"Time Quick Sort untuk A: {quick_sort_time_A:.8f} detik\n")

print("Hasil Sorting B dengan Bubble Sort:", bubble_sorted_B)
print("Hasil Sorting B dengan Quick Sort:", quick_sorted_B)
print(f"Time Bubble Sort untuk B: {bubble_sort_time_B:.8f} detik")
print(f"Time Quick Sort untuk B: {quick_sort_time_B:.8f} detik\n")

if bubble_sort_time_A > quick_sort_time_A:
    print("Quick Sort lebih efektif untuk list A")
else:
    print("Bubble Sort lebih efektif untuk list A")

if bubble_sort_time_B > quick_sort_time_B:
    print("Quick Sort lebih efektif untuk list B")
else:
    print("Bubble Sort lebih efektif untuk list B")
