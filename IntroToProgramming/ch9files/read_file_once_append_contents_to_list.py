
# can only call 'read' on a file once. If you plan on using it multiple times, it is a good idea to save the file's contents to a variable or a container object.
# here we read the file's data then append it to a list

my_list = list()

with open("st.txt", "r") as f:
	my_list.append(f.read())

print(my_list)
