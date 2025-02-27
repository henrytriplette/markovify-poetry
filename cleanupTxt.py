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