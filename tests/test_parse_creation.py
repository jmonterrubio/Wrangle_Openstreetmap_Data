# coding=utf-8
'''
Created on 30/01/2016

@author: jmonterrubio
'''

import unittest
from map_parser.map import creation

ONE_CREATION_VERSION_GOOD = '1'
ONE_CREATION_CHANGESET_GOOD = '111111'
ONE_CREATION_TIMESTAMP_GOOD = '2012-03-06T16:33:18Z'
ONE_USER_NAME_BAD = 'Pepe_López'
ONE_USER_NAME_GOOD = 'pepe lopez'
ONE_USER_UID_GOOD = '112233'
UNKNOWN_CREATION_FIELD = 'unknown'

class TestsParseCreation(unittest.TestCase):
        
    def test_parse_creation_version(self):
        a_creation = {}
        a_creation['version'] = ONE_CREATION_VERSION_GOOD
        parsed_creation = {}
        creation.fill(parsed_creation, 'version', ONE_CREATION_VERSION_GOOD)
        self.assertEqual(parsed_creation, a_creation)
    
    def test_parse_creation_changeset(self):
        a_creation = {}
        a_creation['changeset'] = ONE_CREATION_CHANGESET_GOOD
        parsed_creation = {}
        creation.fill(parsed_creation, 'changeset', ONE_CREATION_CHANGESET_GOOD)
        self.assertEqual(parsed_creation, a_creation)
        
    def test_parse_creation_timestamp(self):
        a_creation = {}
        a_creation['timestamp'] = ONE_CREATION_TIMESTAMP_GOOD
        parsed_creation = {}
        creation.fill(parsed_creation, 'timestamp', ONE_CREATION_TIMESTAMP_GOOD)
        self.assertEqual(parsed_creation, a_creation)
        
    def test_normalize_user_name(self):
        self.assertEqual(creation.normalize_name(ONE_USER_NAME_BAD), ONE_USER_NAME_GOOD)
        
    def test_parse_creation_uid(self):
        a_creation = {}
        a_creation['uid'] = ONE_USER_UID_GOOD
        parsed_creation = {}
        creation.fill(parsed_creation, 'uid', ONE_USER_UID_GOOD)
        self.assertEqual(parsed_creation, a_creation)
    
    def test_parse_user_name(self):
        a_creation = {}
        a_creation['user'] = ONE_USER_NAME_GOOD
        parsed_creation = {}
        creation.fill(parsed_creation, 'user', ONE_USER_NAME_BAD)
        self.assertEqual(parsed_creation, a_creation)
    
    def test_parse_creation_unknown_field(self):
        a_creation = {}
        parsed_creation = {}
        creation.fill(parsed_creation, UNKNOWN_CREATION_FIELD, '')
        self.assertEqual(parsed_creation, a_creation)

if __name__ == '__main__':
    unittest.main()