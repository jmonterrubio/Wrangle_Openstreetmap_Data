# coding=utf-8
'''
Created on 01/02/2016

@author: jmonterrubio
'''

REGION_KEY = 'is_in'
REGION_VALUE_SEPARATOR = ':'

def fill(reg, key, value):
    if key == REGION_KEY:
        fixed_value = value.replace(',',';')
        fixed_value = fixed_value.replace('Spain','España')
        fixed_value = fixed_value.replace('Europe','Europa')
        if not 'Europa' in fixed_value:
            fixed_value = fixed_value + ';Europa'
        if not 'España' in fixed_value:
            fixed_value = fixed_value + ';España'
        fixed_list = fixed_value.split(';')
        final_list = []
        for name in fixed_list:
            if name in final_list: continue
            final_list.append(name)
        
        t_name = final_list[len(final_list)-1]
        if not t_name == 'Europa':
            e_pos = final_list.index('Europa')
            final_list[e_pos] = final_list[len(final_list)-1]
            final_list[len(final_list)-1] = 'Europa'
            
        t_name = final_list[len(final_list)-2]
        if not t_name == 'España':
            e_pos = final_list.index('España')
            final_list[e_pos] = final_list[len(final_list)-2]
            final_list[len(final_list)-2] = 'España'
            
        final_value = ''
        for name in final_list:
            if final_value == '':
                final_value = name
            else:
                final_value = final_value + ';' + name  
        reg[key] = final_value
        return True
    return False