#!/usr/bin/python
info = {}
name = raw_input("please input name :")
age = raw_input("please input age :")
clas = raw_input("please input class :")
info = {'name  ':name,'age   ':age,'class ':clas}
for k, v in info.items() :
    print "%s: %s" % (k, v)
#    print k + ': ', v
print "END"
 
