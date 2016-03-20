# <! Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)

string = "Race car"
stringstrip = string.replace(" ", "").lower()
print stringstrip
backwards = stringstrip[::-1]
print backwards

if stringstrip == backwards:
	print "You found a palindrome! {} is the same forwards and backwards!".format(string.capitalize())

