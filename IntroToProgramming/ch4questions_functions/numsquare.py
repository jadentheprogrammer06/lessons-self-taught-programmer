
def numsquared():
	'''
	asks user for input of integer number.
	returns that integer squared.
	'''
	while 1 > 0:
		try:
			i = int(input('what number would you like to square? >>> '))
			return i**2
		except (ZeroDivisionError, ValueError):
			print('Invalid Input, sir. Please try again')

print(numsquared())
