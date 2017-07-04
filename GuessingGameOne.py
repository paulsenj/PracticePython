#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

#Extras:

#Keep the game going until the user types “exit”
#Keep track of how many guesses the user has taken, and when the game ends, print this out.
c = ""
g = 0 

import random
r = random.randint(1,10)


while c != "exit":
  u = int(raw_input("Pick a number between 1 and 10. I'll tell you if it matches mine!"))
  
  g += 1
  
  if u == r:
    print "Congratulations, you got it exactly right!"
    print "You made {} guesses!".format(g)
    break
  elif u > r:
    print "You guessed too high."
  elif r > u:
    print "You guessed too low."
  
  c = raw_input("Press any key to continue, or type exit to quit.") 

if c == "exit":
  break

