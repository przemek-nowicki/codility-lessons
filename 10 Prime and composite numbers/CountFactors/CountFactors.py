def solution(N):
    i = 1
    factors = 0
    while (i * i < N):
        if N%i == 0:
            factors += 2
        i += 1
        
    if i*i == N:
        factors += 1
        
    return factors