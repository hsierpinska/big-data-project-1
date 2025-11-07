#!/usr/bin/env python3
import sys

last_key = None
total_count = 0
total_age = 0

for line in sys.stdin:
    line = line.strip()
    key, value = line.split("\t", 1)
    count, age = map(int, value.split(","))

    if last_key == key:
        total_count += count
        total_age += age
    else:
        if last_key:
            avg_age = total_age / total_count
            print(f"{last_key}\t{total_count},{avg_age:.1f}")
        total_count = count
        total_age = age
        last_key = key

if last_key:
    avg_age = total_age / total_count
    print(f"{last_key}\t{total_count},{avg_age:.1f}")
