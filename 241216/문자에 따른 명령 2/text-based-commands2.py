orders = input()

y, x = 0, 0
d = [(-1,0), (0,1), (1,0), (0,-1)]
cur_d = 0
for i in range(len(orders)):
    o = orders[i]
    if o == 'F':
        dx, dy = d[cur_d]
        x += dx
        y += dy
    elif o == 'L':
        cur_d = (cur_d + 3) % 4
    elif o == 'R':
        cur_d = (cur_d + 1) % 4

print(y, x)