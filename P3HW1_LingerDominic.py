# CTI-110-0903
# Dominic Linger
#P3HW1 - List
#10/18/2023


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('\nEnter grade for Module 2: '))
mod_3 = float(input('\nEnter grade for Module 3: '))
mod_4 = float(input('\nEnter grade for Module 4: '))
mod_5 = float(input('\nEnter grade for Module 5: '))
mod_6 = float(input('\nEnter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
sum = sum(grades)
avg = sum / len(grades)

#prints results from grades
print('\n------------Results------------')
print('\nLowest Grade:', '     ', f'{low:.1f}')
print('\nHighest Grade:', '    ', f'{high:.1f}')
print('\nSum of Grades:', '    ', f'{sum:.1f}')
print('\nAverage:', '          ', f'{avg:.2f}')
print('\n-------------------------------')

# determine letter grade for average
if avg >= 90:
    print('\nYour grade is: A')
elif avg >= 80:
    print('\nYour grade is: B')
elif avg >= 70:
    print('\nYour grade is: C')
elif avg >= 60:
    print('\nYour grade is: D')
else:
    print('\nYour grade is: F') # TO DO: finish this
