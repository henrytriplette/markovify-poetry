#!/usr/bin/python
import markovify
import re
import io
import sys, getopt
import spacy

import fnmatch
import json
import random
import os
import argparse

# Author
import author

current_file_path = os.path.abspath(__file__)
input_directory = os.path.split(current_file_path)[0] + "/input/"
scripts_directory = os.path.split(current_file_path)[0] + "/models/"
state_size = 2

def find(pattern, path):
        """
        Finds the *first* instance of a file name in a single directory.
        :param pattern: str, file name pattern to search for
        :param path:    str, path to search
        :return:        list of str or empty list, any matching file name ends up in the list
        """
        result = []
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        for file in files:
            if fnmatch.fnmatch(file, pattern):
                result.append(file)
                break
        return result

def main(args):

    spacy.prefer_gpu();

    # print("Spacy set to {} language;".format(args.spacy_language))
    print("--------------------")

    for file in os.listdir( input_directory ):
        if file.endswith(".txt"):
            filename_clean = file.replace(".txt", "")
            # Check and generate json cache file
            if find(filename_clean + "_" + str(args.state_size) + ".json", scripts_directory):
                print("Found:", filename_clean)
            else:
                print("Starting cache for {};".format(filename_clean))

                # Spacy
                # nlp = spacy.load(args.spacy_language)

                text = io.open(input_directory + filename_clean + '.txt', 'r', encoding='utf-8')
                model = author.POSifiedText(text, args.state_size)
                model_json = model.to_json()
                with open(scripts_directory + filename_clean + "_" + str(args.state_size) + ".json", "w") as json_data:
                    json.dump(model_json, json_data, indent=4)
                print("- Generated cache for {};".format(filename_clean))

if __name__ == "__main__":

    # Initialize
    parser = argparse.ArgumentParser(description='Convert TXT files to Markovify.json models')
    # parser.add_argument('-l', '--spacy_language', help='Spacy Language Model', required=True, default='en_core_web_lg', choices=['en_core_web_lg', 'it_core_news_lg'])
    parser.add_argument('-s', '--state_size', help='State size', required=True, type=int, default=2)

    args = parser.parse_args()

    main(args)
