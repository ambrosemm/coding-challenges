/*
Given an integer n and two other values, build an array of size n filled with these two values alternating.

Examples
5, true, false     -->  [true, false, true, false, true]
10, "blue", "red"  -->  ["blue", "red", "blue", "red", "blue", "red", "blue", "red", "blue", "red"]
0, "one", "two"    -->  []
Good luck!
https://www.codewars.com/kata/62a611067274990047f431a8/train/javascript
*/
function alternate(n, firstValue, secondValue){
    values = [firstValue, secondValue]
    ret = []
    for (i=0;i<n;i++){
      ret.push(values[i%2])
    }
    return ret
  }