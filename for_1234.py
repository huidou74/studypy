#!/usr/bin/python
a = []   
for i in range(1,5):
    for x in range(1,5):
        for z in range(1,5):
            if (i != x and x != z and i !=z ):
                b = (i*100+x*10+z)
                a.append(str(b))
print a
print len(a)    
