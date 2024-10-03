n, d = map(int, input().split())
coor = [[0, 0]] + sorted([list(map(int, input().split())) for _ in range(n)], key = lambda x: x[1])

ans = 1000001

j= 1
for i in range(1, n):
    if i >= j:
        j = i + 1
    while j <= n and abs(coor[i][1] - coor[j][1]) < d:
        j += 1

    if j > n:
        break
    ans = min(ans, abs(coor[j][0] - coor[i][0]))
print(ans) if ans < 1000001 else print(-1)