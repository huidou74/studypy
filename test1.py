#!/usr/bin/python
import random
num = random.randint(1,20)
print ("OK, play my game")
for i in range(1,7):
    a = input("please input the number :")
    if a >= 1 and a <= 20:
        if num > a:
            print ("input the number is small !")
            print ("keep trying !"), i
        elif num < a:
            print ("input the number is big ! ")
            print ("keep trying !"), i
        elif num == a: 
            print ("Congratulations ! you win ! input the number is True !")
            print ("the system num is "),num
            break
    else :
        print "please input the number within 20 !"
    if i == 6: 
            print ("game is over ,you loss! the number is "),num 
