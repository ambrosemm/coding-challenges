"""
Your task is to write function factorial.

https://en.wikipedia.org/wiki/Factorial

https://www.codewars.com/kata/57a049e253ba33ac5e000212/train/python
"""

def factorial(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f