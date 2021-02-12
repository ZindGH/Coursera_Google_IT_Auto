#!/usr/bin/env python3
import os
import requests
proj_folder = os.getcwd() + '/supplier-data/images/'
url = 'http://localhost/upload/'

for path in os.listdir(proj_folder):
    if '.jpeg' in path:
        with open(proj_folder + path, 'rb') as opened:
            r = requests.post(url, files={'file': opened})