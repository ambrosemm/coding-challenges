"""
ould find two different items in the array that, when added together, give the target value. The indices of these items should then be returned in a tuple / list (depending on your language) like so: (index1, index2).

For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; target will always be the sum of two different items from that array).

Based on: https://leetcode.com/problems/two-sum/

two_sum([1, 2, 3], 4) # returns (0, 2) or (2, 0)
two_sum([3, 2, 4], 6) # returns (1, 2) or (2, 1)

https://www.codewars.com/kata/52c31f8e6605bcc646000082/train/python
"""

def two_sum(numbers, target):
    for i, x in enumerate(numbers):
        for j, y in enumerate(numbers):
            if x+y==target and i!=j:
                return (i,j)