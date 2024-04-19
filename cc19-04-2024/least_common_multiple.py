"""Write a function that calculates the least common multiple of its arguments; each argument is assumed to be a non-negative integer. In the case that there are no arguments (or the provided array in compiled languages is empty), return 1. If any argument is 0, return 0.Write a function that calculates the least common multiple of its arguments; each argument is assumed to be a non-negative integer. In the case that there are no arguments (or the provided array in compiled languages is empty), return 1. If any argument is 0, return 0.

https://www.codewars.com/kata/5259acb16021e9d8a60010af/train/python
"""

import math

def lcm(*args):
    """Compute the least common multiple of some non-negative integers"""
    if not args:
        return 1

    lcm = args[0]
    for number in args[1:]:
        lcm = math.lcm(lcm, number)

    return lcm