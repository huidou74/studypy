#!/usr/bin/python
import os
import sys

def print_dir(path):
    lsdir = os.listdir(path)
    dirs = [ i for i in lsdir if os.path.isdir(os.path.join(path, i)) ]
    files = [ i for i in lsdir if os.path.isfile(os.path.join(path, i))]
    if dirs:
        for d in dirs:
            print_dir(os.path.join(path, d))
    if files:
        for f in files:
            print os.path.join(path, f)

print_dir(sys.argv[1])
