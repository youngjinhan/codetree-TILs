n = int(input())
x, y = 0, 0
for i in range(n):
    d, l = input().split()
    l = int(l)
    if d == 'N':
        y += l
    elif d == 'E':
        x += l
    elif d == 'S':
        y -= l
    elif d == 'W':
        x -= l
print(x, y)