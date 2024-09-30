n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

j, p_sum, ans = 0, 0 , 0

for i in range(1, n+1):
    while j+1 <= n and p_sum + arr[j+1] <= m:
        p_sum += arr[j+1]
        if p_sum == m:
            ans += 1
        j += 1
    
    
    p_sum -= arr[i]

print(ans)