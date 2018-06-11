
def solution(N):
    maxx =0
    cnt =0
    for i in bin(N)[2:]:
        if i == '0': 
            cnt = cnt +1
        elif i == '1': 
            if cnt > maxx: maxx=cnt
            cnt = 0
    return maxx