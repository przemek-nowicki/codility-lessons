function solution(A) {
    let uniqueValues = [];
    let smallestPositiveInteger=0;

    for(let i=0; i<A.length; i++) {
        if(uniqueValues[A[i]]) {
            continue;
        }
        uniqueValues[A[i]] = true;
    }

    do {
        smallestPositiveInteger++;
    } while(uniqueValues[smallestPositiveInteger]);

    return smallestPositiveInteger;
}

console.log(solution([1,3,6,4,1,2]));