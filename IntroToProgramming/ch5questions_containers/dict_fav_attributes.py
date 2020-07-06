dict_favorites = {'height':
		  "6'9",
		  'favorite color':
		  "transparent",
		  'favorite song':
		  "darude sandstorm"
		  }

def ask_user_returns_value():
	while 1 > 0:
		uinput = input('which key do you wish to find the favorite value from: >>>')
		if uinput in dict_favorites:
			print(dict_favorites[uinput])
		if uinput not in dict_favorites:
			print(f'{uinput} not found in {dict_favorites}, "quit" to quit program')
		if uinput == 'quit':
			break

print(dict_favorites)

ask_user_returns_value()
