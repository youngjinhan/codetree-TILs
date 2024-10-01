pos = [0] * 1000001
n, k = map(int, input().split())
max_p = 0
for i in range(n):
    cnt, p = map(int, input().split())
    max_p = max(max_p, p)
    pos[p] += cnt

p_sum = 0
for i in range(1, 2*k + 2):
    p_sum += pos[i]

ans = p_sum

for i in range(2, p - (2*k) + 1):
    p_sum = p_sum - pos[i - 1] + pos[i + 2*k]
    ans = max(ans, p_sum)

print(ans)