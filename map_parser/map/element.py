'''
Created on 31/01/2016

@author: jmonterrubio
'''

import attributes
import tags
import node_references
from utils import string

ELEMENTS = ['node', 'way']

def fill(d, key, value):
    if value:
        d[key] = value#string.normalize(value)
    
def shape(element):
    node = {}
    if element.tag in ELEMENTS:
        fill(node, 'type', element.tag)
        attributes.parse(node, element)
        tags.parse(node, element)
        node_references.parse(node, element)
        return node
    else:
        return None