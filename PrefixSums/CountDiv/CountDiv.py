def solution(A, B, K):
    a = int(A/K)
    b = int(B/K)

    if A%K == 0: a = a - 1
    
    return b-a