nested_lists = [['Top Gun', 'Risky Business', 'Minority Report'], ['Titanic', 'The Revenant', 'Inception'],
['Training Day', 'Man on Fire', 'Flight']]
newlist = []
for i in range(3):
	newlist.append(input(f'enter item {i} in your custom list.'))
import csv

for list in nested_lists:
	print(list)

with open('listrows.csv', 'w') as f:
	w = csv.writer(f, delimiter=',')
	for list in nested_lists:
		w.writerow(list)
	w.writerow(newlist)
