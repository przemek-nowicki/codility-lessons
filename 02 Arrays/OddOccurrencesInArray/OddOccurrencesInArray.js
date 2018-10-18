/**
 * OddOccurrencesInArray
 * Find value that occurs in odd number of elements.
 */

function solution(A) {
    const pairs = {};
    for(let i=0; i<A.length; i++) {
        pairs[A[i]] = pairs[A[i]] ? pairs[A[i]]+1 : 1;
    }
    for(let key in pairs) {
        if(pairs[ key ] % 2 === 1)
            return +key;
    }
}