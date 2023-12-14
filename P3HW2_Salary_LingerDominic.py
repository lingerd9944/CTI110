#CTI-110
#P3HW2 - Salary
#Dominic Linger
#10/24/23
#

#Declaring vars I will use for program to calculate employees pay
empName = input("Enter employee's name: ")
empHours = float(input('\nEnter number of hours worked: '))
empPayRate = float(input("\nEnter employee's pay rate: "))
overtimeHours = 0
regPay = 0

#Calculates employees overtime pay rate
overtimePayRate = empPayRate + (empPayRate * .5)


#If statement to get the number of overtime hours an employee worked
if empHours > 40:
    overtimeHours = empHours - 40
else:
    overtimePay = 0
    
#calculate overtime pay based only on the amount of hours employee worked over 40 hours
overtimePay = overtimePayRate * overtimeHours

#calculates the pay for the hours the employee worked less than or equal to 40 hours
regPay = (empHours - overtimeHours) * empPayRate

#add both the regular pay and the overtime pay to get the gross pay for the employee
grossPay = overtimePay + regPay

#prints results in a table
print("\n--------------------------------------")
print("\nEmployee name:", empName)
print("\nHours Worked   Pay Rate   OverTime   Overtime Pay     RegHour Pay     Gross Pay")
print("-------------------------------------------------------------------------------------")
print(f'{empHours:<15.1f}{empPayRate:<11.1f}{overtimeHours:<11.1f}{overtimePay:<17.2f}${regPay:<15.2f}${grossPay:<5.2f}')



