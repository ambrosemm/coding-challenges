"""
Converting a normal (12-hour) time like "8:30 am" or "8:30 pm" to 24-hour time (like "0830" or "2030") sounds easy enough, right? Well, let's see if you can do it!

You will have to define a function named "to24hourtime", and you will be given an hour (always in the range of 1 to 12, inclusive), a minute (always in the range of 0 to 59, inclusive), and a period (either "am" or "pm") as input.

Your task is to return a four-digit string that encodes that time in 24-hour time.

https://www.codewars.com/kata/59b0a6da44a4b7080300008a/train/python
"""
def to24hourtime(hour, minute, period):
    # hour will always range from 1 to 12 (inclusive)
    # minute will always range from 0 to 59 (inclusive)
    # period will always be either "am" or "pm"
    if period=='pm' and hour!=12:
        hour = hour+12
    elif period=='am' and hour==12:
        hour = 0
    raw = str(hour*100+minute)
    raw = '0'*(4-len(raw))+raw
    print(raw)
    return raw
