n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr = [0] + sorted(arr)

j = n
ans = 0
for i in range(1, n+1):
    while j > i and arr[i] + arr[j] > k:
        j -= 1
    if j == i:
        break
    ans += j - i

print(ans)