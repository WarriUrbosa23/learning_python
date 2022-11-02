def first_letter_of_string(word):
	"""
	This function will give you the first letter of any string.  
	"""
	return word[0]

def last_letter_of_string(word):
	"""
	This function will give you the last letter of any string.  
	"""
	return word[len(word)-1]

a = "hello"
assert first_letter_of_string("hello") == "h"
assert last_letter_of_string("hello") == "o"
print(first_letter_of_string(a))
print(last_letter_of_string(a))