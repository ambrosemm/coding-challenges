"""
Your task, is to create N×N multiplication table, of size provided in parameter.

For example, when given size is 3:

1 2 3
2 4 6
3 6 9
For the given example, the return value should be:

[[1,2,3],[2,4,6],[3,6,9]]

https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08/train
"""

def multiplication_table(size):
    rows = []
    for i in range(1, size+1):
        cols = []
        for j in range(1, size+1):
            cols.append(i*j)
        rows.append(cols)
    return rows