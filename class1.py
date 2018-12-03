#!/usr/bin/python
#coding:utf8
class People(object):   
    color = 'yellow' 
    __age = 30     #前面加两个__ 为私有属性，只能内部使用   
       
    def think(self):      
        self.color = "black"     
        print "I am a %s" % self.color   
        print "i am a thinker"
        print self.__age     #调用私有属性

ren = People()      #将类实体化
ren.color = 'aaa'   #对象内的color属性重新赋值
print ren.color   #输出这个对象被新赋值的属性
print People.color     #调用类里的属性，是原来的值，是因为类实体化之前之后是不同的个体

print '-' *50

ren.think()     #调用对象里的方法

print '-' *50

print ren.__dict__       #通过对象调用公有的属性，保存到字典里输出
 
print People.__dict__    #通过类调用内置属性，公私有属性全部保存到字典输出         

print '-' *50

print ren._People__age  #以这种方法查看对象里的私有属性，测试用
