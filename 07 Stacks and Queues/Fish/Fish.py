def solution(A, B):
    survivals = []
    survivals_cnt = 0
    
    for i in range(len(A)):
        if B[i] == 0:
            while len(survivals) > 0:
                if A[i] < A[survivals[-1]]:
                    break
                else:
                    survivals.pop()
            else:
                #this fish made it to the top
                survivals_cnt = survivals_cnt + 1
        else:
            survivals.append(i)
            
    survivals_cnt = survivals_cnt + len(survivals)
    return survivals_cnt