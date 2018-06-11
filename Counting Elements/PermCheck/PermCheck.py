def solution(A):
    A.sort()
    
    x = 0;
    if A[0] != 1: return 0
    
    for i in range(0,len(A)-1):
        if A[i] !=  A[i+1]-1:
            return 0
            
    return 1