#!/bin/env python

import sys
import csv

from dd import def_dict

def read_chemicals(chemfile):
    chem_lookup = def_dict("Unknown Chemical Code")
    with open(chemfile,"rb") as csvfile:
        chemreader = csv.reader(csvfile)
        chemreader.next() # skip header
        for line in chemreader:
            chem_lookup[line[0]]=line[1].strip()
    return chem_lookup

if __name__ == "__main__":
    read_chemicals(sys.argv[1])

