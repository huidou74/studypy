#!/usr/bin/python
import os
user = raw_input("input you user : ")
ip = input("input the ip   : ")
class Sshd():
  def __init__(self,read_user,read_ip):
    self.read_user = read_user
    self.read_ip = read_ip
  def ssh(self):
    return os.system('ssh')
 
d_l = Sshd(user,ip)
