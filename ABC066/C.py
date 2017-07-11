n = int(input())
a = list(map(int, input().split()))

result = []

if n % 2 == 0:
    for i in range(n, 0, -2):
        result.append(a[i - 1])
    for i in range(1, n, 2):
        result.append(a[i - 1])
else:
    for i in range(n, 0, -2):
        result.append(a[i - 1])
    for i in range(2, n, 2):
        result.append(a[i - 1])

print(' '.join(map(str, result)))
