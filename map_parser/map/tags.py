'''
Created on 31/01/2016

@author: jmonterrubio
'''

import address
import re

problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

def fill(d, key, value):
    if value:
        d[key] = value
        
def contains_problematic_characters(tag_key):
    return problemchars.search(tag_key)
    
def parse(node, element):
    addr = {}
    for tag in element.iter("tag"):
        if contains_problematic_characters(tag.attrib['k']):
            continue
        if address.fill(addr, tag.attrib['k'], tag.attrib['v']):
            continue
        fill(node, tag.attrib['k'], tag.attrib['v'])
    fill(node, 'address', addr)