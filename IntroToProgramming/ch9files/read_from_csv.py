# make sure you've created
# the file from the previous
# example

import csv

with open("st.csv", "r") as f:
	r = csv.reader(f, delimiter = ',')
	for row in r:
		print(','.join(row))

