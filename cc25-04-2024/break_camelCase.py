"""
Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""

https://www.codewars.com/kata/5208f99aee097e6552000148/train/python
"""
def solution(s):
    return "".join([" " + c if c.isupper() else c for c in s])
        