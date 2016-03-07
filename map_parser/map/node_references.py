'''
Created on 31/01/2016

@author: jmonterrubio

Node references parsing functions
'''

#
# Append'value' into the references list
#
def append(refs, value):
    refs.append(value)

#
# Set 'key' and 'value' into the 'd' map
#
def fill(d, key, value):
    if value:
        d[key] = value

#
# Parse element objects into a new node
#
def parse(node, element):
    refs = []
    for nd in element.iter("nd"):
        append(refs, nd.attrib['ref'])
    fill(node, 'node_refs', refs)