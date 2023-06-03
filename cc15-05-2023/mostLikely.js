/*
Create a function which compares two probabilities, returning true if the first one is most likely otherwise false.

For this exercise probability is expressed as two numbers separated by a colon e.g. a probability of 1 in 3 will be 1:3.

So:

Input: ('1:3','1:2') - returns false as 1 in 3 is less likely than 1 in 2.
https://www.codewars.com/kata/56644a421b7c94c622000056/train/javascript
*/
function mostLikely(prob1,prob2){
    let convert2num = function (x) {return Number(x)}
    let ar1 = prob1.split(":").map(convert2num)
    let ar2 = prob2.split(":").map(convert2num)
    return ar1[0]/ar1[1] > ar2[0]/ar2[1]
}