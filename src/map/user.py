'''
Created on 29/1/2016

@author: jmonterrubio
'''

import unicodedata

def normalize(s):
    return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

def audit_user(user, key, value):
    if key == 'uid':
        user[key] = value
    if key == 'user':
        user['name'] = normalize(value) 
    return user

