#!/usr/bin/env python3
import os
import requests


proj_folder = os.getcwd() + '/supplier-data/descriptions/'
description = {}
url = 'http://localhost/fruits/'
description_keys = ['name', 'weight', 'description']


for path in os.listdir(proj_folder):
    with open(proj_folder + path, 'r') as file:
        image_name = path.replace('.txt', '.jpeg')
        for (part, key) in zip(file.read().splitlines(), description_keys):
            if key == 'weight':
                part = int(part.replace(' lbs', ''))
            description[key] = part
        description['image_name'] = image_name
        print(description)
    r = requests.post(url, json=description)


