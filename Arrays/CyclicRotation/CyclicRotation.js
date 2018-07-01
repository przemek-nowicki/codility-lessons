/**
 * 1. CyclicRotation
 * Rotate an array to the right by a given number of steps.
 */
function solution(A, K) {
    const rotated = [];
    for(let i = 0; i <A.length; i++){
        rotated[(i + K) % (A.length)] = A[i]
    }
    return rotated;
}
console.log(solution([3, 8, 9, 7, 6],3));