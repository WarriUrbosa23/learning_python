def middle_letter_of_odd_string(word):
	"""
	This function will give you the middle letter of any string with an odd number of characters. 
	"""
	return word[len(word)/2]


def middle_letter_of_even_string(word):
	"""
	This function will give you the middle letter of any string with an even number of characters
	"""
	return word[(len(word)/2)-1] + word[(len(word)/2)]

def middle_of_string(word):
	is_even = (len(word)/2) * 2 == len(word)

	if is_even:
		return middle_letter_of_even_string(word)
	else:
		return middle_letter_of_odd_string(word)


# a = "Mihir"
# e = "OneTwo"
# assert middle_letter_of_odd_string("Mihir") == "h"
# assert middle_letter_of_odd_string("A") == "A"
# print(middle_letter_of_odd_string(a))
# print(middle_letter_of_even_string(e))

print(middle_of_string("1211"))
print(middle_of_string("123"))
assert middle_of_string("Manoj") == "n"
assert middle_of_string("Poomol") == "om"