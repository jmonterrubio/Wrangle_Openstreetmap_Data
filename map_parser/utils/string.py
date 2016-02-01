'''
Created on 31/01/2016

@author: jmonterrubio
'''

import re
import unicodedata

problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

def normalize(s):
    return ''.join((c for c in unicodedata.normalize('NFD', unicode(s)) if unicodedata.category(c) != 'Mn')).encode('ascii','ignore').replace ("_", " ").lower()

def contains_problematic_characters(tag_key):
    return problemchars.search(tag_key)