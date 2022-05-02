import random

# 2 variables to keep track of wins for human & computer seperately
player_wins = 0
computer_wins = 0

# list of options to randmonly choose for computer
options = ["rock", "paper", "scissors"]

while True:
	# take player input for r/p/s choice, and option to quit game
	player_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
	if player_input == "q":
		break

	if player_input not in ["rock", "paper", "scissors"]:
		continue

	random_number = random.randint(0, 2)
	# rock: 0, paper: 1, scissors: 2
	computer_pick = options[random_number]
	print("Computer picked", computer_pick + ".")

	# if conditions to see who wins
	if player_input == "rock" and computer_pick == "scissors":
		print("You won!")
		player_wins += 1
		
	elif player_input == "paper" and computer_pick == "rock":
		print("You won!")
		player_wins += 1
		
	elif player_input == "scissors" and computer_pick == "paper":
		print("You won!")
		player_wins += 1

	elif player_input == computer_pick:
		print("Tie!")

	else:
		print("You lost!")
		computer_wins += 1
		
print("You won", player_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")
