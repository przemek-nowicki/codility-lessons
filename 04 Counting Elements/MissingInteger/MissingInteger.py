def solution(A):
    A.sort()
    
    l=A[-1]
    if l <=0: return 1
    
    B = [None] * (l+2)
    for k,v in enumerate(A):
        if v > 0:
            B[v] = k
    
    B[0] = 0
    for k,b in enumerate(B):
        if b == None: return k