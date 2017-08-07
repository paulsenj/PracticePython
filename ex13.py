# Write a program that asks the user how many Fibonnaci numbers to generate
# and then generates them. Take this opportunity to think about how you can
# use functions. Make sure to ask the user to enter the number of numbers in
# the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of
# numbers where the next number in the sequence is the sum of the previous two
# numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13)

fibonnaci = [1,1]
count = 12
one = 1
print "How many fibonnaci numbers should I print?"
print count

while (count-2 >0):
	total = fibonnaci[-1]+fibonnaci[-2]
	fibonnaci.append(total)
	count = count-1
print fibonnaci