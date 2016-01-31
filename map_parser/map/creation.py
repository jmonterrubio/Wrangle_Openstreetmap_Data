'''
Created on 30/01/2016

@author: jmonterrubio
'''
import unicodedata

CREATED = ['version', 'changeset', 'timestamp', 'uid']
USER = 'user'

def normalize_name(s):
    return ''.join((c for c in unicodedata.normalize('NFD', unicode(s)) if unicodedata.category(c) != 'Mn')).replace ("_", " ").lower()

def fill_user_attr(created, key, value):
    if key == USER:
        created[key] = normalize_name(value)
        return True
    return False

def fill(created, key, value):
    if key in CREATED:
        created[key] = value
        return True
    return fill_user_attr(created, key, value)