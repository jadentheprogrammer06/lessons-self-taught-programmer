string = 'Who now? When now? What now?'
newlist = string.split("?")

print(newlist)

for question in newlist:
	question_with_mark = question + '?'
	newlist[newlist.index(question)] = question_with_mark

print(newlist)

if newlist[len(newlist)-1] == '?':
	newlist.pop()

print(newlist)
