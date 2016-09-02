#!/bin/bash
token="8870999dc7faf555e92c7b9743979580"
github="https://github.com/jerenept/code2040.git"

curl --data "{\"token\" : \"$token\", \"github\" : \"$github\" }" --header "Content-Type:application/json" "http://challenge.code2040.org/api/register"
