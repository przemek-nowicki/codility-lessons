function solution(N) {
    const binary = parseInt(N, 10);
    const binaryRep = binary.toString(2).split('');
    let zerosCnt = 0;
    let binaryGap = 0;
    for(let i=0; i<binaryRep.length; i++) {
        if(binaryRep[i] === '1') {
            binaryGap = zerosCnt > binaryGap ? zerosCnt : binaryGap;
            zerosCnt = 0;
        } else {
            zerosCnt++;
        }
    }
    return binaryGap;
}

console.log(solution(1041));