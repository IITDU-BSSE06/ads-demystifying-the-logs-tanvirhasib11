#!/usr/bin/python
import sys

maximum=0
total_sales = 0
Key1 = None
name_path1=""
name_file=""

for line in sys.stdin:
    mapping_data = line.strip().split("\t")
    if len(mapping_data) != 2:
        continue

    Key, fullPath = mapping_data

    if Key1 and Key1 != Key:
        Key1 = Key;
        if total_sales > maximum:
            maximum=total_sales
            name_file=Key
            name_path1=fullPath
        total_sales = 0

    Key1 = Key
    total_sales += 1

print name_file+'\t'+ name_path1
