#!/usr/bin/python

import sys
import json
import pprint
args = str(sys.argv[1])

file_object = open(args, 'r')
jsond = json.loads(file_object.read())
file_object.close()

first = jsond['resultStatus']
for element in jsond['orderLists']:
    print element['item']


