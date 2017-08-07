days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJuly\nAug"
#%r would return this exactly as is, including the \n

#these return basically the same thing
print "Here are the days: ", days
print "Here are the days: %s" % days

print "Here are the months: ", months
print """
There's something going on here.
With the three double-quotes,
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""