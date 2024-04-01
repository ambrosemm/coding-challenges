"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.

https://www.codewars.com/kata/530e15517bc88ac656000716/train/python
"""
from string import ascii_lowercase, ascii_uppercase
def rot13(message):
    return _rot(message, 13)

def _rot(message, n):
    rotn_lower = {c:ascii_lowercase[(i+n)%len(ascii_lowercase)] for i, c in enumerate(ascii_lowercase)}
    rotn_upper = {c:ascii_uppercase[(i+n)%len(ascii_uppercase)] for i, c in enumerate(ascii_uppercase)}
    rotn = {**rotn_lower, **rotn_upper} # join the two dictionaries
    trans = ''.join([rotn[c] if c in rotn.keys() else c for c in message])
    return trans