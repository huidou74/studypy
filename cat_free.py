#!/usr/bin/python
with open("/proc/meminfo") as fd:
    for line in fd:
        if line.startswith("MemTotal"):
            total = line.split()[1]
            continue
        if line.startswith("MemFree"):
            free = line.split()[1]
            break
print total,free
print "%.2f" % (int(total)/1024.0) + " M"
print "%.2f" % (int(free)/1024.0) + " M"
