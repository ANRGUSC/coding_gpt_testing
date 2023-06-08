#!/bin/bash

# Check if a file name is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: ./extract_code.sh <filename>"
    exit 1
fi

# Extract the content using sed
sed -n 's/.*\({\"lang\":\"Python3\"[^}]*\}\).*/\1/p' "$1"

