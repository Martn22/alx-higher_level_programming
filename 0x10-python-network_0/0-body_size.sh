#!/bin/bash
# Script that gets URL and displays body of response in bytes
curl -s "$1" | wc -c
