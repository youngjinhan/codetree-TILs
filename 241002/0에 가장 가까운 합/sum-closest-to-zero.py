n = int(input())
arr = [0] + sorted(list(map(int, input().split())))

j = n
ans = 10**10
for i in range (1, n+1):
    p_sum = arr[i]
    while j > i and abs(p_sum + arr[j]) <= ans:
        ans = abs(p_sum + arr[j])
        j -= 1

    if ans == 0:
        break 
print(ans)