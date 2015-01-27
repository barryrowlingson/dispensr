from dd import def_dict
import csv

def read_postcodes(pcfile):
    """ read postcodes into a lookup table """

    location_lookup = def_dict((-9999,-9999))

    loop over lines in pcfile:
        postcode = get field from line
        (lat coordinate, lon coordinate) = fields from line
        location_lookup[postcode] = (lat coordinate, lon coordinate)
    return location_lookup

