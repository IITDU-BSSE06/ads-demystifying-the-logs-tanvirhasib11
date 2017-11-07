#!/usr/bin/python
import sys

unique_Files=0
Key1 = None

for line in sys.stdin:
    mapping_data = line.strip().split("\t")
    if len(mapping_data) != 2:
        continue

    Key, fullPath = mapping_data

    if Key1 and Key1 != Key:
        unique_Files+=1
        Key1 = Key;
        total_sales = 0
    Key1 = Key

print str(unique_Files)
