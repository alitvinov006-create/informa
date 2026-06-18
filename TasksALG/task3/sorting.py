def rad_sort(arr):
    maxi = max(arr)
    digit = 1
    while maxi // digit > 0:
        arr = sort_by_digit(arr, digit)
        digit *= 10
    return arr

def sort_by_digit(arr, digit):
    c = [[] for _ in range(10)]
    for i in arr:
        index_c = (i // digit) % 10
        c[index_c].append(i)
    return unite_c(c)

def unite_c(c):
    united_arr = []
    for bucket in c:
        united_arr.extend(bucket)
    return united_arr
print(rad_sort([3, 2, 1]))