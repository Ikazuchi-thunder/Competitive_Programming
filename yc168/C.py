b = list(map(int, input().split()))

r = (b[2] - b[1]) / (b[1]- b[0])

d = b[1] - r * b[0]

print(int(r * b[2] + d))
