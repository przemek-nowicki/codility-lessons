def solution(A):
    if len(A) < 2: return 0
    
    max_slice = max_ending = 0
    minPrice = A[0]
    for a in A[1:]:
        max_ending = max(0, a - minPrice)
        minPrice = min(minPrice,a)
        max_slice = max(max_slice, max_ending)

    return max_slice