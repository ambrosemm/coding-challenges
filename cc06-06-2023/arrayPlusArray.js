/*
I'm new to coding and now I want to get the sum of two arrays... Actually the sum of all their elements. I'll appreciate for your help.

P.S. Each array includes only integer numbers. Output is a number too.
https://www.codewars.com/kata/5a2be17aee1aaefe2a000151/train/javascript
*/
function arrayPlusArray(arr1, arr2) {
    const sum = (arr) => arr.reduce((a, b)=>a+b)
    return sum(arr1) + sum(arr2);
  }