list = ['The', 'fox', 'jumped', 'over', 'the', 'fence', '.']

string = ' '.join(list)
print(string)

if string[-1] == '.':
	if string[-2] == ' ':
		string = string[:-2] + '.'

print(string)
