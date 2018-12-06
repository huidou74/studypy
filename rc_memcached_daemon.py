#!/usr/bin/python
#coding:utf-8
import os
import sys
from subprocess import Popen, PIPE

class Process(object):
    args = {'PORT':'11211',
            'USER':'memcached',
            'MAXCONN':'1024',
            'CACHESIZE':'64',
            'OPTIONS':''}

    def _readConf(self, f):
        with open(f) as fd:
            lines = fd.readlines()
        return dict([i.strip().replace('"','').split("=") for i in lines])
    
    def _parseArgs(self):
        conf = self._readConf('/etc/sysconfig/memcached')
        if 'USER' in conf:
            self.args['USER'] = conf['USER']
        if 'PORT' in conf:
            self.args['PORT'] = conf['PORT']
        if 'MAXCONN' in conf:
            self.args['MAXCONN'] = conf['MAXCONN']
        if 'CACHESIZE' in conf:
            self.args['CACHESIZE'] = conf['CACHESIZE']
        option = ['-u', self.args['USER'],
                  '-p', self.args['PORT'],
                  '-c', self.args['CACHESIZE'],
                  '-m', self.args['MAXCONN']]
        os.system('chown %s %s' % (self.args['USER'], self.workdir))
        return option

    def __init__(self, name, program, workdir):
        self.name = name
        self.program = program 
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
        cmd = [self.program] + self._parseArgs() + ['-d','-P',self._pidFile()]  #列表更安全。[]+[]=[...]几个小列表组合成大列表
        p = Popen(cmd,stdout=PIPE)  #如果上面的cmd传下来的是列表,那么这里的shell=Ture 可以去掉,默认为False
        print "%s start Sucessful ! " % self.name
  
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
    wd = '/var/run/memcached'
    pm = Process(name = name, 
             program = prog, 
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

