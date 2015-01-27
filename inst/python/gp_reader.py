#!/bin/env python

import csv
from dd import def_dict
from postcodes import fix_postcode
import sys

def read_GP_address(gpfile, location_lookup):
    """
    GP address file is like this:
    201406,A81001,THE DENSHAM SURGERY  ,THE HEALTH CENTRE  ,LAWSON STREET  ,STOCKTON ,CLEVELAND    ,TS18 1HU
     [0]    [1]          [2]              ..........................................                  [7]
    
    """
    PCFIELD=7
    GPFIELD=1

    gp_lookup = def_dict((-9999,-9999,"QQ11QQ"))
    with open(gpfile, "rb") as csvfile:
        gpreader = csv.reader(csvfile)
        for line in gpreader:

            postcode = fix_postcode(line[PCFIELD])
            (lat, lon) = location_lookup[postcode]

            practice_code = line[GPFIELD] 
            gp_lookup[practice_code] = (lat, lon, postcode)

    return gp_lookup

def main(args):
    from postcodes import read_postcodes
    print "reading postcodes"
    pclookup = read_postcodes(args[2])
    print "reading and matching GP postcodes"
    gplookup = read_GP_address(args[1], pclookup)
    print "X12345:", gplookup["X12345"], " doesnt exist"
    print "Y02504:", gplookup["Y02504"], " should exist"
    missing = 0
    for k,v in gplookup.iteritems():
        if v[0]<0:
            missing = missing + 1
    print "Total %s with %s missing" % (len(gplookup.keys()), missing)


if __name__=="__main__":
    if len(sys.argv)!=3:
        print "Usage: gp_reader <address file> <postcode file>"
    else:
        main(sys.argv)


