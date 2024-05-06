"""
When provided with a letter, return its position in the alphabet.

Input :: "a"

Ouput :: "Position of alphabet: 1"

https://www.codewars.com/kata/5808e2006b65bff35500008f/train/python
"""

import string

def position(c):
    return f"Position of alphabet: {string.ascii_lowercase.rfind(c) + 1}"