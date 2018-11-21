#!/usr/bin/python
i = raw_input("input the money: ")
i = float(i)/10000
# (i <= 10 )* 10%
if i <= 10:
    z = (i*0.1)*10000
    print (str("i<10   :") + str(z)) + " RMB"

# 10 - 20 
elif i >= 10 and i < 20:
    a = (i*0.1)*10000
    b = ((i-10)*0.1)*10000
    print str("i<10    :") + str(a) + " RMB"
    print str("20>i<10 :") + str(b) + " RMB"   
    print "total  :" ,a+b, 
    print "RMB"

#20 - 40
elif i >= 20 and i < 40:
    c = ((i-20)*0.05)*10000
    print str("40>i<20  :") + str(c) + " RMB"


#40 - 60
elif i >= 40 and i < 60:
    d = ((i-40)*0.03)*10000
    print str("60>i<40  :") + str(d) + " RMB"

#60 - 100 . >100
elif i >= 60 and i < 100:
    e = ((i-60)*0.015)*10000
    print str("100>i<60  :") + str(e) + " RMB"
elif i >= 100:
    f = ((i-100)*0.01)*10000
    print str("i>100    :") + str(f) + " RMB"
       

