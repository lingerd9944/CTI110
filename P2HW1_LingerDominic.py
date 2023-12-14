#Plans for an upcoming vacation by taking user input expenses, budget, and destination to calculate total cost and expected budget
#10/11/23
#CTI-110 P2HW2 - Travel
#Dominic Linger
#

print('This program calculates and displays travel expenses')

#get user input for destination, budget, and expected costs
budget = float(input('\nEnter Budget: '))
destination = input('\nEnter your travel destination:   ')
gas = float(input('\nHow much do you think you will spend on gas?   '))
hotel = float(input('\nApproximately, how much will you need for accomodation/hotel?    '))
food = float(input('\nLast, how much do you need for food?  '))

#print all travel information user input above
print('\n------------Travel Expenses------------')

#prints user input on destination, budget, and expected costs.
print('\nLocation:', '          ', destination)
print('\nInitial Budget:','    ','$' + str(budget))
print('\nFuel:', '              ','$' + str(gas))
print('\nAccomodation:', '      ','$' + str(hotel))
print('\nFood:', '              ','$' + str(food))

print('\n----------------------------------------')

#cost = gas + hotel + food
#budget - cost = remaining balance 
remaining_balance = budget - (gas + hotel + food)

#prints remaining balance 
print('\nRemaining Balance:',' ','$' + str(remaining_balance))  

