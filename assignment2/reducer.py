#!/usr/bin/python

import sys
number = 0
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue
    path, other = data_mapped
    if '/assets/js/the-associates.js' in path:
     number = number + 1
print number
