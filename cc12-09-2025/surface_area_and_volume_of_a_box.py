"""
Write a function that returns the total surface area and volume of a box as an array: [area, volume]

https://www.codewars.com/kata/565f5825379664a26b00007c/train/python
"""

def get_size(w,h,d):
    return [2 * w * h + 2 * w * d + 2 * h * d, w * h * d]