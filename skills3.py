from random import sample
from datetime import date
import csv

print (str(date.today()))

skills = [ 'bar muscle up',
					 'ring muscle up',
					 'toes to bar',
					 'chest to bar',
					 'double unders',
					 'handstand walk',
					 'pistols',
					 'rope climbs',
					 'ring dips',
					 'handstand push up',
					 'burpee box jump'
	]

skills_done = []
with open('randomizer.csv', 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		for i in range(1,len(row)):
			skills_done.append(row[i])
#counts = dict((x, skills_done.count(x)) for x in set(skills_done))
#print(counts)

y_or_n = 'n'
while (y_or_n == 'n'):

	skill_choices = sample(skills, 3)
	
	print('\n')
	print('choices for today:\n')
	print(skill_choices)
	print('\n')
	print('have been done:\n')
	for skill in skill_choices:
		print('{}:{}'.format(skill, skills_done.count(skill)))

	y_or_n = input('is that ok y/n ').lower()
	print('\n')
	
	if y_or_n == 'y':
		# save the choices to a list with the date
		today = date.today()
		with open('randomizer.csv', 'a') as f:
			f.write('{},{},{},{}\n'.format(str(today), skill_choices[0], skill_choices[1], skill_choices[2]))
		
		
