//NOT FINISCHED!!
def solution(S, P, Q):
    cumArr= [[0]*4for i in range(len(S))]
    
    for k,s in enumerate(S):
        if s == 'A':
            cumArr[k][0] =  1
        elif s == 'C':
            cumArr[k][1] = 1
        elif s == 'G':
            cumArr[k][2] =  1
        elif s == 'T':
            cumArr[k][3] =  1

    print(cumArr) 
    for i in range(len(P)):
        if cumArr[Q[i]][0] - cumArr[P[i]][0] != 0:
            print(1)
        elif cumArr[Q[i]][1] - cumArr[P[i]][1] != 0:
            print(2)
        elif cumArr[Q[i]][2] - cumArr[P[i]][2] != 0:
            print(3)
        elif cumArr[Q[i]][3] - cumArr[P[i]][3] != 0:
            print(4)
        else: print("upss")