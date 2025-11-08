#!/usr/bin/env python3
import sys

last_key = None
total_count = 0
total_age = 0

for line in sys.stdin:
    line = line.strip()
    # pomijamy puste linie
    if not line:
        continue  

    try:
        key, value = line.split("\t", 1)
        count, age = map(int, value.split(","))
    except (ValueError, IndexError):
        continue  # pomijamy wiersze w złym formacie

    if last_key == key:
        total_count += count
        total_age += age
    else:
        if last_key is not None:
            avg_age = total_age / total_count  # obliczamy średni wiek
            # emitujemy wynik
            print(f"{last_key}\t{total_count},{avg_age:.1f}")  
        total_count = count
        total_age = age
        last_key = key

# emitujemy wynik dla ostatniego klucza
if last_key is not None:
    avg_age = total_age / total_count
    print(f"{last_key}\t{total_count},{avg_age:.1f}")
