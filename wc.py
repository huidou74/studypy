#!/usr/bin/python
def wordCount(s):
    chars = len(s)
    words = len(s.split())
    count = s.count('\n')
    print count,words,chars
if __name__ == '__main__':
    s = open('/etc/passwd').read()
    wordCount(s)
