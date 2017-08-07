#Calculate the cost per ounce of various foods
print "What is the cost per ounce of these foods?"
print "Peanut butter is $4 for 32oz, or ${} per ounce.".format(4.00/32)
peanut_butter = 4.00/32
print "Jelly is $6 for 12oz, or ${} per ounce.".format(6.00/12)
jelly = 6.00/12
print "Bread is $2.50 for a 16 oz loaf, or ${} per ounce.".format(2.50/16)
bread = 2.50/16
print "If it takes one ounce each of jelly and peanut butter, plus 4 ounces of bread to make a sandwich, how much will that cost?"
print "${}".format(jelly + peanut_butter + bread * 4)