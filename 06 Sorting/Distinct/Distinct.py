def solution(A):
    if len(A) == 0: return 0
    A.sort()
    i = 1
    cnt = 1
    while i < len(A):
        if A[i-1] != A[i]:
            cnt = cnt+1
        i = i+1
    return cnt 