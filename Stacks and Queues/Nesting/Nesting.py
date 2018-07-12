def solution(S):
    cnt = 0
    for s in S:
        if s == '(': cnt = cnt + 1
        elif s == ')': cnt = cnt - 1
        if cnt < 0: return 0
            
    if cnt == 0: return 1
    else: return 0