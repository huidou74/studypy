#!/usr/bin/python
import os

def isNum(s):           #定义函数     
    if s.isdigit():     #判断这个形参是否为数字
        return True     #如果它是数字,返回一个True
    return False        #如果它不是数字,返回一个False

for i in os.listdir('/proc'):   #用一个方法去读取该目录下的所有文件名
    if isNum(i):               #调用这个函数,传递一个变量给函数,会有返回值
       print i             #如果上面的函数返回了一个true,则打印这个值,否则不打印
   
