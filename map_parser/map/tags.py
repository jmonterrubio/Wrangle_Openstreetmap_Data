'''
Created on 31/01/2016

@author: jmonterrubio
'''

import address
from utils import string 

def fill_string(d, key, value):
    if value:
        d[key] = string.normalize(value)

def fill(d, key, value):
    if key != 'undefined' and value:
        d[key] = value
        
    
def parse(node, element):
    addr = {}
    for tag in element.iter("tag"):
        if string.contains_problematic_characters(tag.attrib['k']):
            continue
        if address.fill(addr, tag.attrib['k'], tag.attrib['v']):
            continue
        fill(node, tag.attrib['k'], tag.attrib['v'])
    fill(node, 'address', addr)