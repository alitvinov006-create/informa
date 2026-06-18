import random, time

def q_sort(arr, low, high):
    if low < high:
        key = s_divide(arr, low, high)
        q_sort(arr, low, key - 1)
        q_sort(arr, key + 1, high)
    return arr

def s_divide(arr, low, high):
    key = arr[high]
    i = low - 1
    for j in range(low, high):  # исправлено
        if arr[j] <= key:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

arr = [random.randint(1, 100000) for _ in range(50000)]
ts = time.time()
print(q_sort(arr, 0, len(arr) - 1))
te = time.time()
print(te-ts)