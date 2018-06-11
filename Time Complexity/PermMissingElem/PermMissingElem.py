def solution(A):
    n = len(A)+1
    sum_all = (int)(n*(n+1))/2
    sum = 0
    for i in A:
        sum = sum+i
        
    ret = int(sum_all - sum)

    return ret