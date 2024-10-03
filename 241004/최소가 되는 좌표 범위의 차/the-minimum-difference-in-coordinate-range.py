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



import sys
from collections import deque

def find_min_window(N, D, points):
    # 점들을 x좌표 기준으로 정렬
    points.sort(key=lambda p: p[0])
    
    left = 0
    min_diff = sys.maxsize
    min_deque = deque()
    max_deque = deque()
    
    for right in range(N):
        y = points[right][1]
        
        # 최소 y값을 관리하는 deque
        while min_deque and points[min_deque[-1]][1] >= y:
            min_deque.pop()
        min_deque.append(right)
        
        # 최대 y값을 관리하는 deque
        while max_deque and points[max_deque[-1]][1] <= y:
            max_deque.pop()
        max_deque.append(right)
        
        # 현재 윈도우가 조건을 만족하는지 확인
        while points[max_deque[0]][1] - points[min_deque[0]][1] >= D:
            current_diff = points[right][0] - points[left][0]
            if current_diff < min_diff:
                min_diff = current_diff
            # 왼쪽 포인터를 이동하면서 윈도우를 축소
            if min_deque[0] == left:
                min_deque.popleft()
            if max_deque[0] == left:
                max_deque.popleft()
            left += 1
    
    return min_diff if min_diff != sys.maxsize else -1

def main():
    import sys
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    D = int(data[1])
    points = []
    for i in range(N):
        x = int(data[2 + 2*i])
        y = int(data[3 + 2*i])
        points.append((x, y))
    
    result = find_min_window(N, D, points)
    print(result)

if __name__ == "__main__":
    main()