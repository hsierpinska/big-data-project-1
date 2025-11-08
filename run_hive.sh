#!/bin/bash

input_dir3=$1
input_dir4=$2
output_dir6=$3

beeline -n ${USER} -u jdbc:hive2://localhost:10000/default -f hive.hql \
  --hiveconf input_dir3=$input_dir3 \
  --hiveconf input_dir4=$input_dir4 \
  --hiveconf output_dir6=$output_dir6