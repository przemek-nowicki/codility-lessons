function solution(A) {
    let i=0;
    let totaSum = 0;
    const n = A.length;
    for(i=0; i < n; i++) {
        totaSum += A[i];
    }
    let firstPartSum = 0;
    let secondPartSum = 0;
    let absDiff = 0;
    let minDiff = Number.POSITIVE_INFINITY;
    for(i=0; i<n-1; i++) {
        firstPartSum += A[i];
        secondPartSum = totaSum - firstPartSum;
        absDiff = Math.abs(firstPartSum - secondPartSum);
        if(absDiff < minDiff) {
            minDiff = absDiff;
        }
    }
    return minDiff;
}