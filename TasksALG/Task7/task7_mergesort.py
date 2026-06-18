def rearrange(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = rearrange(arr[:mid]) # делим раз
    right = rearrange(arr[mid:]) # делим два

    result = []

    # отрицательные из левой части
    for x in left:
        if x < 0:
            result.append(x)
    # отрицательные из правой части
    for x in right:
        if x < 0:
            result.append(x)
    # неотрицательные из левой части
    for x in left:
        if x >= 0:
            result.append(x)
    # неотрицательные из правой части
    for x in right:
        if x >= 0:
            result.append(x)
    return result


m = [9, -3, 5, -2, -8, -6, 1, 3]
print(rearrange(m))