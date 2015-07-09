#!/usr/bin/env python

import datetime
import sys
import json
import os
import shlex

target_file = None # what we're going to edit
properties = None # the passed JSON with properties

def module_exit(success=True, msg="No message provided"):
    if success:
        result_json = {
            "changed" : True,
            "msg": msg,
        }
    else:
        result_json = {
            "failed": True,
            "msg": msg,
        }
    print json.dumps(result_json)
    sys.exit(0 if success else 1)

# read the argument string from the arguments file
args_file = sys.argv[1]
args_data = file(args_file).read()

arguments = shlex.split(args_data)
for arg in arguments:
    if "=" not in arg:
        continue

    (key, value) = arg.split("=")
    if key == "file":
        target_file = value
    elif key == "props":
        properties = json.loads(value)

if not (properties and target_file):
    module_exit(False, "Both file and props must be provided")

with open(target_file, 'r') as props_file:
    source_lines = props_file.read_lines()

source_lines = [x for x in source_lines if "=" in x] # filter out non-propertie
source_properties = {}
for line in source_lines:
    source_properties[line.split('=')[0]] = "=".join(line.split('=')[1:])
    
source_properties.update(properties) # perform override

with open(target_file, 'w') as props_file:
    for key, value in source_properties.iteritems():
        props_file.write("{0}={1}\n".format(key, value))

module_exit(True, "File {0} has been updated".format(target_file))
