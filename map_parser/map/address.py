'''
Created on 01/02/2016

@author: jmonterrubio
'''
from utils import string

ADDRESS = 'addr'
ADDRESS_SEPARATOR = ':'

def fill(addr, key, value):
    if key.startswith(ADDRESS + ADDRESS_SEPARATOR):
        if key.count(ADDRESS_SEPARATOR) == 1:
            addr[key[5:]] = string.normalize(value)
        return True
    return False