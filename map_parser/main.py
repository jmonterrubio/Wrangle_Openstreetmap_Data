'''
Created on 27/1/2016

@author: jmonterrubio
'''

import pprint
from map import parser

def clean_map():
    # NOTE: if you are running this code on your computer, with a larger dataset, 
    # call the process_map procedure with pretty=False. The pretty=True option adds 
    # additional spaces to the output, making it significantly larger.
    data = parser.process_map('../resources/sample_near_santander.osm')
    #pprint.pprint(data)
    

if __name__ == "__main__":
    clean_map()
