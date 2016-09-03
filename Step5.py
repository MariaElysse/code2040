#!/usr/bin/env python3
import requests
import datetime
token="8870999dc7faf555e92c7b9743979580"
source_url="http://challenge.code2040.org/api/dating"
dest_url="http://challenge.code2040.org/api/dating/validate"

r=requests.post(source_url, data={"token" : token})
datestamp = datetime.datetime.strptime(r.json()['datestamp'], "%Y-%m-%dT%H:%M:%SZ")
delta = datetime.timedelta(seconds=r.json()['interval'])
result=datestamp+delta
s=requests.post(dest_url, json={"token" : token, "datestamp" : result.isoformat()+"Z"})
print("{} : {} \n{}Z".format(s.status_code, s.text, result.isoformat()))
