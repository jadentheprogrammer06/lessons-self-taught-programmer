numlist = [12, 423, 10, 11, 69, 420, 1, 23, 9, 6, 7]

while 1 > 0:
	try:
		i = input('please guess a integer number from the list. ("q" to quit)')
		if 'q' in i:
			break
		if  int(i) in numlist:
			print('you guessed correct!')
			a = input(' want to go again? ("n" for no to exit program) >>> ')
			if "n" in a:
				break
	except ValueError:
		print('please enter an integer')
