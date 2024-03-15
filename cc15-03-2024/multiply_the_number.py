"""
Jack really likes his number five: the trick here is that you have to multiply each number by 5 raised to the number of digits of each numbers, so, for example:

  3 -->    15  (  3 * 5¹)
 10 -->   250  ( 10 * 5²)
200 --> 25000  (200 * 5³)
  0 -->     0  (  0 * 5¹)
 -3 -->   -15  ( -3 * 5¹)

https://www.codewars.com/kata/5708f682c69b48047b000e07/train/python
"""
def multiply(n):
    if n<0:
        return n*5**(len(str(n))-1)
    else:
        return n*5**(len(str(n)))