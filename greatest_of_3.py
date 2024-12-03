"""
Program made by MoonBeamGGS to find the greatest number in a set of 3
"""
"""
Revised for use with Python3 and above, if a later version is to release.
"""
def greatest_of_3(a, b, c):
	"""
	This function will give you the greatest number out of a set of 3
	"""
	if a >= b and a >= c:
		print ("Number A is the greatest of the 3")
		return(a)
	if b >= a and b >= c:
		print ("Number B is the greatest of the 3")
		return(b)
	if c >= a and c >= b:
		print ("Number C is the greatest of the 3")
		return(c)


a = input("Pick a number to set as number A: ")
b = input("Pick a number to set as number B: ")
c = input("Pick a number to set as number C: ")
a =float(a)
b = float(b)
c = float(c)
print(greatest_of_3(a, b, c))

"""
a: First number
b: Second number
c: Third number
@return 
"""
def greatest_of_3_alternate(a, b, c):
	if a > b:
		if a > c:
			return a
	else:
		if b > c:
			return b

	return c

def hello_name(name):
	print("hello {name}".format(name=name))

assert greatest_of_3_alternate(12, 24, 36) == 36
print(greatest_of_3_alternate(a,b,c))

#hello_name(input("What's your name?"))