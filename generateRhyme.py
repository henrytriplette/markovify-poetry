#!/usr/bin/python
import configparser
import argparse
import json
import ollama
import re

config = configparser.ConfigParser()
config.read('config.ini')

def main(args):
    while True:
        user_input = input("Enter word or phrase: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        print("Generating rhymes...")
        ai_model = config.get('RHYME', 'ai_model')

        try:
            content = """
            You are a creative AI lyricist. Your task is to take a word and suggest possible rhymes. 
            Prioritize the flow and musicality of the lyrics. Provide only the rhymes without additional comments or explanations.
            """
            # Setting up the model, enabling streaming responses, and defining the input messages
            ollama_response = ollama.chat(model=ai_model, messages=[
            {
                'role': 'system',
                'content': content,
            },
            {
                'role': 'user',
                'content': user_input,
            },
            ])
            
            # Remove the </think> tags from the response
            response = re.sub(r'<think>.*?</think>', '', ollama_response['message']['content'], flags=re.DOTALL)
            
            # Printing out of the refined response
            print("+---------------------------------+")
            print(response)
            print("+---------------------------------+")
        
        
        except ollama.ResponseError as e:
            print('Error:', e.error)
            if e.status_code == 404:
                ollama.pull(ai_model)

if __name__ == "__main__":    
    parser = argparse.ArgumentParser(description='Load JSON models and generate text')
    parser.add_argument('-m', '--model', help='Model File Path')

    args = parser.parse_args()

    main(args)