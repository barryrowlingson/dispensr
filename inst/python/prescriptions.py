#!/bin/env python
import sys
import os

import postcodes
import gp_reader
import chem_reader
import progress

import csv

class pdata(object):   
    fields = [
        "sha",
        "pct",
        "practice",
        "bnfcode",
        "bnfname",
        "chemical_code",
        "chemical_name",
        "product",
        "generic",
        "equivalent",
        "items",
        "nic",
        "act_cost",
        "quantity",
        "period",
        "xgrid",
        "ygrid",
        "postcode"]
    def writeline(self):
        parts = [str(getattr(self,x)).strip() for x in pdata.fields]
        print ",".join(parts)
    @classmethod
    def writeheader(cls):
        print ",".join(pdata.fields)

def read_prescriptions(Prescriptions, gplookup, chemlookup):
    """ 
    for each line of the prescription file:
      get location and postcode from gplookup table
      get chemical from chemlookup table
      process BNF code into components
      print comma-separated record to output
    """
    f_info = os.stat(Prescriptions)
    size = f_info.st_size

    with open(Prescriptions, "rb") as csvfile:
        preader = csv.reader(csvfile)
        preader.next() # skip header
        pdata.writeheader()
        linecount=0
        for line in preader:
            linecount = linecount + 1
            if linecount % 1000 == 0:
                progress.progress(csvfile.tell(), size)
            o = pdata()
            o.sha = line[0]
            o.pct = line[1]
            o.practice = line[2]
            o.bnfcode = line[3]
            o.bnfname = line[4]
            o.items = line[5]
            o.nic = line[6]
            o.act_cost = line[7]
            o.quantity = line[8]
            o.period = line[9]
            o.chemical_code = o.bnfcode[0:9]
            o.chemical_name = chemlookup[o.chemical_code]
            o.product = o.bnfcode[9:11]
            o.generic = (o.product == "AA")
            o.equivalent = o.chemical_code + "AA" + o.bnfcode[13:15] + o.bnfcode[13:15]
            (o.xgrid, o.ygrid, o.postcode) = gplookup[o.practice]
            o.writeline()

            

    pass

def main(args):
    print >> sys.stderr, "Reading postcodes..."
    pclookup = postcodes.read_postcodes(args[3])
    print >> sys.stderr, "Reading addresses..."
    gplookup = gp_reader.read_GP_address(args[2], pclookup)
    print >> sys.stderr, "Reading chemicals..."
    chemlookup = chem_reader.read_chemicals(args[4])
    print >> sys.stderr, "Processing prescriptions..."
    read_prescriptions(args[1], gplookup, chemlookup)


if __name__=="__main__":
    if len(sys.argv)!=5:
        print "Usage: prescriptions <Prescription File> <Address file> <Postcode file> <Chemical file>"
    else:
        main(sys.argv)

