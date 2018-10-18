
def solution(A):
    A.sort()
    #two negatives gives positive, take max   
    return max(A[0]*A[1]*A[-1], A[-1]*A[-2]*A[-3])