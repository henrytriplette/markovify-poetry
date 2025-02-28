"""
This script will try load JSON models and generate text,
then send the generated text to Ollama for correction.

Usage:
    python generateTextAi.py -m "some-model.json" -l 10

Author: Henry Triplette
Date: February 27, 2025
"""

#!/usr/bin/python
import argparse
import json
import ollama
import re

from rich import print
from libs import posifiedText

def main(args):
    reconstituted_model = posifiedText.loadPOSifiedText(args)
    sentences = []
    
    # Generate a sentences array
    for i in range(args.length):
        sentence = reconstituted_model.make_sentence(tries=100)
        if (sentence is not None):
            sentences.append(sentence)

    # Join sentences into a sonnet
    sonnet = "\n".join(sentences)

    print("+---------------------------------+")
    print(sonnet)
    print("+---------------------------------+")

    try:
        # Setting up the model, enabling streaming responses, and defining the input messages
        ollama_response = ollama.chat(model='deepseek-r1:8b', messages=[
        {
            'role': 'system',
            'content': 'Correct the form of the given poem by analyzing and adjusting its structure, rhyme scheme, meter, line breaks, and punctuation. Ensure adjustments are made while preserving the original meaning and creativity. Provide only the corrected poem without additional comments. If the poem intentionally deviates from traditional forms, correct the form. Adjust line spacing and suggest appropriate rhyme endings as needed.',
        },
        {
            'role': 'user',
            'content': sonnet,
        },
        ])
        
        # Remove the </think> tags from the response
        result = re.sub(r'<think>.*?</think>', '', ollama_response['message']['content'], flags=re.DOTALL)

        # Printing out of the generated response
        print("+---------------------------------+")
        print(result)
        print("+---------------------------------+")

    except ollama.ResponseError as e:
        print('Error:', e.error)
        if e.status_code == 404:
            ollama.pull(model)


if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Load JSON models and generate text')
    parser.add_argument('-m', '--model', help='Model File Path', required=True)
    parser.add_argument('-l', '--spacy_language', help='Spacy Language Model', default='en_core_web_lg', choices=['en_core_web_lg', 'it_core_news_lg'])
    parser.add_argument('-n', '--length', help='Generated text length', default=10)
    
    args = parser.parse_args()

    main(args)