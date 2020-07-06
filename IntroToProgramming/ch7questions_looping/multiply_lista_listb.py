list_one = [8, 19, 148, 4]
list_two = [9, 1, 33, 83]
output = list()

print(list_one, list_two)

for x in list_one:
	y = list_one.index(x)
	output.append(x * list_two[y])

print(output)
