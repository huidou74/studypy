#!/usr/bin/python

# fd = open("/tmp/123")
# while True:
#     line = fd.readline()
#     if not line:
#         break
#     print line,
# fd.close()



with open("/tmp/123") as fd:
    while True:
        line = fd.readline()
        if not line:
            break
        print line,



