#!/usr/bin/python
import sys
def factorial1(n):
    if n == 0:
        return 1
    else:
        return n * factorial1(n-1)

def factorial2(n):
    if n == 0:
        return 0
    else:
        return n + factorial2(n-1)

print "n * (n-1) = " + str(factorial1(int(sys.argv[1])))
print "n + (n-1) = " + str(factorial2(int(sys.argv[1])))
