#!/usr/bin/python
#-*- coding:utf-8 -*-
# fd = open("/tmp/123")
# while True:
#     line = fd.readline()
#     if not line:
#         break
#     print line,
# fd.close()

#a = {'a':'333'}
#with open("/tmp/aaa",'a') as fd:
#    fd.write(str(a))
#    while True:
#        line = fd.readline()
#        if not line:
#            break
#        print line


with open("/tmp/mysql1") as fd:
    while True:
        line = fd.readlines()
        if not line:
            break
        aa = line
        a = line.pop(3)
print aa
n = list(a.split())
del n[2]
n.insert(2,"333")
print a,n
nn = '         '.join(n)
aa.insert(3,(nn+'\n'))
print aa
with open("/tmp/mysql2","w") as dd_df:
    for i in aa:
        dd_df.write(i)

         
   
        


    







#with open("/tmp/aaa") as fd:
#    while True:
#        line = fd.readlines()
#        if not line:
#            break
#        a = eval(line[0])
#        b = eval(line[1])
#a.update(b)

#print a

#with open("/tmp/aaa1",'w') as n_fd:
#    n_fd.write(str(a))       


#print a
#with open("/etc/motd") as fd:
#    while True:
#        line = fd.readline()
#        if not line:
#            break
#        print line,




