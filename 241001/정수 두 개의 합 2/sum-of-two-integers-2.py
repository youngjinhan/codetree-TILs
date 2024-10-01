n, k = map(int, input().split())
arr = sorted([0] + [int(input()) for _ in range(n)])

j = n
ans = 0
for i in range(1, n+1):
    while j > i and arr[i] + arr[j] > k:
        j -= 1
    if j == i:
        break
    ans += j - i

print(ans)