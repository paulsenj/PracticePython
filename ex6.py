#This substitutes a number into the string
x = "There are %d types of people." % 10
#This changes the string "binary" into a variable
binary = "binary"
#This changes the string "don't into a variable"
do_not = "don't"
#This substitutes strings into the string (2)
y = "Those who know %s and those who %r." % (binary, do_not)

print x
print y

#%r returns exactly what was input, including the quotes in this string
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" 

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."
#"adding" the two strings together is concatenating
print w + e