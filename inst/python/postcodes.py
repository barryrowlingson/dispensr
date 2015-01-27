#!/bin/env python
#
from dd import def_dict
import csv
import sys

def fix_postcode(pc):
    """ convert postcodes to standard form
    
    standard form is upper case with no spaces

    >>> pcs = ["LA1 4YF", "LA14YF", "   LA1 4YF", "L A 1 4 Y f"]
    >>> [fix_postcode(pc) for pc in pcs]
    ['LA14YF', 'LA14YF', 'LA14YF', 'LA14YF']
    """
    return pc.upper().replace(" ","")


def read_postcodes(pcfile, default=(-9999,-9999)):
    """ read postcodes into a lookup table 

    Postcode format is all the postcodes in one "pc, x, y" file:

    "AB101AA",394251,806376
    "AB101AB",394232,806470
    "AB101AF",394181,806429

    with no header and only the postcode field quoted, although 
    the csv module should cope with minor differences.

    """

    # return a default value for a missing postcode:
    location_lookup = def_dict(default)

    with open(pcfile, "rb") as csvfile:
        pcreader = csv.reader(csvfile)
        for line in pcreader:
            postcode = fix_postcode(line[0])
            (lat , lon ) = (int(line[1]),int(line[2]))
            location_lookup[postcode] = (lat , lon )
    return location_lookup


def main(args):
    """ simple test of reading a postcode file into a lookup """
    lookup = read_postcodes(args[1])
    print lookup["LA1 4YF"] # returns default because not in standard form
    print lookup[fix_postcode("LA1 4YF")] # should work

if __name__=="__main__":
    if len(sys.argv)!=2:
        print "Usage: postcodes <postcode file>"
    else:
        main(sys.argv)

        
