'''
Created on 31/01/2016

@author: jmonterrubio

Attributes elements functions
'''

import creation
import position
from utils import string

#
# Set 'key' and string formatted 'value' into the 'd' map
#
def fill_string(d, key, value):
    if value:
        d[key] = string.normalize(value)

#
# Set 'key' and 'value' into the 'd' map
#
def fill(d, key, value):
    if value:
        d[key] = value

#
# Iterate over 'element' to fill inner node objects given special
# treatment 'created' and 'pos'
#
def parse(node, element):
    created = {}
    pos = []
    for key, value in element.items():
        if creation.fill(created, key, value):
            continue
        if position.fill(pos, key, value):
            continue
        fill_string(node, key, value)
    fill(node, 'created', created)
    fill(node, 'pos', pos)