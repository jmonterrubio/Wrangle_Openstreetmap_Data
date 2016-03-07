'''
Created on 01/02/2016

@author: jmonterrubio

Address element functions
'''
#from utils import string

ADDRESS = 'addr'
ADDRESS_SEPARATOR = ':'

#
# Set formatted 'key' and 'value' into the 'addr' map
# if it is and address element
#
def fill(addr, key, value):
    if key.startswith(ADDRESS + ADDRESS_SEPARATOR):
        if key.count(ADDRESS_SEPARATOR) == 1:
            addr[key[5:]] = value#string.normalize(value)
        return True
    return False