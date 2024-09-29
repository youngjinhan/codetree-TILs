n, s = map(int, input().split())
arr = list(map(int, input().split()))
leng = len(arr)

j = 0
p_sum = 0
ans = -1
for i in range(leng):
    while j < leng:
        if p_sum >= s:
            ans = j - i if ans == -1 else min(ans, j-i)
            # print(i, ans)
            break
        p_sum += arr[j]
        j += 1
    p_sum -= arr[i]

print(ans)