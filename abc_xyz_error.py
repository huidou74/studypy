#!/usr/bin/python
list1 = ['a','b','c']
list2 = ['x','y','z']
dict1 = {}
dict2 = {}
dict1.fromkeys('abc',None)
dict2.fromkeys('xyz',None)
for i in list1:
    for j in list2:
        if (i != 'z'and i != 'x') and (j != 'a'and j != 'c'):
             dict1[i] = j
             dict2[j] = i
             if (len(dict1) == 3) and (len(dict2) == 3):
                 print ("----------") 
                 print dict1.items()
                 print dict2.items()
                         
