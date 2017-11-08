#!/usr/bin/python
import sys

maximum=0
total = 0
Key1 = None
name_path1="http://www.the-associates.co.uk"
name_file="favicon.ico"

for line in sys.stdin:
    mapping_data = line.strip().split("\t")
    if len(mapping_data) != 2:
        continue

    Key, fullPath = mapping_data

    if Key1 and Key1 != Key:
        Key1 = Key;
        if total > maximum:
            maximum=total
            name_file=Key
            name_path1=fullPath
        total = 0

    Key1 = Key
    total += 1

print name_file+'\t'+ name_path1
