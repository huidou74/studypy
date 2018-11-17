#!/usr/bin/python
while True:
    suma = int(raw_input("please input the number :"))
    if suma >= 90:
        print "A"
    elif suma >= 80:
        print "B"
    elif suma >= 60:
        print "C"
    elif suma == -1:
        break
    else :
        print "D"
print "END" 

