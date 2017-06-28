import sys

N = int(input())
a = []
for i in range(N):
    a.append(int(input()))

count = 0
now = 1

while count < N:
    count += 1
    now = a[now - 1]
    if now == 2:
        print(count)
        sys.exit()

print(-1)
