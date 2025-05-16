"""
This script will try to fetch some txt files from the Internet Archive given a Creator Key.

Usage:
    python fetchText.py -f "John Doe"

Author: Henry Triplette
Date: February 27, 2025
"""

import argparse
import internetarchive as ia

# https://archive.org/services/docs/api/internetarchive/quickstart.html
def main(args):
    search_results = ia.search_items('creator:' + args.fetch + ' AND mediatype:texts AND language:English')
    
    for item in search_results:
        item_id = item['identifier']
        print(f"Downloading text file for: {item_id}")
        ia.download(item_id, verbose=True, glob_pattern="*.txt", destdir="input")
        
    # ia.download(args.fetch, verbose=True, glob_pattern="*.txt", destdir="input")

if __name__ == '__main__':

    # Initialize
    parser = argparse.ArgumentParser(description='Fetch some txt files from the Internet Archive.')
    parser.add_argument('-f', '--fetch', help='File to download', required=True)

    args = parser.parse_args()

    main(args)
