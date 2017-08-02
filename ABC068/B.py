N = int(input())

k = [2 ** i for i in range(1, 8)]

M = 1

for i in k:
    if i <= N:
        M = i

print(M)
