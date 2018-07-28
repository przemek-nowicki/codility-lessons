function solution(A) {
    A.sort();
    if(A[0] !== 1) {
        return 0;
    }
    for(let i=A.length-1; i>=1; i--) {
        let diff = A[i] - A[i-1];
        if(diff !== 1) {
            return 0;
        }
    }
    return 1;
}