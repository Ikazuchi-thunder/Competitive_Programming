import math

N = int(input())

ans = set()

for i in range(1, math.ceil(N ** 0.5) + 1):
    if N % i == 0:
        ans.add(str(i) + str(N // i))
        ans.add(str(N // i) + str(i))

print(ans)
print(len(ans))
