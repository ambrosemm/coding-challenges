"""
Complete the function/method so that it returns the url with anything after the anchor (#) removed.

Examples
"www.codewars.com#about" --> "www.codewars.com"
"www.codewars.com?page=1" -->"www.codewars.com?page=1"

https://www.codewars.com/kata/51f2b4448cadf20ed0000386/train/python
"""

def remove_url_anchor(url):
    ret = []
    for c in url:
        if c=='#':
            break
        ret.append(c)
    return ''.join(ret)