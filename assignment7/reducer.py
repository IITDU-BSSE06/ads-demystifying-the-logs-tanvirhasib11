#!/usr/bin/python
import operator
import sys
d = dict()
for line in sys.stdin:
    year = line.strip()
    if year in d:
      d[year] +=1
    else: 
      d[year] = 1

for keys in d:
print (keys,d[keys])
