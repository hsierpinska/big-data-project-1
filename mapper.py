#!/usr/bin/env python3
import csv
import sys
for line in sys.stdin:
    line = csv.reader([line]).__next__()
    # pominięcie nagłówka
    if line[0] == "visit_id":
        continue
    hospital_id = line[1]
    date = line[5]
    year = date.split("-")[0]
    age_str = line[6]

    # zapobieganie pustym danym (walidacja)
    if not date or not age_str:
            continue
    
    # próba konwersji wieku na int (walidacja)
    age = int(age_str)
    print( "%s,%s\t%s,%s" % (hospital_id, year, 1, age) )