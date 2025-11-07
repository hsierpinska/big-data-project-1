#!/usr/bin/env python3
import sys

last_key = None
sum_count = 0
sum_age = 0

for line in sys.stdin:
    line = line.strip()
    key, value = line.split("\t", 1)
    count, age = map(int, value.split(","))

    if last_key == key:
        sum_count += count
        sum_age += age
    else:
        if last_key:
            print(f"{last_key}\t{sum_count},{sum_age}")
        sum_count = count
        sum_age = age
        last_key = key

if last_key:
    print(f"{last_key}\t{sum_count},{sum_age}")
