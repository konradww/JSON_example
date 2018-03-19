# Read and write JSON files with Python 3
# -*- coding: utf-8 -*-
import json
import io

# Define data
data = {'string': 'example string',
        'list': [75, 42, 3.141, 777, 'text'],
        'dict': {'key1': 'value1',
                'key2': 'value2',
                'key3': 3}}


# Write JSON file
with io.open('data.json', 'w') as outfile:
    outfile.write(json.dumps(data,
                             sort_keys=True,
                             ensure_ascii=False,
                             indent=4
                             )
                  )

# Read JSON file
with open('data.json') as data_file:
    data_loaded = json.load(data_file)


print(data == data_loaded)
print (data_loaded)
list = data_loaded['list']
print (list)
