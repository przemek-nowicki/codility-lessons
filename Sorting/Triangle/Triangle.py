def solution(A):
    if len(A) < 3: return 0
    A.sort()
    
    i = 0
    for i in range(0,len(A)-2):
        if A[i] == 0 or A[i+1] == 0 or A[i+2] == 0: continue
    
        if A[i] + A[i+1] > A[i+2]: return 1

    
    return 0