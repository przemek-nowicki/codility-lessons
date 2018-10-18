
def solution(S, P, Q):
    cumArr= [[0]*4for i in range(len(S)+1)]
    A = 0 
    C = 0
    G = 0 
    T = 0
    
    for k,s in enumerate(S):
        if s == 'A':
            A = A +1
        elif s == 'C':
            C = C +1
        elif s == 'G':
            G = G +1
        elif s == 'T':
            T = T +1
            
        cumArr[k+1][0] = A
        cumArr[k+1][1] = C
        cumArr[k+1][2] = G
        cumArr[k+1][3] = T

    #print(cumArr) 
    ret = [0] * len(P)
    for i in range(len(P)):
        #print(Q[i]+1,P[i])
        #print(cumArr[Q[i]+1],  cumArr[P[i]])
        
        if cumArr[Q[i]+1][0] > cumArr[P[i]][0]:
            ret[i] = 1
        elif cumArr[Q[i]+1][1] > cumArr[P[i]][1]:
            ret[i] = 2
        elif cumArr[Q[i]+1][2] > cumArr[P[i]][2]:
            ret[i] = 3
        elif cumArr[Q[i]+1][3] > cumArr[P[i]][3]:
            ret[i] = 4

    #print(ret)         
    return ret