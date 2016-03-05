# coding=utf-8
'''
Created on 30/01/2016

@author: jmonterrubio
'''

import unittest
from map_parser.map import region

ONE_GOOD_REGION = 'Liérganes;Santander;Cantabria;España;Europa'
BAD_REGION_WITH_COMMAS = 'Liérganes,Santander,Cantabria,España,Europa'
BAD_REGION_NOT_SPANISH = 'Liérganes;Santander;Cantabria;Spain;Europe'
BAD_REGION_MISSING_ENTITIES = 'Liérganes;Santander;Cantabria'
BAD_REGION_WITH_DUPLICATES = 'Liérganes;Santander;Cantabria;Cantabria;España;Europa'
BAD_REGION_INCORRECT_ORDER = 'Europa;España;Liérganes;Santander;Cantabria'

class TestsParseRegion(unittest.TestCase):
        
    def test_parse_region(self):
        a_region = {}
        a_region[region.REGION_KEY] = ONE_GOOD_REGION
        parsed_region = {}
        region.fill(parsed_region, region.REGION_KEY, ONE_GOOD_REGION)
        self.assertEqual(parsed_region, a_region)
     
    def test_not_contains_commas(self):
        a_region = {}
        a_region[region.REGION_KEY] = ONE_GOOD_REGION
        parsed_region = {}
        region.fill(parsed_region, region.REGION_KEY, BAD_REGION_WITH_COMMAS)
        self.assertEqual(parsed_region, a_region)
     
    def test_spanish_language(self):
        a_region = {}
        a_region[region.REGION_KEY] = ONE_GOOD_REGION
        parsed_region = {}
        region.fill(parsed_region, region.REGION_KEY, BAD_REGION_NOT_SPANISH)
        self.assertEqual(parsed_region, a_region)
         
    def test_contains_known_entities(self):
        parsed_region = {}
        region.fill(parsed_region, region.REGION_KEY, BAD_REGION_MISSING_ENTITIES)
        self.assertTrue('España' in parsed_region[region.REGION_KEY])
        self.assertTrue('Europa' in parsed_region[region.REGION_KEY])
         
    def test_not_contains_duplicates(self):
        a_region = {}
        a_region[region.REGION_KEY] = ONE_GOOD_REGION
        parsed_region = {}
        region.fill(parsed_region, region.REGION_KEY, BAD_REGION_WITH_DUPLICATES)
        self.assertEqual(parsed_region, a_region)
        
    def test_has_correct_entities_order(self):
        a_region = {}
        a_region[region.REGION_KEY] = ONE_GOOD_REGION
        parsed_region = {}
        region.fill(parsed_region, region.REGION_KEY, BAD_REGION_INCORRECT_ORDER)
        self.assertEqual(parsed_region, a_region)

if __name__ == '__main__':
    unittest.main()