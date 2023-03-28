#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Please provide a directory path."
    exit 1
fi

dir="$1"

before=$(ls -1 "$dir"/*.pdf | wc -l)

count=0
processed=0
for file in "$dir"/*.pdf; do
    processed=$((processed+1))
    if [ "$processed" -eq 5 ]; then
        count=$((count+5))
        processed=0
        echo -ne "Progress: $count / $before\r"
    fi

    if pdftotext "$file" - | grep -qi "cs\.ai"; then
        title=$(pdftk "$file" dump_data | grep "InfoTitle:" | cut -d " " -f 2-)
        echo "$title"
    fi
done

after=$(ls -1 "$dir"/*.pdf | wc -l)

echo "Before: $before"
echo "After: $after"
