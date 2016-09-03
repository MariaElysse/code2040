#!/usr/bin/env python3
import requests

source_url = "http://challenge.code2040.org/api/haystack"
dest_url = "http://challenge.code2040.org/api/haystack/validate"
token="8870999dc7faf555e92c7b9743979580"

source = requests.post(source_url, data={"token" : token})
index = source.json()['haystack'].index(source.json()['needle'])
dest = requests.post(dest_url, data={"token" : token, "needle" : index}) 
print("{0} : {1}".format(dest.status_code, dest.text))
