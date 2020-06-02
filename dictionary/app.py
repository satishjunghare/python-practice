import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(keyword):
	keyword = keyword.lower()
	if keyword in data:
		return data[keyword]
	elif len(get_close_matches(keyword, data.keys())) > 0:
		keyword_suggession = get_close_matches(keyword, data.keys())[0]
		is_same_word = input("Did you mean %s instead? (Y/N): " % keyword_suggession)
		if is_same_word.lower() == "y":
			return data[keyword_suggession]
		else:
			return "The word doesn't exists. Please double check it."
	else:
		return "The word doesn't exists. Please double check it."

def ask_input():
	word = input("Enter word: ")
	output = translate(word)

	if type(output) == list:
		for item in output:
			print(item)
	else:
		print(output)


# Ask for user input
ask_input()
