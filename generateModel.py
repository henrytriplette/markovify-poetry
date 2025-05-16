"""
This script will try to convert TXT files to Markovify.json models

Usage:
    python generateModel.py -f "some-txt-file.txt"

Author: Henry Triplette
Date: February 27, 2025
"""

#!/usr/bin/python
import json
import argparse
import re

from libs import posifiedText
from libs import textUtils

def main(args):    
    textUtils.remove_duplicate_lines(args.file, args.file + ".deduped.txt")
    # Read the file
    with open(args.file + ".deduped.txt", 'r', encoding='utf-8') as file:
        corpus = file.read()

    # Remove special characters (keeping letters, numbers, spaces, and newlines)
    corpus = re.sub(r'[^a-zA-Z0-9\s\n]', '', corpus)

    text_model = posifiedText.posifiedTextNewlineModel(corpus, args)
    model_json = text_model.to_json()
    
    with open(args.file + ".json", "w") as json_data:
        json.dump(model_json, json_data, indent=4)
    print("- Generated cache for {};".format(args.file))

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Convert TXT files to Markovify.json models')
    parser.add_argument('-f', '--file', help='TXT File Path', required=True)
    parser.add_argument('-l', '--spacy_language', help='Spacy Language Model', default='en_core_web_lg', choices=['en_core_web_lg', 'it_core_news_lg'])
    parser.add_argument('-s', '--state_size', help='State size', type=int, default=2)
    
    args = parser.parse_args()

    main(args)