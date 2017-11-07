#!/usr/bin/python
import sys

for line in sys.stdin:
    data = line.strip().split("GET ")
    if len(data)> 1:
        hitadrs = str(data[1])
        print "{0}\t{1}".format(hitadrs, 1)
