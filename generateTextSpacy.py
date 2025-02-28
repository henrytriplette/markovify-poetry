"""
This script will try load JSON models and generate text using Spacy models

Usage:
    python generateText.py -m "some-model.json" -l 10

Author: Henry Triplette
Date: February 27, 2025
"""

#!/usr/bin/python
import markovify
import argparse
import json
import spacy

def main(args):
    nlp = spacy.load("en_core_web_sm")
    
    class POSifiedText(markovify.Text):
        """Uses spacy to parse the text into a model.

        For information on the inherited properties and functions,
        see the markovify documentation at
        [https://github.com/jsvine/markovify](https://github.com/jsvine/markovify)
        """

        def word_split(self, sentence):
            """Split the sentence into words and there respective role in the
            sentence."""
            return ["::".join((word.orth_, word.pos_)) for word in nlp(sentence)]

        def word_join(self, words):
            """Join words back into a sentence."""
            sentence = " ".join(word.split("::")[0] for word in words)
            return sentence
        
    reconstituted_model = POSifiedText.from_json(json.load(open(args.model)))
    for i in range(args.length):
        print(reconstituted_model.make_sentence(tries=100))

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Load JSON models and generate text')
    parser.add_argument('-m', '--model', help='Model File Path', required=True)
    parser.add_argument('-l', '--length', help='Generated text length', default=10)
    
    args = parser.parse_args()

    main(args)