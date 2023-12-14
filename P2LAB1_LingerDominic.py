''' Type your code here. '''

gas_milage = float(input("Please enter your car's gas milage:\n"))
gas_cost = float(input("Please enter the cost of gas:\n"))

cost_miles = (20 / gas_milage) * gas_cost
cost_miles2 = (75 / gas_milage) * gas_cost
cost_miles3 = (500 / gas_milage) * gas_cost

print(f'{cost_miles:.2f} {cost_miles2:.2f} {cost_miles3:.2f}')