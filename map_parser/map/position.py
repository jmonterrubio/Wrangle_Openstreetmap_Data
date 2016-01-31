'''
Created on 30/01/2016

@author: jmonterrubio
'''

POSITION = ['lat', 'lon']

def fill(position, key, value):
    if key in POSITION:
        position.insert(POSITION.index(key),float(value))
        return True
    return False