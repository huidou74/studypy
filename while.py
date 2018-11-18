#!/usr/bin/python
a = ''
while a != 'q' :
    a = raw_input("input the q for quit : ")
    print "hello "
    if not a:
        break 
    if a == 'quit':
        continue
    print "continue"
else :
    print "is ture quit!"


