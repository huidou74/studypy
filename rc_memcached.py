#!/usr/bin/python
#coding:utf-8
import os
import sys
from subprocess import Popen, PIPE

class Process(object):
    def __init__(self, name, program, args, workdir):
        self.name = name
        self.program = program
        self.args = args
        self.workdir = workdir
    
    def _init(self):
        if not os.path.exists(self.workdir):
            os.mkdir(self.workdir)
            os.chdir(self.workdir)

    def _writePid(self):
        if self.pid:
            with open(self._pidFile(),'w') as fd:
                fd.write(str(self.pid))

    def _pidFile(self):
        return os.path.join(self.workdir, "%s.pid" % self.name) 
    
    def _getPid(self):
        p = Popen(['pidof',self.name], stdout=PIPE)
        pid = p.stdout.read().strip()    
        return pid

    def start(self):
        pid = self._getPid()
        if pid :
            print "%s is running . PID: %s" % (self.name,pid)
            sys.exit()
        self._init()
        cmd = self.program + ' ' + self.args
        p = Popen(cmd,stdout=PIPE,shell=True)
        self.pid = p.pid
        self._writePid()
        print "%s start Sucessful ! %s pid: %s " % (self.name,self.name,self.pid)
  
    def stop(self):
        pid = self._getPid()
        if pid:
            os.kill(int(pid),15)
            if os.path.exists(self._pidFile()):
                os.remove(self._pidFile())
                print "%s is stop" % self.name

    def restart(self):
        self.stop()
        self.start()
        
    def status(self):
        pid = self._getPid()
        if pid:
            print "%s is running ! pid: %s" % (self.name,pid)
        else :
            print "%s is not running" % self.name    
    
    def help(self):
        print "Usage: %s {start|stop|status|restart}" % __file__

def main():
    name = 'memcached'
    prog = '/usr/bin/memcached'
    args = '-u memcached -p 11211 -c 1024 -m 64'
    wd = '/var/run/memcached'
    pm = Process(name = name, 
             program = prog, 
             args = args,
             workdir = wd)
    try:
        cmd = sys.argv[1]
    except IndexError, e:
        print "Option error!"
        sys.exit()
    if cmd == 'start':
        pm.start()
    elif cmd == 'stop':
        pm.stop()
    elif cmd == 'restart':
        pm.restart()
    elif cmd == 'status':
        pm.status()
    else:
        pm.help()
       



if __name__ == '__main__':
    main()







