#!/usr/bin/python 
#coding:utf8

class MyClass(object):
    name = 'Test'

    def __init__(self):     #如果加了内部的构造函数，即当前的类别实例化会，
        self.func1()           #会自动加载，并初始化里面的内容 
        self.__func2()
        self.classFun()
        self.staticFun()

    def func1(self):
        print self.name,
        print "我是公有方法"
       # self.__func2()

    def __func2(self):
        print self.name,
        print "我是私有方法"

    @classmethod      #修饰器，这样就将类里的方法，转为类方法然后外部调用
    def classFun(self):
        print self.name,
        print "我是类方法"
    
    @staticmethod    #修饰器
    def staticFun():     #静态方法不能有 self 方法
        print MyClass.name,    #因为是静态的，需要类名来调用
        print "我是静态方法"

mc = MyClass()    #实例化

# mc.func1()

# mc.__fun2()   #直接调用不行。必须在内部调用,在func1里面调用才可以


# MyClass.classFun()    #类方法，需要加修饰器才可以再外部调用

# MyClass.staticFun()   #静态方法，需要加修饰器才可以再外部调用
