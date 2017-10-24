import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def word_lookup(word):
    if word in data:
        return data[word]
    elif word.lower() in data:
        return data[word.lower()]
    elif len(get_close_matches(word, data.keys())) > 0:
        answer = input("Did you mean %s instead? " % get_close_matches(word, data.keys())[0])
        if answer.lower() == "yes" or answer.lower() == "y":
            return data[get_close_matches(word, data.keys())[0]]
        else:
            return "Not found."
    else:
        return "Not found."


lookup = input("Enter a word: ")

output = word_lookup(lookup)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
