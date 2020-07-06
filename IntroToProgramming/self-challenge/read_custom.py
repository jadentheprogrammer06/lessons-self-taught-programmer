import os #we are importing the os module which contains the directory functions


while 1 == 1:
	try:
		y = input('reading file: [input file name including extension] >>> ')
		if y == 'q':
			break
		with open(y, 'r') as user_read:
			print(f'\nreading file "{y}":')
			x = user_read.read()
			print(x)
	except FileNotFoundError:
		print(f'\n')
		print('list of files in current directory: ', os.listdir('.'))
		print(f'file "{y}" not found. try again or type "q" to quit.')
		continue
