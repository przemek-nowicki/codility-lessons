# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    starts = [None] * len(A)
    ends = [None] * len(A)
    for i in range(len(A)):
        starts[i] = i - A[i]
        ends[i] = i + A[i]

    starts.sort()
    ends.sort()

    start = 0 
    end = 0
    current = 0
    result = 0
    for i in range(len(starts)):
        
        while start < len(starts) and starts[start] <= ends[end]:
            current = current + 1
            start = start + 1
            
        current = current -1
        result = result + current
        
        end = end +1
        
    result = result if result <= 10E6 else -1   
    
    return result