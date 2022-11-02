"""
This simple program, made by Mihir Pillay will allow you to reverse any string that consists of five characters.
"""
def reverse(word):
	"""
	This function gives the random number
	"""
	reversed = ""
	reversed = reversed + word[4]
	reversed = reversed + word[3]
	reversed = reversed + word[2]
	reversed = reversed + word[1]
	reversed = reversed + word[0]
	return reversed

def reversed_superior(word):
	reversed = ""
	for index in range(4, -1, -1):
		reversed = reversed + word[index]
	return reversed


word = input("Pls give 5 character string: ")
#print(reverse(word))
print(reversed_superior(word))
