# csv stands for comma separated values
#  a delimeter like , or | separates values in a csv file.
# popular spreadsheet software often use CSV files.
# data separated by commas are represented as cells in a row on the spreadsheet 
# every line represents a row.

# python has a csv module
# you can use the with-statement to open the file, but CSV module must be used to convert the file object into a CSV object.
# csv module method 'writer' accepts file objects and delimeter
# 'writer' method returns a csv object.
# this csv object has a method 'writerow': accepts a list as a parameter, and writes list to CSV file.
# every item in the list gets written separated by your chosen delimeter
# writerow only creates one row. Call the method multiple times if you wish to write multiple rows.

import csv

with open("st.csv", "w", newline="") as f:
	w = csv.writer(f, delimiter=",") #spelling is delimiter. NOT DELIMETER. :]
	w.writerow(['one','two','three'])
	w.writerow(['four','five','six'])
