#!/usr/bin/python
import sys
import os
def isNum(s):
    for i in s:
         if i in '0123456789':
             pass
         else:
             break
          #   print "%s is a not number" % s
    else:
         print s
for i in os.listdir("/proc"):
    isNum(i)
