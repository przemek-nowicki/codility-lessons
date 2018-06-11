def solution(N, A):

    B = [0] * N

    maxx=0
    last =0
    for k,x in enumerate(A):
        if x == N + 1: 
            last = maxx
        else:
            if B[x-1] > last:
                B[x-1] = B[x-1] + 1
            else:
                B[x-1] = last + 1

            if maxx < B[x-1]: maxx = B[x-1]
            
    for k,b in enumerate(B):
         if b < last: B[k] = last

    return B