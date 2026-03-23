#!/bin/bash

URL="https://gist.githubusercontent.com/kevin336/acbb2271e66c10a5b73aacf82ca82784/raw/e38afe62e088394d61ed30884dd50a6826eee0a8/employees.csv"
OUTPUT="data.csv"

echo "Downloading employee data..."
curl -o "$OUTPUT" "$URL"

if [ $? -ne 0 ]; then
    echo "Download failed!" >> error.log
    exit 1
fi

echo "Download completed!"
