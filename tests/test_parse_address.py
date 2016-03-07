# coding=utf-8
'''
Created on 30/01/2016

@author: jmonterrubio

Address parsing tests
'''

import unittest
from map_parser.map import address

ONE_GOOD_CITY = 'City'

UNKNOWN_ADDRESS_FIELD = 'address:'
BAD_ADDRESS_FIELD = 'addr:city:info'

class TestsParseAddress(unittest.TestCase):
    
    # Parse correctly a well defined address
    def test_parse_address(self):
        an_address = {}
        an_address['city'] = ONE_GOOD_CITY
        parsed_address = {}
        address.fill(parsed_address, 'addr:city', ONE_GOOD_CITY)
        self.assertEqual(parsed_address, an_address)
    
    # Parse correctly an address with bad fields
    def test_parse_address_bad_field(self):
        an_address = {}
        parsed_address = {}
        address.fill(parsed_address, BAD_ADDRESS_FIELD, '')
        self.assertEqual(parsed_address, an_address)
    
    # Parsing is not adding unknown fields
    def test_parse_address_unknown_field(self):
        an_address = {}
        parsed_address = {}
        address.fill(parsed_address, UNKNOWN_ADDRESS_FIELD, '')
        self.assertEqual(parsed_address, an_address)

if __name__ == '__main__':
    unittest.main()