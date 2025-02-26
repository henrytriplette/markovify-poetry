#!/usr/bin/python
import markovify
import json
import argparse

def main(args):
    corpus = open(args.file).read()

    text_model = markovify.NewlineText(corpus, state_size=2)
    model_json = text_model.to_json()
    
    with open(args.file + ".json", "w") as json_data:
        json.dump(model_json, json_data, indent=4)
    print("- Generated cache for {};".format(args.file))

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Convert TXT files to Markovify.json models')
    parser.add_argument('-f', '--file', help='TXT File Path', required=True)
    
    args = parser.parse_args()

    main(args)
    