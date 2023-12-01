#!/bin/bash
# get url send request and display size of the body
curl -s "$1" | wc -c
