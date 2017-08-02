import numpy as np

K = int(input())

print(50)

n = K // 50
m = K % 50

a = np.array(range(50)) + n

for i in range(m):
    a -= 1
    a[i] += 51

print(' '.join(map(str, a)))
