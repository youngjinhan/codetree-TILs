n = int(input())
arr = [0] + list(map(int, input().split()))
cnt_arr = [0] * (100001)

j, ans = 0, 0

for i in range(1, n+1):
    while j+1 <= n and cnt_arr[arr[j+1]] == 0:
        cnt_arr[arr[j+1]] += 1
        j += 1

    ans = max(ans, j - i + 1)

    cnt_arr[arr[i]] -= 1

print(ans)