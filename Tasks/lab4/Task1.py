a = list(map(int, input().split()))
b = list(map(int, input().split()))

ca = 0
cb = 0

for i in a:
    if i % 2 == 0:
        ca += 1

for k in b:
    if k % 2 == 0:
        cb += 1

if ca > cb:
    print(a)
else:
    print(b)