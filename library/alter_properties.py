#!/usr/bin/env python

from ansible.module_utils.basic import *

# using ansible module class to manage all the parameters stuff
module = AnsibleModule(
    argument_spec = dict(
        file      = dict(required=True, type='str'),
        props     = dict(required=True, type='dict'),
    )
)

with open(module.params['file'], 'r') as props_file:
    source_lines = props_file.readlines()

source_lines = [x for x in source_lines if "=" in x] # filter out non-propertie
source_properties = {}
for line in source_lines:
    source_properties[line.split('=')[0]] = "=".join(line.split('=')[1:])
    
source_properties.update(module.params['props']) # perform override

with open(module.params['file'], 'w') as props_file:
    for key, value in source_properties.iteritems():
        props_file.write("{0}={1}\n".format(key, value))

module.exit_json(changed=True, msg="File {0} has been updated".format(module.params['file']))
