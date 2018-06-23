def solution(A):
    
    alen = len(A)
    avgmin = (A[0] + A[1])/2
    avgstart = 0
    
    for i in range(1,alen):
        if i + 2 > alen: break
        
        avg = (A[i] + A[i+1]) / 2
        if avg < avgmin:
            avgmin = avg
            avgstart = i
        
        if i + 3 > alen: continue
        
        avg = (A[i] + A[i+1] + A[i+2]) / 3
        if avg < avgmin:
            avgmin = avg
            avgstart = i
        
        
    return avgstart