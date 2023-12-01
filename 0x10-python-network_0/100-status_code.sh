#!/bin/bash
#sends a request to a URL and displays only the status
curl -sI -w '%{response_code}' "$1" -o /dev/null
