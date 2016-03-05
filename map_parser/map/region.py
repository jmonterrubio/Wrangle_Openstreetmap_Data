# coding=utf-8
'''
Created on 01/02/2016

@author: jmonterrubio
'''

REGION_KEY = 'is_in'
REGION_VALUE_SEPARATOR = ';'

def set_correct_separator(fixed_value):
    return fixed_value.replace(',',REGION_VALUE_SEPARATOR)

def set_spanish_language(value):
    fixed_value = value.replace('Spain','España')
    fixed_value = fixed_value.replace('Europe','Europa')
    return fixed_value

def add_unexist_entities(value):
    fixed_value = value
    if not 'Europa' in value:
        fixed_value = fixed_value + ';Europa'
    if not 'España' in fixed_value:
        fixed_value = fixed_value + ';España'
    return fixed_value

def remove_duplicates(value):
    value_list = value.split(REGION_VALUE_SEPARATOR)
    final_list = []
    for name in value_list:
        if name in final_list: continue
        final_list.append(name)
    return to_string(final_list)

def to_string(value_list):
    value = ''
    for name in value_list:
        if value == '':
            value = name
        else:
            value = value + REGION_VALUE_SEPARATOR + name
    return value

def order_entity(value_list, entity_name, entity_position):
    unknown_name = value_list[entity_position]
    if not unknown_name == entity_name:
        entity_position_to_fix = value_list.index(entity_name)
        value_list.insert(entity_position, value_list.pop(entity_position_to_fix))

def order_entities(value):
    value_list = value.split(REGION_VALUE_SEPARATOR)
    order_entity(value_list, 'Europa', len(value_list)-1)
    order_entity(value_list, 'España', len(value_list)-2)        
    return to_string(value_list)
            
def fill(reg, key, value):
    if key == REGION_KEY:
        fixed_value = set_correct_separator(value)
        fixed_value = set_spanish_language(fixed_value)
        fixed_value = add_unexist_entities(fixed_value)
        fixed_value = remove_duplicates(fixed_value)
        fixed_value = order_entities(fixed_value)
        reg[key] = fixed_value
        return True
    return False