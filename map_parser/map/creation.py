'''
Created on 30/01/2016

@author: jmonterrubio
'''
from utils import string

CREATED = ['version', 'changeset', 'timestamp', 'uid']
USER = 'user'

def fill_user_attr(created, key, value):
    if key == USER:
        created[key] = string.normalize(value)
        return True
    return False

def fill(created, key, value):
    if key in CREATED:
        created[key] = value
        return True
    return fill_user_attr(created, key, value)