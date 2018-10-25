def solution(A):
    
    peaks = []
    for i in range(1, len(A)-1):
        if A[i-1] < A[i] > A[i+1]:
            peaks.append(i)
            
    for number_of_blocks in range(len(peaks),0, -1):
        if len(A) % number_of_blocks:
            continue
        
        block_size = len(A) // number_of_blocks
        found = [False] * number_of_blocks
        cnt = 0
 
        for p in peaks:
            block_no = p // block_size
            if not found[block_no]:
                found[block_no] = True
                cnt += 1

            if cnt == number_of_blocks:
                return number_of_blocks
                
    return 0