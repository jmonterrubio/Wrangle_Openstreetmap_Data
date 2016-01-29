'''
Created on 28/1/2016

@author: jmonterrubio
'''

import xml.etree.cElementTree as ET
import re
import codecs
import json


lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

CREATED = [ "version", "changeset", "timestamp", "user", "uid"]
POSITION = [ "lat", "lon"]


    

def audit_created_attribute(created_attrs, created_name, created_value):
    if created_name in CREATED:
        created_attrs[created_name] = created_value
        return True
    return False
        
def audit_position_attribute(position_attrs, position_name, position_value):
    if position_name in POSITION:
        position_attrs.insert(POSITION.index(position_name),float(position_value))
        return True
    return False

def audit_regular_attribute(regular_attrs, regular_name, regular_value):
    regular_attrs[regular_name] = regular_value
    
def set_attributes(node, created_attrs, position_attrs):
    if created_attrs:
        node["created"] = created_attrs
    if position_attrs:
        node["pos"] = position_attrs

def set_address(node, address):
    if address:
        node["address"] = address
        
def contains_problematic_characters(tag_key):
    return problemchars.search(tag_key)

def audit_address(address, key, value):
    if key.startswith('addr:'):
        if key.count(':') == 1:
            address[key[5:]] = value
        return True
    return False

def audit_regular(regulars, key, value):
    regulars[key] = value

def audit_node_references(refs, value):
    refs.append(value)
    
def set_refs(node, refs):
    if refs:
        node["node_refs"] = refs
    
def shape_element(element):
    node = {}
    created_attrs = {}
    position_attrs = []
    if element.tag == "node" or element.tag == "way" :

        node["type"] = element.tag
        for name, value in element.items():
            if audit_created_attribute(created_attrs, name, value):
                continue
            if audit_position_attribute(position_attrs, name, value):
                continue
            audit_regular_attribute(node, name, value)
        set_attributes(node, created_attrs, position_attrs)
        address = {}
        for tag in element.iter("tag"):
            if contains_problematic_characters(tag.attrib['k']):
                continue
            if audit_address(address, tag.attrib['k'], tag.attrib['v']):
                continue
            audit_regular(node, tag.attrib['k'], tag.attrib['v'])
        set_address(node, address)
        refs = []
        for nd in element.iter("nd"):
            audit_node_references(refs, nd.attrib['ref'])
        set_refs(node, refs)
        return node
    else:
        return None


def process_map(file_in, pretty = False):
    # You do not need to change this file
    file_out = "{0}.json".format(file_in)
    data = []
    with codecs.open(file_out, "w") as fo:
        for _, element in ET.iterparse(file_in):  # @UndefinedVariable
            el = shape_element(element)
            if el:
                data.append(el)
                if pretty:
                    fo.write(json.dumps(el, indent=2)+"\n")
                else:
                    fo.write(json.dumps(el) + "\n")
    return data