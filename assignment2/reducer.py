#!/usr/bin/python
import sys

number = 0
for line in sys.stdin:
    mapping_data = line.strip().split("\t")
    if len(mapping_data) != 2:
        continue
    path, other = mapping_data
    if '/assets/js/the-associates.js' in path:
     number = number + 1
print number
