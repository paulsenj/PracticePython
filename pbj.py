bread = 21
peanut_butter = 14
jelly = 7

sandwiches = min (bread/2, peanut_butter, jelly)
pbsandwiches = min (bread/2, peanut_butter)


if bread >= 2 and peanut_butter >= 1 and jelly >= 1 and min (bread/2, peanut_butter, jelly) == jelly:
	print "Success! You can make this many PB&J sandwiches: {0} and this many PB-only sandwiches: {1}".format(sandwiches, pbsandwiches-sandwiches)
elif bread >= 2 and peanut_butter >= 1 and jelly >= 1:
	print "Success! You can make this many PB&J sandwiches: {0}".format(sandwiches)
elif bread >= 2 and peanut_butter >= 1 and jelly == 0:
	print "Meh! You have no jelly, but you could make this many PB-only sandwiches: {0}".format(pbsandwiches)
else:
	print "Fail! You need more ingredients to make a PB&J"

if bread % 2 == 1 and peanut_butter - sandwiches > 0 and jelly - sandwiches > 0:
	print "And an open-faced sammie too!"
if bread % 2 == 1 and peanut_butter - sandwiches > 0 and jelly - sandwiches == 0:
	print "And an open-faced PB-only sammie too!"

if bread/2 == 0:
	print "You're out of bread!"
if peanut_butter == 0:
	print "You're out of peanut butter!"
