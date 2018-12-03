#!/usr/bin/python
#-*- coding:utf-8 -*-
class People(object):     # 定义类(class)，object可以有，也可以没有
    color = 'yellow'      #定义了一个静态属性

    def think(self):      #定义了一个动态方法，这个方法里一定要有self，还可以带多个属性
        self.color = "black"     #如果需要调用类里的属性，就要用到self.color来调用该静态属性
        print "I am a %s" % self.color    #调用动态方法时的输出
        print "i am a thinker"

ren = People()      #将类赋值给'ren'这个变量，就是一个对象，即为将类实例化

print ren           # 单纯打印这个'ren'变量是一个对象(object)，所以将类实例化后的便是对象(object)

print ren.color     #输出，'ren'对象的静态属性，

ren.think()         #使用这个类里面的.think()方法
