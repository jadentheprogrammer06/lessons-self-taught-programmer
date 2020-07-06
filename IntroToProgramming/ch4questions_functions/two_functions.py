def function_a(a=int(input('variable a for function_a : >>>'))):
	print('var / 2')
	return a / 2

def function_b(b):
	print('var * 4 (function a returned result passed as parameter in function b')
	return b * 4

print(function_a())

result_function_a = function_a()

print(function_b(result_function_a))
