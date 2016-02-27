'''
Created on 31/01/2016

@author: jmonterrubio
'''

import creation
import position
from utils import string

def fill_string(d, key, value):
    if value:
        d[key] = string.normalize(value)

def fill(d, key, value):
    if value:
        d[key] = value
        
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