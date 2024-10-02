n = int(input())
arr = [0] + sorted(list(map(int, input().split())))

j = n
ans = 10**10
p_sum = arr[1] + arr[n]
if p_sum == 0:
    print(0) 
    exit

is_possitive = True if p_sum > 0 else False

for i in range (1, n+1):
    while j > i and ((is_possitive and arr[i] + arr[j] > 0) or (not is_possitive and arr[i] + arr[j] < 0)):
        ans = min(ans, abs(arr[i] + arr[j]))
        is_possitive = arr[i] + arr[j] > 0
        j -= 1

    if ans == 0:
        break 
print(ans)