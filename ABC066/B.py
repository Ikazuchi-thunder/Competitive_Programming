import sys

S = input()
n = len(S) // 2

for i in range(1, n):
    if S[0:n - i] == S[n - i: 2 * n - 2 * i]:
        print((n - i) * 2)
        sys.exit()
