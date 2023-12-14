#CTI-110
#P4HW2 - Salary Calculator
#Dominic Linger
#11/8/23
#

#Initial employee name to start the while loop 
empName = input("Enter employee's name or \"Done\" to terminate: " )

#Defining variables for counters and to start loops 
empCounter = 0
totalOvertimePay = 0
totalRegularPay = 0
totalGross = 0

#starting loop that will continue until "Done" is entered by user
while empName != 'Done':
    empHours = float(input('\nHow many hours did %s work? ' %empName))  #Asking for the number of hours employee has worked and storing in variable
    empPayRate = float(input("\nWhat is %s's pay rate? " %empName)) #Storing employees pay rate in variable 

    overtimePayRate = empPayRate + (empPayRate * .5)  #Calculator for determining each employees overtime pay rate

    #if statement for determining the amount of hours an employee worked over 40 hours
    if empHours > 40:
        overtimeHours = empHours - 40
    else:
        overtimeHours = 0
    
    #calculations for both regular and overtime pay by multiplying the reg hours and ovetime hours by their respective payrates 
    overtimePay = overtimePayRate * overtimeHours
    regPay = (empHours - overtimeHours) * empPayRate

    #gross pay calculation just addding both regular and overtime pay 
    grossPay = overtimePay + regPay

    #Prints results of the pay calculations and the regular hours and overtime hours each employee worked
    print("\n--------------------------------------")
    print("\nEmployee name:", empName)
    print("\nHours Worked   Pay Rate   OverTime   Overtime Pay     RegHour Pay     Gross Pay")
    print("-------------------------------------------------------------------------------------")
    print(f'{empHours:<15.1f}{empPayRate:<11.1f}{overtimeHours:<11.1f}{overtimePay:<17.2f}${regPay:<15.2f}${grossPay:<5.2f}')

    #counter to keep track of the number of employees being entered 
    empCounter += 1

    #starts a variable to loop and add all of the different pays for all employees together 
    totalOvertimePay = totalOvertimePay + overtimePay
    totalRegularPay = totalRegularPay + regPay
    totalGross = totalGross + grossPay

    #Asks for employee name at the end of the loop to check if "Done" is entered at the beginning of the next loop 
    empName = input("\nEnter employee's name or \"Done\" to terminate: ")

#Small if statement to print total pay and the number of employees entered as long as "Done" is entered at the end of the loop 
if empName == "Done":
    print("\nTotal number of employees entered: ", empCounter)
    print("Total amount paid for overtime: ", f'${totalOvertimePay:.2f}')
    print("Total amount paid for regular hours: ", f'${totalRegularPay:.2f}')
    print("Total amount paid in gross: ", f'${totalGross:.2f}')