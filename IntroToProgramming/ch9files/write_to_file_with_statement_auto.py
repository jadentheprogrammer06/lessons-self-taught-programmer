# this code will open and write to the fle, then automatically close it after it is run because it is using the "with-statement"

with open("st.txt", "w") as f:
	f.write('Hi from Python! Now using with-statements!')

