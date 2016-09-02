#!/bin/bash 
token="8870999dc7faf555e92c7b9743979580"
source="http://challenge.code2040.org/api/haystack"
dest="http://challenge.code2040.org/api/haystack/validate"
pycode=$"import json;text=\"\".join([x for x in sys.stdin]);print(json.loads(text)['haystack'].index(json.loads(text)['needle']))"

index="$(curl --data "{'token' : '$token'}\" --header \"Content-Type:application/json\" \"$source\")" |  "$(python3 -c \"$pycode\")"
curl -s --data "{\"token\" : \"$token\", \"needle\" : \"$index\" }" --header "Content-Type:application/json" "$dest"
