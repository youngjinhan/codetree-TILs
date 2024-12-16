n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

d = [(0,1), (1,0), (0,-1), (-1,0)]

ans = 0
for i in range(n):
    for j in range(n):
        tmp_cnt = 0
        for k in range(4):
            x, y = i + d[k][0], j + d[k][1]
            
            if 0 <= x < n and 0 <= y < n and arr[x][y] == 1:
                tmp_cnt += 1
            
        if tmp_cnt >= 3:
            ans += 1
print(ans)