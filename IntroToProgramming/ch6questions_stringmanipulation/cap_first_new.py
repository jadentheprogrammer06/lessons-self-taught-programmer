string = 'aldous huxley was born in 1894.'
newstring = ''

# This program capitalizes the first two words in the given string.
# It may potentially be modified to capitalize any words that are considered a name value
# which were found in a list/container of names.


string = string.capitalize()

c = 0

for i, char in enumerate(string):
	if char == ' ':
		c += 1
		newstring = ''
		newstring += string[i+1:].capitalize()
		if c == 1:
			string = string[:i]
			string += ' ' + newstring

print(string)
print('#capitalizes the first two words in given string by enumerating and capitalizing both the original and the slice for the second word')

