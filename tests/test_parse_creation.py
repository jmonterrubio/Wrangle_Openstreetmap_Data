# coding=utf-8
'''
Created on 30/01/2016

@author: jmonterrubio

Creation parsing tests
'''

import unittest
from map_parser.map import creation

ONE_CREATION_VERSION_GOOD = '1'
ONE_CREATION_CHANGESET_GOOD = '111111'
ONE_CREATION_TIMESTAMP_GOOD = '2012-03-06T16:33:18Z'
ONE_USER_NAME_GOOD = 'pepe lopez'
ONE_USER_UID_GOOD = '112233'
UNKNOWN_CREATION_FIELD = 'unknown'

class TestsParseCreation(unittest.TestCase):
    
    # Parse correctly a well defined creation version
    def test_parse_creation_version(self):
        a_creation = {}
        a_creation['version'] = ONE_CREATION_VERSION_GOOD
        parsed_creation = {}
        creation.fill(parsed_creation, 'version', ONE_CREATION_VERSION_GOOD)
        self.assertEqual(parsed_creation, a_creation)
    
    # Parse correctly a well defined creation changeset
    def test_parse_creation_changeset(self):
        a_creation = {}
        a_creation['changeset'] = ONE_CREATION_CHANGESET_GOOD
        parsed_creation = {}
        creation.fill(parsed_creation, 'changeset', ONE_CREATION_CHANGESET_GOOD)
        self.assertEqual(parsed_creation, a_creation)
    
    # Parse correctly a well defined creation timestamp
    def test_parse_creation_timestamp(self):
        a_creation = {}
        a_creation['timestamp'] = ONE_CREATION_TIMESTAMP_GOOD
        parsed_creation = {}
        creation.fill(parsed_creation, 'timestamp', ONE_CREATION_TIMESTAMP_GOOD)
        self.assertEqual(parsed_creation, a_creation)
    
    # Parse correctly a well defined creation uid
    def test_parse_creation_uid(self):
        a_creation = {}
        a_creation['uid'] = ONE_USER_UID_GOOD
        parsed_creation = {}
        creation.fill(parsed_creation, 'uid', ONE_USER_UID_GOOD)
        self.assertEqual(parsed_creation, a_creation)
    
    # Parsing is not adding unknown fields
    def test_parse_creation_unknown_field(self):
        a_creation = {}
        parsed_creation = {}
        creation.fill(parsed_creation, UNKNOWN_CREATION_FIELD, '')
        self.assertEqual(parsed_creation, a_creation)

if __name__ == '__main__':
    unittest.main()