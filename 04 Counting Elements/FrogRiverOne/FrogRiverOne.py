def solution(X, A):
    B = [None] * X
    for k,v in enumerate(A):
        if B[v-1] == None:
             B[v-1] = k
    
    
    for v in B:
        if v == None:
            return -1
    B.sort()   
    
    return B[X-1]