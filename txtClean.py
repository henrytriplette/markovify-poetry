"""
This script will try to fix TXT for repetitive lines and remove duplicates.
It will then save the cleaned content to a new file.

Usage:
    python txtClean.py -f "some-txt-file.txt"

Author: Henry Triplette
Date: February 27, 2025
"""

#!/usr/bin/python
import argparse

from libs import textUtils

def main(args):    
    textUtils.remove_duplicate_lines(args.file, args.file + ".deduped.txt")
    
if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Convert TXT files to Markovify.json models')
    parser.add_argument('-f', '--file', help='TXT File Path', required=True)
    
    args = parser.parse_args()

    main(args)