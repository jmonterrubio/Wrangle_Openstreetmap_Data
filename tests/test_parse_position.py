# coding=utf-8
'''
Created on 30/01/2016

@author: jmonterrubio

Position parsing tests
'''

import unittest
from map_parser.map import position

ONE_POSITION_LAT_GOOD = 1.0
ONE_POSITION_LON_GOOD = 2.0

UNKNOWN_POSITION_FIELD = 'unknown'

class TestsParsePosition(unittest.TestCase):
    
    # Parse correctly a well defined position
    def test_parse_position(self):
        a_position = [ONE_POSITION_LAT_GOOD,ONE_POSITION_LON_GOOD]
        parsed_position = []
        position.fill(parsed_position, 'lat', ONE_POSITION_LAT_GOOD)
        position.fill(parsed_position, 'lon', ONE_POSITION_LON_GOOD)
        self.assertEqual(parsed_position, a_position)
        
    # Parsing is checking correct order
    def test_parse_position_reverse_parsing_order(self):
        a_bad_position = [ONE_POSITION_LON_GOOD,ONE_POSITION_LAT_GOOD]
        parsed_position = []
        position.fill(parsed_position, 'lon', ONE_POSITION_LON_GOOD)
        position.fill(parsed_position, 'lat', ONE_POSITION_LAT_GOOD)
        self.assertNotEqual(parsed_position, a_bad_position)
    
    # Parsing is not adding unknown fields
    def test_parse_position_unknown_field(self):
        a_position = [ONE_POSITION_LAT_GOOD,ONE_POSITION_LON_GOOD]
        parsed_position = [ONE_POSITION_LAT_GOOD,ONE_POSITION_LON_GOOD]
        position.fill(parsed_position, UNKNOWN_POSITION_FIELD, '')
        self.assertEqual(parsed_position, a_position)

if __name__ == '__main__':
    unittest.main()