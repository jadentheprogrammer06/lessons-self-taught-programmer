import random
import csv
randomly_selected_words = ['banana', 'fortnite', 'minecraft', 'hobgoblins', 'water', 'apple', 'microsoft', 'google', 'iphone', 'switch', 'table', 'chair', 'zombie', 'elonmusk', 'johnwick', 'killerbeans', 'mustache', 'linux', 'windows']
option_b = randomly_selected_words[random.randint(0, len(randomly_selected_words)-1)]
def hangman(word):
	wrong = 0
	win = False
	stages = ["",
		 "________    ",
		 "|      |    ",
		 "|      |    ",
		 "|      0    ",
		 "|     /|\   ",
		 "|     / \   ",
		 "|           "
		 ]
	rletters = list(word)
	board = ["_"] * len(rletters) # board = "_" * len(rletters) # previously used. instead of string we want to use a list of underscores to easily modify indices.
	while win == False:
		print('hint: guess one letter in the word: ', " ".join(board), "\nhint: it could be the name of a person, character, place, thing, or brand.")
		playerguess = input('[guess a letter] >>>')
		if playerguess in rletters:
			guessindice = rletters.index(playerguess)
			rletters[guessindice] = '#'
			board[guessindice] = playerguess #
			print(' '.join(board))
		else:
			wrong += 1
		print("\n".join(stages[0:wrong+1]))
		print('\n')
		if wrong == (len(stages) - 1):
			print('*your brutal death is put on public display.')
			for i in range(3):
				input('\n\n')
				print('Nothing you can do about it. You are a ghost now. :) \n')
			print(' '.join('GAMEOVER'))
			print('the correct word was: {}'.format(word), '\n')
			break
		if "_" not in board:
			print(" ".join(board))
			print('You correctly guessed the word "{}"! Congrats!'.format(word))
			print(" ".join("YOU WON THE GAME"))
			win = True
			username = input('enter your name to be submitted to the leaderboard:\n>>>')
			with open('leaderboard.csv', 'a', newline='') as leaderboard_csv:
				write_leaderboard = csv.writer(leaderboard_csv, delimiter='|')
				write_leaderboard.writerow(['user:{}'.format(username), 'word:"{}"'.format(word)])
			break
		else:
			continue


runscript = True
while runscript == True:
	i = input('\n\nWelcome to Hang Man. Enter "quit" to exit. Enter "scores" for leaderboard.\nPlease select your mode: ["A"]player one inputs a custom word. OR... ["B"]player two guesses a randomly-generated word.\n>>>')
	if i == "A":
		customword = input('Enter your custom word: [word that uses letters]\n>>>')
		hangman(customword)
	if i == "B":
		hangman(option_b)
	if i == "scores" or i == "leaderboard":
		print('\n')
		with open("leaderboard.csv", "r") as scores:
			read_scores = csv.reader(scores, delimiter='|')
			for rows in read_scores:
				print('|'.join(rows))
	if i == "quit":
		break
