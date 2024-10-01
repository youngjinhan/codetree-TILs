pos = [0] * 1000001
n, k = map(int, input().split())
max_p = 0
for i in range(n):
    cnt, p = map(int, input().split())
    max_p = max(max_p, p)
    pos[p] += cnt

p_sum = 0
ans = 0
j = 0
for i in range(1, 1000001):
    while j+1 <= 1000000 - 2*k and j+1 <= i + 2*k:
        p_sum += pos[j+1]
        j += 1 
    ans = max(ans, p_sum)
    p_sum -= pos[i]


print(ans)


# N, K = map(int, input().split())
 
# maxSize = 1000001
# arr = [0] * maxSize
# basket = set()
# for i in range(N):
#     a, b = map(int, input().split())
#     arr[b] += a
#     basket.add(b)
 
# j = 0
# k = 0
# jSum = 0
# kSum = 0
# res = 0
 
# for i in range(maxSize):
#     while j < i - K:
#         jSum += arr[j]
#         j += 1
    
#     while k <= i + K and k < maxSize:
#         kSum += arr[k]
#         k += 1
    
#     res = max(res, kSum - jSum)
    
# print(res)