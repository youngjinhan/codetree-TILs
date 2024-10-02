n = int(input())
arr = [0] + sorted(list(map(int, input().split())))

j = n
ans = 10**9
for i in range (1, n+1):
    p_sum = arr[i]
    while j > i and p_sum + arr[j] >= 0:
        if p_sum + arr[j] == 0:
            ans = 0
            exit 
        ans = min(ans, abs(p_sum + arr[j]))
        j -= 1

print(ans)