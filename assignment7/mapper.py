#!/usr/bin/python
import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data)> 1:
        method = data[5]
print str(method)
