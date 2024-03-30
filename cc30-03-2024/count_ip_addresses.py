"""
Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).

All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.

Examples
* With input "10.0.0.0", "10.0.0.50"  => return   50 
* With input "10.0.0.0", "10.0.1.0"   => return  256 
* With input "20.0.0.10", "20.0.1.0"  => return  246

https://www.codewars.com/kata/526989a41034285187000de4/train/python
"""
def ips_between(start, end):
    return abs(ip2int(start)-ip2int(end))

def ip2int(ips):
    return sum([int(ip)*256**i for ip, i in zip(ips.split('.'), (reversed(range(4))))])