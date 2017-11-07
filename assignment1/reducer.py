#!/usr/bin/python

import sys
num = 0
for line in sys.stdin:
	ip = line.strip()
	if ip == "10.99.99.186":
		num = num + 1
print num
