#!/usr/bin/env python3
import sys

last_key = None
current_count = 0
current_age_sum = 0

for line in sys.stdin:
    line = line.strip()
    # walidacja - pomijamy puste linie
    if not line:
        continue  

    try: # walidacja na błędne/niepełne dane
        key, value = line.split("\t", 1)
        count, age = map(int, value.split(","))
    except (ValueError, IndexError):
        continue 

    if last_key == key:
        current_count += count
        current_age_sum += age
    else:
        if last_key is not None:
            # emitujemy wynik
            print(f"{last_key}\t{current_count},{current_age_sum}")  
        current_count = count
        current_age_sum = age
        last_key = key

# emitujemy wynik dla ostatniego klucza
if last_key is not None:
    print(f"{last_key}\t{current_count},{current_age_sum}")
