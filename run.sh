#!/bin/bash

if [ -z ${1} ]; then echo "missing file"; exit 1; fi

cat ${1} | docker run --rm -i zanasufiit/tabulate-form-csv
