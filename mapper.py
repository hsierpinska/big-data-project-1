# prosty test 
# cat input.txt | ./mapper.py | sort | ./reducer.py > output.txt

import sys
for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        value = 1
        print( "%s\t%d" % (word, value) )


