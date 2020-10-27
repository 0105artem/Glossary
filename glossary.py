#! python3
# glossary.py - gets an english word from the user and returns its definition.
# If user made a typo the program will find the most similar word to the input.

import json
from difflib import get_close_matches


data = json.load(open('data.json'))


def dictionary(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()] # In case user enters words like USA or NATO
    elif get_close_matches(word, data.keys()):
        for match in get_close_matches(word, data.keys()):
            ans = input('Do you mean ' + match + '? Enter Y if yes, or N of no: ')
            if ans.lower() == 'y':
                return data[match] 
    else:
        return 'Sorry, this word doesn\'t exist. Please double check it.'


def print_definitions(output):
    if type(output) == list:
        for definition in output:
            print(definition)
    else:
        print(output)


word = input('Input a word: ')
output = dictionary(word)
print_definitions(output)
