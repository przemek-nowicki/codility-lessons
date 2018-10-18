def solution(H):
    stack = []
    numberOfStones = 0
    currentHeight = 0
    
    for h in H:
        while len(stack) != 0 and h < currentHeight:
            stone = stack.pop()
            currentHeight = currentHeight - stone

        if len(stack) == 0: 
            stoneSize = h
            currentHeight = h
            stack.append(stoneSize)
            numberOfStones = numberOfStones +1
        elif h > currentHeight:
            stoneSize = h - currentHeight
            currentHeight = h
            stack.append(stoneSize) 
            numberOfStones = numberOfStones +1
        elif h == currentHeight:
            continue

    return numberOfStones