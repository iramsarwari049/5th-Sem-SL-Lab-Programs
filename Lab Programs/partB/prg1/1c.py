
#Introduction to Python : Classes & Objects, Functions
#b)   Write a recursive python function that has a parameter representing a list of integers
#and returns the maximum stored in the list.
#Hint: The maximum is either the first value in the list or the maximum of the rest of
#the list whichever is larger. If the list only has 1 integer, then its maximum is this
#single value, naturally. Demonstrate with some examples.

# Note : Handle all other corner cases which are not handled here

def find_max(ls):
	if type(ls) is int:
		return ls
	if len(ls) == 1:
		return ls[0]
	else:
		return find_max(ls[1:]) if find_max(ls[1:]) > ls[0] else ls[0]

def main():
	try:
		lis = eval(input("Enter a list of numbers: "))
		print ("The largest number is: ", find_max(lis))
	except SyntaxError:
		print ("Please enter comma separated numbers")
	except NameError:
		print ("Enter only numbers")

main()