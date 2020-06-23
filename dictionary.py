import json
from difflib import get_close_matches

with open('data.json') as src:
    data = json.load(src)

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        recommended = get_close_matches(word, data.keys())[0]
        yn = input("Did you mean %s instead? Type Y to confirm. " % recommended).lower()[0]
        if yn == 'y':
            return data[recommended]
        else:
            return "Word doesn't appear in dictionary"
    else:
        return "Word doesn't appear in dictionary"

word = input('Enter word: ')

output = translate(word)
if type(output) == list:
    for i in output:
        print('- ', i)
else:
    print(output)
