'''
Created on 31/01/2016

@author: jmonterrubio
'''

ADDRESS = 'addr'
ADDRESS_SEPARATOR = ':'

def fill(addr, key, value):
    if key.startswith(ADDRESS + ADDRESS_SEPARATOR):
        if key.count(ADDRESS_SEPARATOR) == 1:
            addr[key[5:]] = value
        return True
    return False