import sys

N = int(input())
s = []
for i in range(N):
    s.append(int(input()))

if sum(s) % 10 != 0:
    print(sum(s))
else:
    for i in sorted(s):
        if i % 10 != 0:
            print(sum(s) - i)
            sys.exit()
    print(0)
