#CTI-110
#P2HW2 - List
#Dominic Linger
#Date
#

#Collects grade information into a list
testGrades = [float(input('Enter grade for Module 1:  ')), float(input('\nEnter grade for Module 2:  ')), float(input('\nEnter grade for Module 3:  ')), 
              float(input('\nEnter grade for Module 4:  ')) , float(input('\nEnter grade for Module 5:  ')), float(input('\nEnter grade for Module 6:  '))]

#finds sum of all grades entered
#the sum of grades will be equal to all the grades entered by user. Ex. sum = g1 + g2 + g3 .....
sumGrade = sum(testGrades)

#gets the average score of all grades entered
#average will be equal to the sum of all grades divided by the amount of numbers that make up the sum. Ex. average equal = (g1 + g2)/2
avgGrade = sumGrade / len(testGrades)

#finds the lowest grade entered and stores it to variable 'lowestGrade'
#parses all inputs for the lowest integer value
lowestGrade = min(testGrades)

#finds the highest grade entered and stores it to variable 'highestGrade'
#parses all inputs for highest integer value
highestGrade = max(testGrades)

#prints the lowest grade, highest grade, the grade average, and the sum of all grades entered by user
print('\n------------Results------------')
print('\nLowest Grade:', '     ', f'{lowestGrade:.2f}')
print('\nHighest Grade:', '    ', f'{highestGrade:.2f}')
print('\nSum of Grades:', '    ', f'{sumGrade:.2f}')
print('\nAverage:', '          ', f'{avgGrade:.2f}')
print('\n-------------------------------')