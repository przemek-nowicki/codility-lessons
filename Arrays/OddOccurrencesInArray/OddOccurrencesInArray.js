/**
 * OddOccurrencesInArray
 * Find value that occurs in odd number of elements.
 */

function solution(A) {
    const pairs = {};
    for(let i=0; i<A.length; i++) {
        pairs[A[i]] = pairs[A[i]] ? pairs[A[i]]+1 : 1;
    }
    const unpaired = Object.keys(pairs).filter(a => pairs[a] === 1);
    return unpaired[0] ? parseInt(unpaired[0]) : 0;
}