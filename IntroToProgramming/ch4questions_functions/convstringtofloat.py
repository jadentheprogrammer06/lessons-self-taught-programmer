# if we try to get input in function parameter right away, it is a bit harder to really use exceptions to test input
def convert_str_to_float():
	'''
	when function called:
		try: asks user for input.
			will return input if input can be converted to a float
		except ValueError:
			tells user to try again. ValueError found; input invalid.
	'''
	while 1 > 0:
		try:
			uinput=float(input('enter a float >>>'))
			return uinput
		except ValueError:
			print('please try again')
print(convert_str_to_float())
# have to print([function called]) in order to print result
