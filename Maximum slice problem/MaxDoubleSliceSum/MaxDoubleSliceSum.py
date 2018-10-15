def solution(A):
    
    forward = [0] * len(A)
    ending = 0
    for i in range(1,len(A)-2):
        ending = max(0, ending + A[i])
        forward[i] = ending
    
    backwards = [0] * len(A)
    ending = 0
    for i in range(len(A)-2,1,-1):
        ending = max(0, ending + A[i])
        backwards[i] = ending

    maxi = 0    
    for i in range(0,len(A)-2):
        maxi = max(maxi, forward[i] + backwards[i+2])
        
    return maxi