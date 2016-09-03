#!/usr/bin/env python3
import requests
import json 
token="8870999dc7faf555e92c7b9743979580"
source_url="http://challenge.code2040.org/api/prefix"
dest_url="http://challenge.code2040.org/api/prefix/validate"

r=requests.post(source_url, data={"token" : token })
result = [x for x in r.json()['array'] if not x.startswith(r.json()['prefix'])]
s=requests.post(dest_url, json={"token" : token, "array" : result})
print("{} : {}".format(s.status_code, s.text))
