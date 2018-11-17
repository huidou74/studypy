#!/usr/bin/python
for i in xrange(1,10):
    for x in xrange(1,i+1):
        print "%sx%s=%s" % (i, x, i*x),
    print 

