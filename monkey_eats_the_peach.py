#!/usr/bin/python
# -*- coding:--utf8 -*-
a = 1
b = 1 
print "第10 天剩下桃子: %s " % a
for i in range(9,0,-1):
    a = ((a + 1 ) *2)
    print "第 %s 天剩下桃子: %s " % (i,a)
for i in range(1,11):
    b = ((a+1)*2)
print  "total : %s" % b
