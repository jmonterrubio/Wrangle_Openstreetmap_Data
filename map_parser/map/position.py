'''
Created on 30/01/2016

@author: jmonterrubio

Position element functions
'''

POSITION = ['lat', 'lon']


#
# Set formatted 'key' and 'value' into the 'position' map
# if it is and position element
#
def fill(position, key, value):
    if key in POSITION:
        position.insert(POSITION.index(key),float(value))
        return True
    return False