#!/usr/bin/env python3
import csv
import sys
for line in sys.stdin:
    line = csv.reader([line]).__next__()
    if line[0] == "visit_id":
        continue
    hospital_id = line[1]
    date = line[5]
    year = date.split("-")[0]
    age = line[6]
    print( "%s,%s\t%s,%s" % (hospital_id, year, 1, age) )