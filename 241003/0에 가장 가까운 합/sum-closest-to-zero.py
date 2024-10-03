import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력:
n = int(input())
arr = list(map(int, input().split()))

arr = [0] + sorted(arr)

# 0에 가장 가까운 합을 구합니다.
ans = INT_MAX

# 구간을 잡아봅니다.
j = n
for i in range(1, n + 1):
    if i < j:
        ans = min(ans, abs(arr[i] + arr[j]))
    
    # 두 수의 합이 0 이하가 될 때 까지 j 구간을 내리면서 정답을 살펴봅니다.
    while i < j - 1 and arr[i] + arr[j] > 0:
        j -= 1
        ans = min(ans, abs(arr[i] + arr[j]))

# 정답을 출력합니다.
print(ans)