#!/usr/bin/python
import markovify
import argparse
import json

def main(args):
    reconstituted_model = markovify.Text.from_json(json.load(open(args.model)))
    for i in range(args.length):
        print(reconstituted_model.make_sentence(tries=100))

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Load JSON models and generate text')
    parser.add_argument('-m', '--model', help='Model File Path', required=True)
    parser.add_argument('-l', '--length', help='Generated text length', default=10)
    
    args = parser.parse_args()

    main(args)