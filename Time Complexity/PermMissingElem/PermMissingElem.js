function solution(A) {
    const total = A.length;
    let sum = (total + 1) * (total + 2) / 2;
    for (let i = 0; i < total; i++) {
        sum -= A[i];
    }
    return sum;
}

console.log(solution([2,3,1,5]));