a = [1, 7, 5, 3, 8, 88, 2, 66, 32]
n = len(a)

for j in range(0, n - 1):
    for i in range(0, n - j - 1):
        if a[i] < a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
    print(a)
print(a)

