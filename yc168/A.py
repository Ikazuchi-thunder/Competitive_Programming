s = input()

if s[-2:] == 'ai':
    print(s[:-2] + 'AI')
else:
    print(s + '-AI')
