function solution(X, A) {
    const positions = [];
    let earliestTime = -1;
    let noJumps = 0;
    for(let i = 0; i < A.length; i++) {
        if(positions[A[i]]) {
            continue;
        }
        positions[A[i]] = true;
        noJumps++;
        if(noJumps === X) {
            earliestTime = i;
            break;
        }
    }
    return earliestTime;
}

const A = [1,3,1,4,2,3,5,4];
const X = 5;

console.log(solution(X, A));