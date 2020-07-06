q1 = input('what is your name ? ')
q2 = input('what is your favorite programming language ? ')
questions = {'name':q1,
	     'favorite language':q2
	    }

with open('question_answered.txt', 'w') as f:
	for key, answer in questions.items():
		f.write(key+':'+answer+'\n')
