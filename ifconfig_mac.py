#!/usr/bin/python
macaddr = 'C8:60:00:8E:6F:aa'
mac = macaddr[:-2]
a = macaddr[-2:]
b = int(a,16)+1
if b in range(10):
    c = hex(b)[2:]
    c = '0' +str(c)
else:
    c = hex(b)[2:]
    if len(c) == 1:
        c = '0' + c
#c = hex(b)[-2:]
# c = hex(b).split('x')[-2]  -> '94'
new = mac+c
print macaddr
print new.upper()


