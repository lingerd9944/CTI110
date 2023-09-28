#Plans for an upcoming vacation by taking user input expenses, budget, and destination to calculate total cost and expected budget
#9/28/23
#CTI-110 P1HW2 - Travel Expense
#Dominic Linger

print('This program calculates and displays travel expenses')

#get user input for destination, budget, and expected costs
budget = int(input('Enter Budget:\n'))
destination = input('Enter your travel destination:\n')
gas = int(input('How much do you think you will spend on gas?\n'))
hotel = int(input('Approximately, how much will you need for accomodation/hotel?\n'))
food = int(input('Last, how much do you need for food?\n'))

#print all travel information user input above
print('\n------------Travel Expenses------------')

#prints user input on destination, budget, and expected costs.
print('Location:', destination)
print('Initial Budget:', budget)
print('\nFuel:', gas)
print('Accomodation:', hotel)
print('Food:', food)

#cost = gas + hotel + food
#budget - cost = remaining balance 

#prints remaining balance by adding all expected costs and subtracting that total from the budget
print('\nRemaining Balance:', budget - (gas + hotel + food))  

