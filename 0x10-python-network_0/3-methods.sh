#!/bin/bash
#display all methods http that server accept
curl -Is "$1" | grep "Allow: " | cut -d ' ' -f 2-
