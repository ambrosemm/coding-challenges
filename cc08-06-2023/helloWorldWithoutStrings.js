/*
Task
You need to create a function, helloWorld, that will return the String Hello, World! without actually using raw strings. This includes quotes, double quotes and template strings. You can, however, use the String constructor and any related functions.

You cannot use the following:

"Hello, World!"
'Hello, World!'
`Hello, World!`
Good luck and try to be as creative as possible!
https://www.codewars.com/kata/584c7b1e2cb5e1a727000047/train/javascript
*/
const helloWorld = () => {
    return String.fromCharCode(72) +
           String.fromCharCode(101) +
           String.fromCharCode(108) +
           String.fromCharCode(108) +
           String.fromCharCode(111) +
           String.fromCharCode(44) +
           String.fromCharCode(32) +
           String.fromCharCode(87) +
           String.fromCharCode(111) +
           String.fromCharCode(114) +
           String.fromCharCode(108) +
           String.fromCharCode(100) +
           String.fromCharCode(33)
  };