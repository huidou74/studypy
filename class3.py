#!/usr/bin/python
#coding:utf8
class People(object):   
    color = 'yellow' 
    __age = 30     
       
    def think(self):      
        self.color = "black"     
        print "I am a %s" % self.color   
        print "i am a thinker"
        print self.__age    
        
#        self.__aaa()   #调用私有方法
     
    def __aaa(self):    # 私有方法，只能内部调用
        print "使用私有方法 "
 
    def axx(self):      #需要使用到一个类的方法内部调用才可以访问到内部的私有方法
        self.__aaa()

      
    @classmethod
    def test(x):
        print  x.color
        print "动态方法"

    @staticmethod
    def test1():   
        print "静态方法"

print "通过实体化后的类访问"
abc = People()
abc.test()
abc.test1()
print "---------------------"

print "通过类访问的"
People.test()
People.test1()

print "---------------------"

abc.axx()
