import re

T = int(input())
S = []
for i in range(T):
    S.append(input())

for s in S:
    minind = 0
    maxind = 0
    before = False
    longest = ''
    see = ''
    nowminind = 0
    for i in range(len(s)):
        if s[i] in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
            if not before:
                nowminind = i
                before = True
            see += s[i]
        else:
            if len(see) >= len(longest):
                longest = see
                minind = nowminind
                maxind = i
            see = ''
            before = False
    if see != '':
        if len(see) >= len(longest):
            longest = see
            minind = nowminind
            maxind = len(s)
            see = ''

    if len(longest) == 0:
        print(s)
        continue

    ans = s[:minind]
    ans += ('%0' + str(len(longest)) + 'd') % (int(longest) + 1)
    ans += s[maxind:]
    print(ans)
