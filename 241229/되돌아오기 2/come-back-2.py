x,y = 0, 0
d = [(0,1),(1,0),(0,-1),(-1,0)]
d_num = 0

args = input()

for i in range(len(args)):
    arg = args[i]
    if arg == 'F':
        dx,dy = d[d_num]
        x, y = x + dx, y + dy
        if x == 0 and y == 0:
            print(i+1)
            exit()
    elif arg == 'L':
        d_num = (d_num+3) % 4
    elif arg == 'R':
        d_num = (d_num+1) %4

print(-1)