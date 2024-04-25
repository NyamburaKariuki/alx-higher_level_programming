#!/bin/bash
# Fetch allowed HTTP methods using curl
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -f2- -d" " 
