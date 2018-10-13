def solution(A):
    max_ending = max_slice = A[0]
    for a in A[1:]:
        max_ending = max(a,max_ending + a)
        max_slice = max(max_slice, max_ending)
        
    return max_slice