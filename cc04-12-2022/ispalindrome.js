/*
Write a function that checks if a given string (case insensitive) is a palindrome.
https://www.codewars.com/kata/57a1fd2ce298a731b20006a4/train/javascript
 */
function isPalindrome(x) {
    a = x.toLowerCase().split('').join('')
    b = x.toLowerCase().split('').reverse().join('')
    return a==b
}