n, m = map(int, input().split())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))

def is_subsequence():
    i = 1
    for j in range(1, m+1):
        if i <= n and A[i] != B[i]:
            i += 1
        
        if i == n+1:
            return False
        
        i += 1
    
    return True

print("Yes") if is_subsequence() else print("No")