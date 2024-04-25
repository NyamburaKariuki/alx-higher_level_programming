#!/bin/bash
# Fetch allowed HTTP methods using curl
curl -s -I -X OPTIONS "$1" | grep "Allow:" | tr -d '\r' | awk '{print "Allowed HTTP methods:", $2}'
