# code in module3 (how module1 could be changed so that its code is not run when the module is imported into another script.

if __name__ ==  "__main__":
	print('Hello')

# functions should still be able to be called when imported.

def print_hello():
	print('Hello World')
