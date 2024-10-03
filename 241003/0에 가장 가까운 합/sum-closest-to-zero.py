n = int(input())
arr = [0] + sorted(list(map(int, input().split())))

j = n
ans = 10**10
for i in range (1, n+1):
    if j > i:
        ans = min(ans, abs(arr[i] + arr[j]))
    
    while i < j-1 and arr[i] + arr[j] > 0:
        j -= 1
        ans = min(ans, abs(arr[i] + arr[j]))

print(ans)