#!/usr/bin/python
x = []
for i in range(100,1000):
    a = str(i)[0]
    b = str(i)[1]
    c = str(i)[2]
    d = a+b+c
    if str(int(a)**3+int(b)**3+int(c)**3) == d:
        x.append(d)
print x   

