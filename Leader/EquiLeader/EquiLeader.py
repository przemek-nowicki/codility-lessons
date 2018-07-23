def solution(A):
    idx = -1
    size = 0
    for i in range(len(A)):
        if size == 0: 
            idx = i
            size = 1
        elif A[i] != A[idx]:
            size = size - 1
        elif A[i] == A[idx]:
             size = size +1

    cnt = 0
    for a in A:
        if a == A[idx]: cnt = cnt +1

    if cnt <= len(A)/2: 
        return 0

    cnt_left = 0
    cnt_equiLeader = 0

    for i in range(len(A)):
        if A[i] == A[idx]: 
            cnt_left = cnt_left +1
        if cnt_left > (i+1)/2 and (cnt - cnt_left) > (len(A) - i -1)/2:
            cnt_equiLeader = cnt_equiLeader + 1
            
    return cnt_equiLeader