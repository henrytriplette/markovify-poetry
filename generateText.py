"""
This script will try load JSON models and generate text,
then send the generated text to Ollama for correction.

Usage:
    python generateTextAi.py -m "some-model.json" -l 10

Author: Henry Triplette
Date: February 27, 2025
"""

#!/usr/bin/python
import configparser
import argparse
import json
import ollama
import re

from rich import print
from libs import posifiedText

config = configparser.ConfigParser()
config.read('config.ini')

def main(args):
    reconstituted_model = posifiedText.loadPOSifiedText(args)
    sentences = []
    
    # Generate a sentences array
    for i in range(int(args.length)):
        sentence = reconstituted_model.make_sentence(tries=100)
        if (sentence is not None):
            sentences.append(sentence)

    # Join sentences into a sonnet
    sonnet = "\n".join(sentences)

    print("+---------------------------------+")
    print(sonnet)
    print("+---------------------------------+")

    ai_enable = config.getboolean('AI', 'ai_enable')
    if not ai_enable:
        print("AI is disabled in the config file. Exiting.")
        return

    # Set model and mode
    ai_model = config.get('AI', 'ai_model')
    ai_mode = config.get('AI', 'ai_mode')
    
    if ai_mode == 'song':
        content = 'You are a creative AI lyricist. Your task is to take a poem and rewrite it as lyrics for a song. Preserve the core emotion, themes, and imagery of the original poem, but adapt the structure to fit a typical song format (e.g., verses, chorus, possibly a bridge). Feel free to modernize language or adjust phrasing for rhythm and melody, while keeping the soul of the poem intact. If the poem has a specific rhyme scheme, try to maintain it, but prioritize the flow and musicality of the lyrics. Provide only the rewritten lyrics without additional comments or explanations.'
    elif ai_mode == 'poem':
        content = 'Correct the form of the given poem by analyzing and adjusting its structure, rhyme scheme, meter, line breaks, and punctuation. Ensure adjustments are made while preserving the original meaning and creativity. Provide only the corrected poem without additional comments. If the poem intentionally deviates from traditional forms, correct the form. Adjust line spacing and suggest appropriate rhyme endings as needed.'
    else:
        print(f"Unknown ai_mode '{ai_mode}' in config.ini. Exiting.")
        return
    
    try:
        # Setting up the model, enabling streaming responses, and defining the input messages
        ollama_response = ollama.chat(model=ai_model, messages=[
        {
            'role': 'system',
            'content': content,
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
            ollama.pull(ai_model)


if __name__ == "__main__": 
    text_length = config.get('DEFAULT', 'text_length')
    
    parser = argparse.ArgumentParser(description='Load JSON models and generate text')
    parser.add_argument('-m', '--model', help='Model File Path', required=True)
    parser.add_argument('-l', '--spacy_language', help='Spacy Language Model', default='en_core_web_lg', choices=['en_core_web_lg', 'it_core_news_lg'])
    parser.add_argument('-n', '--length', help='Generated text length', default=text_length, type=int)
    
    args = parser.parse_args()

    main(args)