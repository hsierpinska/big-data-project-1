# usage cat shrank-data-example.csv python3 mapper.py 

#     line = line.strip()

import csv
import sys
# for line in sys.stdin:
#     line = csv.reader([line]).__next__()
#     line = line.strip()
#     if line.startswith("visit_id"):
#         continue
#     fields = line.split(",")
#     hospital_id = fields[1]
#     date = fields[5]
#     year = date.split("-")[0]
#     age = fields[6]
#     print( "%s,%s\t%s,%s" % (hospital_id, year, 1, age) )

for line in sys.stdin:
    line = csv.reader([line]).__next__()
    if line[0] == "visit_id":
        continue
    hospital_id = line[1]
    date = line[5]
    year = date.split("-")[0]
    age = line[6]
    print( "%s,%s\t%s,%s" % (hospital_id, year, 1, age) )