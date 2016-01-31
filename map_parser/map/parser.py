'''
Created on 28/1/2016

@author: jmonterrubio
'''

import element
import codecs
import json

import xml.etree.cElementTree as ET


#lower = re.compile(r'^([a-z]|_)*$')
#lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')


def process_map(file_in, pretty = False):
    # You do not need to change this file
    file_out = "{0}.json".format(file_in)
    data = []
    with codecs.open(file_out, "w") as fo:
        for _, elem in ET.iterparse(file_in):  # @UndefinedVariable
            el = element.shape(elem)
            if el:
                data.append(el)
                if pretty:
                    fo.write(json.dumps(el, indent=2)+"\n")
                else:
                    fo.write(json.dumps(el) + "\n")
    return data