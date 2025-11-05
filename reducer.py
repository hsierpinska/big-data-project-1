
# assume the input file is already sorted

# filename = 'example-red-input.txt'

#correct output
# abc123,2023	2,47.5
# abc123,2024	1,60.0
# xyz789,2023	2,35.0

# file = open(filename, 'r')
last_key = None
sum_count = 0
sum_age = 0
import sys
for line in sys.stdin:
    line = line.strip()
    key, value = line.split("\t", 1)
    visit_id = key.split(",")[0]
    year = int(key.split(",")[1])
    count = int(value.split(",")[0])
    age = int(value.split(",")[1])
    # kluczem jest para visit_id, year
    if last_key == key:
        sum_count += count
        sum_age += age
    else:
        if last_key:
            avg_age = sum_age / sum_count
            print( "%s\t%d,%.1f" % (last_key, sum_count, avg_age) )
        sum_count = count
        sum_age = age
        last_key = key
print( "%s\t%d,%.1f" % (last_key, sum_count, sum_age / sum_count) )

