x, y = 0, 0
mapper = {
    'W':0,
    'S':1,
    'N':2,
    'E':3
}

d = [(-1,0),(0,-1),(0,1),(1,0)]

n = int(input())
sec = 0
for i in range(n):
    dstr, dis = input().split()
    dis = int(dis)
    d_num = mapper[dstr]
    dx, dy = d[d_num]
    for j in range(dis):
        x, y = x + dx, y + dy
        sec += 1

        if x == 0 and y == 0:
            print(sec)
            exit()
print(-1)

