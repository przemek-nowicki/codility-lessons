import sys
def solution(N):
    i = 1
    perimeter = sys.maxsize
    while (i * i <= N):
        if N % i == 0:
            perimeter = min(perimeter, 2*(int(N/i)+i))
        i += 1

    return perimeter