n,m = map(int, input().split())
arr = [[0 for col in range(m)] for row in range(n)]

d = [(0,1),(1,0),(0,-1),(-1,0)]
d_num = 0

x, y = 0, 0
cnt = 1
arr[x][y] = cnt
cnt += 1
for i in range(n*m - 1):
    dx, dy = d[d_num]
    nx, ny = x + dx, y + dy
    if 0<= nx < n and 0<= ny <m and arr[nx][ny] == 0:
        x, y = nx, ny
    else:
        d_num = (d_num+1) % 4
        dx, dy = d[d_num]
        x, y = x + dx, y + dy
    
    arr[x][y] = cnt
    cnt += 1

for i in range(n):
    print(*arr[i])
