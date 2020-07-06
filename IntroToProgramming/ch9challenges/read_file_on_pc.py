import os
filename = 'movie_anime-list.txt'

i = os.path.join('/', 'mnt','c','Users','JADEN','Documents')


print(i)

filepath = os.path.join(i, filename)
with open(filepath, "r") as f:
	print(f.read())


