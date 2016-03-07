'''
Created on 30/01/2016

@author: jmonterrubio

Creation element functions
'''
#from utils import string

CREATED = ['version', 'changeset', 'timestamp', 'uid']
USER = 'user'

#
# Set formatted 'key' and 'value' into the 'created' map
# if it is and user element
#
def fill_user_attr(created, key, value):
    if key == USER:
        created[key] = value#string.normalize(value)
        return True
    return False

#
# Set formatted 'key' and 'value' into the 'created' map
# if it is and created element
#
def fill(created, key, value):
    if key in CREATED:
        created[key] = value
        return True
    return fill_user_attr(created, key, value)