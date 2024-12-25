n, t = map(int, input().split())
arr =[[0 for col in range(n)] for row in range(n)]
r,c,d = input().split()
r,c = int(r), int(c)

mapper = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}

dir = [(0,1), (1,0), (-1,0), (0,-1)]
dir_num = mapper[d]

x,y = r-1,c-1
for i in range(t):
    dx, dy = dir[dir_num]
    if 0<= x + dx <n and 0<= y+dy <n:
        x+= dx
        y+= dy
    else:
        dir_num = 3 - dir_num
print(x+1, y+1)

