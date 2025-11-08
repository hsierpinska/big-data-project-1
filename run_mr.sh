#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Użycie: $0 <input_dir> <output_dir>"
    exit 1
fi

INPUT_DIR=$1
OUTPUT_DIR=$2

hadoop fs -rm -r -skipTrash $OUTPUT_DIR

mapred streaming \
-files mapper.py,combiner.py,reducer.py \
-input $INPUT_DIR \
-output $OUTPUT_DIR \
-mapper mapper.py \
-combiner combiner.py \
-reducer reducer.py \