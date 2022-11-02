def reversed(word):
	reversed = ""
	for index in range(len(word)-1, -1, -1):
		reversed = reversed + word[index]
	return reversed
word = input("Please give word: ")
print(reversed(word))