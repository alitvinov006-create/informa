a = set(map(int, input().split()))
b = set(map(int, input().split()))
print(a if len(a) > len(b) else b)