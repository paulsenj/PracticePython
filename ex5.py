name = "Jamie Paulsen"
age = 29 #and feeling fine
height = 63 #inches
weight = 125.0 #lbs
eyes = "Blue"
teeth = "White"
hair = "Blonde"

print "Let's talk about %r." % name
#%r forces something to become a string by adding single quotes around it
print "She's %d inches tall." % height
print "She's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "She's got %s eyes and %s hair." % (eyes, hair)
print "Her teeth are usually %s depending on how much tea she's had." % teeth

#this line is tricky
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
print "Her height is %d feet, %d inches." % (height/12, height % 12)
print "In centimeters, that's %f." % (height * 2.54)
#%f is a floating point decimal
print "Her weight in kilograms is %d." % (weight * .45392)