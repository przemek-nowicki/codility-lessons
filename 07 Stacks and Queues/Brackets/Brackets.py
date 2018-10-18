def solution(S):
    
    cnt = [0] * 3
    stack = []
    
    for s in S:
        if s == '(': 
            cnt[0] = cnt[0] + 1
            stack.append(0)
        elif s == ')':
            if len(stack) == 0 or stack[-1] != 0: return 0
            stack.pop()
            cnt[0] = cnt[0] - 1
        elif s == '[': 
            stack.append(1)
            cnt[1] = cnt[1] + 1
        elif s == ']': 
            if len(stack) == 0 or stack[-1] != 1: return 0
            stack.pop()
            cnt[1] = cnt[1] - 1
        elif s == '{': 
            stack.append(2)
            cnt[2] = cnt[2] + 1
        elif s == '}': 
            if len(stack) == 0 or stack[-1] != 2: return 0
            stack.pop()
            cnt[2] = cnt[2] - 1
        
        if any(v < 0 for v in cnt): return 0
        
    if all(v == 0 for v in cnt) and len(stack) == 0: 
        return 1
    else:
        return 0