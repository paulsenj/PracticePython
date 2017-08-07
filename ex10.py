print "I am 5'3\" tall." #escape double quote in this string
print 'I am 5\'3" tall' #escape the single quote

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
#''' works the same was as """

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#while True:
#	for i in ["/","-","|","\\","|"]:
#		print "%s\r" % i,
#this runs forever!