/*
Build a function that returns an array of integers from n to 1 where n>0.

Example : n=5 --> [5,4,3,2,1]
https://www.codewars.com/kata/5a00e05cc374cb34d100000d/train/javascript
*/
const reverseSeq = n => {
  return [...Array(n).keys()].map(i=>n-i)
};