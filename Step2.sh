#!/bin/bash 
token="8870999dc7faf555e92c7b9743979580"
source="http://challenge.code2040.org/api/reverse"
dest="http://challenge.code2040.org/api/reverse/validate"

str="$(curl -s --data "{ \"token\" : \"$token\" }" --header "Content-Type:application/json" $source)"
rev="$(echo $str | rev)"
echo "Received: \"$str\". Returning \"$rev\"."
curl --data "{ \"token\" : \"$token\" , \"string\" : \"$rev\" }" --header "Content-Type:application/json" $dest 
