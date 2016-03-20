# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
# compare them, print out a message of congratulations to the winner,
# and ask if the players want to start a new game)

print "Player 1, what do you choose? Rock, Paper, or Scissors?"
player_1 = raw_input().lower()
print "Player 2, what do you choose? Rock, Paper, or Scissors?"
player_2 = raw_input().lower()

options = ["rock", "paper", "scissors"]

if player_1 in options and player_2 in options:
	if player_1 == "rock" and player_2 == "paper":
		print "Congratulations Player 2! Paper beats rock."
	elif player_1 == "rock" and player_2 == "scissors":
		print "Congratulations Player 1! Rock beats scissors."
	elif player_1 == "rock" and player_2 == "rock":
		print "It's a tie. Try again!"
	elif player_1 == "paper" and player_2 == "rock":
		print "Congratulations Player 1! Paper beats rock."
	elif player_1 == "paper" and player_2 == "scissors":
		print "Congratulations Player 2! Scissors beats paper."
	elif player_1 == "paper" and player_2 == "paper":
		print "It's a tie. Try again!"
	elif player_1 == "scissors" and player_2 == "paper":
		print "Congratulations Player 2! Scissors beats paper."
	elif player_1 == "scissors" and player_2 == "rock":
		print "Congratulations Player 1! Rock beats scissors."
	elif player_1 == "scissors" and player_2 == "scissors":
		print "It's a tie. Try again!"
else: 
	print "One of you picked something that wasn't rock, paper, or scissors. Try again!"
