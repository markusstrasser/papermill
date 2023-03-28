#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Please provide a directory path."
    exit 1
fi

dir="$1"

before=$(find "$dir" -type f | wc -l)

processed=0
count=0
for file in $(find "$dir" -type f | sort); do
    basename=$(basename "$file")
    version=$(echo "$basename" | grep -oE "v[0-9]+\.pdf" | grep -oE "[0-9]+v[0-9]+" | sed 's/v//')
    latest=$(echo "$basename" | grep -oE "v[0-9]+\.pdf" | grep -oE "[0-9]+v[0-9]+" | sort -r | head -n1 | sed 's/v//')


    if [ "$version" != "$latest" ]; then
        rm "$file"
    fi

    processed=$((processed+1))
    if [ "$processed" -eq 100 ]; then
        count=$((count+100))
        processed=0
        echo -ne "Progress: $count / $before\r"
    fi
done

after=$(find "$dir" -type f | wc -l)

echo "Before: $before"
echo "After: $after"
