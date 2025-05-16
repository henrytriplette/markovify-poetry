import re

#!/usr/bin/python
def clean_text_file(file_path):
    """Reads a text file, removes special characters, and saves the cleaned content."""
    
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove special characters (keeping letters, numbers, spaces, and newlines)
    cleaned_content = re.sub(r'[^a-zA-Z0-9\s\n]', '', content)
    
    # Save the cleaned content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(cleaned_content)
        
        
def remove_duplicate_lines(input_file, output_file):
    seen_lines = set()
    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            if line not in seen_lines:
                outfile.write(line)
                seen_lines.add(line)