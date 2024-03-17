"""
Given a logarithm base X and two values A and B, return a sum of logratihms with the base X: 
logX A+logX B.
 https://www.codewars.com/kata/5b68c7029756802aa2000176/train/python
"""
from math import log
def logs(x, a, b):
    return log(a, x) + log(b, x)s