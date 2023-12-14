#CTI-110
#P4HW1 - Score List
#Dominic Linger
#11/7/23
#

#Defining variable for counters and defining the set the code will add grades to
i = 1
testGrades = []

#Getting the number of repitions the loop will go through
num = int(input('How many scores do you want to enter? '))

#starting the loop that will continue until the inital counter "i" is equal to the number of grades the person needs to input
while i <= num:
    
    score = float(input("Enter score #%s: " % i)) #Loops to get all grades from student
    if (score >= 0) and (score <= 100): #if statement to determine if the grade is between 0 and 100
        testGrades.append(score) #if the above statement is correct, then that grade will be added to the list
    while (score < 0) or (score > 100): #another loop for if the above if statement is not met. i.e. a grade below 0 or above 100
       print("INVALID Score entered!")
       print("Score should be between 0 and 100")
       score = float(input("Enter score #%s again: " % i))
       if (score >= 0) and (score <= 100): #another if statement to determine is grade is now between 0 and 100 to add to the list 
        testGrades.append(score) 
    i += 1

lowestScore = min(testGrades) #gets lowest score in the list
testGrades.remove(lowestScore) #removes the lowest score in the list
avgGrade = sum(testGrades) / len(testGrades) #finds average of all remaining grades in list


#set of if and elif statements to detemine letter grade based on average grade
if avgGrade >= 90:
    grade = 'A'
elif avgGrade >= 80:
    grade = 'B'
elif avgGrade >= 70:
    grade = 'C'
elif avgGrade >= 60:
    grade = 'D'
else:
    grade = 'F'



#prints all results of the list including the average of remaining grades, the removed grade, and the letter grade 
print('\n------------Results------------')
print('\nLowest Grade', '', ':', '    ', f'{lowestScore:.1f}')
print('\nModified List', ':', '    ', testGrades)
print('\nAverage', '     ',':', '    ', f'{avgGrade:.2f}')
print('\nGrade', '       ',':', '    ',    grade)
print('\n-------------------------------')
