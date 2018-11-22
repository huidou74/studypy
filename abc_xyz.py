#!/usr/bin/python
import itertools
#for a in itertools.permutations('abc'):
#    print a[0], a[1], a[2]
#    if ( a[0] != 'a' ) and (a[-1] != 'a' ) and (a[-1] != 'c'):
#        print "x vs %s, y vs %s, z vs %s" % (a[0], a[1], a[2])
for i in itertools.permutations('xyz'):
    if (i[0] != 'x') and (i[-1] != 'z') and (i[-1] != 'x'):
        print "a vs %s, b vs %s, c vs %s" % (i[0], i[1], i[2])
