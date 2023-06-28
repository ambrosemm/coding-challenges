"""
Complete the function that takes a string of English-language text and returns the number of consonants in the string.

Consonants are all letters used to write English excluding the vowels a, e, i, o, u.
https://www.codewars.com/kata/564e7fc20f0b53eb02000106/train/python
"""
import string

def consonant_count(s):
    alphabet = list(string.ascii_lowercase+string.ascii_uppercase)
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    consonants = list(set(alphabet) - set(vowels))
    count = 0
    for c in s:
        if c in consonants:
            count+=1
    return count