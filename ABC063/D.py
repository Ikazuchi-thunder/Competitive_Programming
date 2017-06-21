import math

N, A, B = map(int, input().split())
h = []
for i in range(N):
    h.append(int(input()))


def enough(T):
    h2 = list(map(lambda x: x - B * T, h))
    return sum(map(lambda x: max(0, math.ceil(x / (A - B))), h2)) <= T


def solver(inf, sup):
    mid = (inf + sup) // 2
    if inf == sup:
        return mid
    elif enough(mid):
        return solver(inf, mid)
    else:
        return solver(mid + 1, sup)


print(solver(0, 10 ** 9))
