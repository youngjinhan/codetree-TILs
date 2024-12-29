n,m = map(int, input().split())
arr = [[0 for col in range(m)] for row in range(n)]

def in_range(x,y):
    return 0<= x <n and 0<= y <m

d = [(0,1),(1,0),(0,-1),(-1,0)]
d_num = 0

x, y = 0, 0
arr[x][y] = 1
for i in range(2, n*m + 1):
    dx, dy = d[d_num]
    nx, ny = x + dx, y + dy
    if not in_range(nx,ny) or arr[nx][ny] != 0:
        d_num = (d_num+1) % 4
        dx, dy = d[d_num]
            
    x, y = x + dx, y + dy
    
    arr[x][y] = i

for i in range(n):
    print(*arr[i])
