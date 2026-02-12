#!/bin/bash

# Check if yq is installed
if ! command -v yq &> /dev/null
then
    echo "yq could not be found. Please install it to continue."
    echo "See: https://github.com/mikefarah/yq#install"
    exit
fi

# The directory where the manuscript will be saved
MANUSCRIPT_DIR="manuscript"

# Create the manuscript directory if it doesn't exist
mkdir -p "$MANUSCRIPT_DIR"

# Read the book.yml file and generate the chapters
yq -r '.chapters[] | .title + "||" + .prompt + "||" + .filename' book.yml | while IFS="||" read -r title prompt filename
do
    echo "Generating chapter: $title"
    gemini -p "Write chapter titled '$title'. $prompt" > "$MANUSCRIPT_DIR/$filename"
done

echo "Book generation complete."
