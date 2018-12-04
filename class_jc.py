#!/usr/bin/python
#-*- coding:utf-8 -*-

class People(object):   #New Style  传统方式不加()
    color = 'yellow'
    
    def __init__(self, c): #父类的构造函数,如果self后跟了一个变量,则在继承的子类时需要重写这个构造函数然后引入这个值
        print "Init..."
        self.dwell = 'Earth'   #这是它的初始化变量

    def think(self):
        print "I am a %s" % self.color
        print "I am a thinker "

class Chinese(People):     #Chinese继承了People父类
    def __init__(self):      #则在继承的子类时需要重写这个构造函数然后引入这个值
#        People.__init__(self,'red')
	super(Chinese,self).__init__('red')
    pass

cn = Chinese()        #实例化调用这个类

print cn.color         #输出里面定义的变量

cn.think()        #还能通过继承的类，访问它内部的函数


print cn.dwell   #也是会执行内部初始化的变量
