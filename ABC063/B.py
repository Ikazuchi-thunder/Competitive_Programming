import sys

S = input()

saw = []

for i in S:
    if i in saw:
        print('no')
        sys.exit()
    else:
        saw.append(i)

print('yes')
