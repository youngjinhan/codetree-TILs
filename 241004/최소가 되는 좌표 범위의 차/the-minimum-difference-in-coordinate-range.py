# n, d = map(int, input().split())
# coor = [[0, 0]] + sorted([list(map(int, input().split())) for _ in range(n)], key = lambda x: x[1])

# ans = 1000001

# j= 1
# for i in range(1, n):
#     if i >= j:
#         j = i + 1
#     while j <= n and abs(coor[i][1] - coor[j][1]) < d:
#         j += 1

#     if j > n:
#         break
#     ans = min(ans, abs(coor[j][0] - coor[i][0]))
# print(ans) if ans < 1000001 else print(-1)




def min_range_with_y_difference(N, D, points):
    # 점들을 x 좌표 기준으로 정렬
    points.sort()
    
    min_length = float('inf')
    left = 0
    
    for right in range(N):
        # 현재 오른쪽 포인터에 있는 점의 y좌표
        while left <= right and points[right][1] - points[left][1] >= D:
            # y좌표 차이가 D 이상인 경우
            min_length = min(min_length, points[right][0] - points[left][0])
            left += 1
    
    return min_length if min_length != float('inf') else -1

# 입력 처리
N, D = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(N)]

# 결과 출력
result = min_range_with_y_difference(N, D, points)
print(result)