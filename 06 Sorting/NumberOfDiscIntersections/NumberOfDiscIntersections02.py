# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    axis = []
    for i in range(len(A)):
        ring = [(i - A[i], +1), (i + A[i], -1)]
        axis += ring
    
    axis.sort(key=lambda r: (r[0], -r[1]))
      
   
    result, active = 0, 0
    for i in range(len(axis)):
        if (axis[i][1] == 1 ):
            result = result + active
        active =  active + axis[i][1]
        
    result = result if result <= 10E6 else -1   
    
    return result