/*
Write a function which calculates the average of the numbers in a given list.

Note: Empty arrays should return 0.
https://www.codewars.com/kata/57a2013acf1fa5bfc4000921/train/javascript
*/
function findAverage(array) {
  if (array.length===0){
    return 0;
  } else {
    return array.reduce((a, b) => a + b) / array.length;
  }
}