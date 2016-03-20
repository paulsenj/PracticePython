print "Player 1, what do you choose? Rock, Paper, or Scissors?"
player_1 = raw_input().lower()
print "Player 2, what do you choose? Rock, Paper, or Scissors?"
player_2 = raw_input().lower()

rock = "rock"
paper = "paper"
scissors = "scissors"

rock > scissors
paper > rock
scissors > paper

if player_1 > player_2:
	print "Congratulations Player 2! Your {} beat Player 1's {}.".format(player_2, player_1)

if player_2 > player_1:
	print "Congratulations Player 2! Your {} beat Player 1's {}.".format(player_2, player_1)
