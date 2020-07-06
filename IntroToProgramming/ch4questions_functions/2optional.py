# note2self: numbers CANNOT BE USED IN FUNCTION NAMES
def three_required_two_optional(a, b, c, d=None, e=None):
	'''
	3required2optional([required parameters: a, b, c], [optional parameters: d, e])
	a, b, c are required parameters (3 numbers must be passed as parameters)
	d and e are optional parameters (if no value passed in to parameters, d and e are None
	'''
	return a, b, c, d, e

optional = three_required_two_optional

print(optional(3,4,5))

print(optional(3,4,1,2,4))

print(optional())
