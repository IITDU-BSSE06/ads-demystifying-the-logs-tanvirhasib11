#!/usr/bin/python
import urlparse
import sys

for line in sys.stdin:
	data_set = line.strip().split(" ")
	if len(data_set) == 10:
		dt0, dt1 ,dt2 ,dt3 ,dt4 ,dt5 ,dt6 ,dt7 ,dt8 ,dt9= data_set
		print "{0}\t{1}".format(dt6,dt6)

