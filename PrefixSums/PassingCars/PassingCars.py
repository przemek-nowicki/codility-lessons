def solution(A):
    east = 0 
    summ = 0
    for a in A:
        if a == 0: east = east+1
        else: summ = summ + east
    
    if summ > 1000000000: return -1
    return summ