'''
Created on 31/01/2016

@author: jmonterrubio
'''

def append(refs, value):
    refs.append(value)

def fill(d, key, value):
    if value:
        d[key] = value
    
def parse(node, element):
    refs = []
    for nd in element.iter("nd"):
        append(refs, nd.attrib['ref'])
    fill(node, 'node_refs', refs)