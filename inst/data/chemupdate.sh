#!/bin/bash

file=$1

if [ ! -f "$file" ] ; then
echo No such file "$file"
exit 1
fi


awk -F, '{gsub(/[ \t]+$/, "", $2);print $1","$2}' < "$file" | psql maps -c "COPY chemicals (chemsub, code) from STDIN WITH delimiter ',' CSV HEADER;"

