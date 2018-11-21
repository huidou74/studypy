#!/usr/bin/python
import sys
while True:
    a = 0
    x = raw_input("input number for x : ")
    if x == 'q':
        sys.exit()

    y = raw_input("input number for y : ")
    if y == 'q':
        sys.exit()

    z = raw_input("input number for z : ")
    if z == 'q':
        sys.exit()
    else :
        x = int(x)
        y = int(y)
        z = int(z)
        if x > y:
#           x <--> y
            a = x
            x = y
            y = a
            if x > z:
#               x <--> z
                a = x
                x = z
                z = a
        if  y > z:
#           y <--> z
            a = y
            y = z
            z = a
            if x > y :
#              x <--> y
                a = x
                x = y
                y = a
        print (str("x : ")+ str(x)) 
        print (str("y : ")+ str(y)) 
        print (str("z : ")+ str(z)) 
