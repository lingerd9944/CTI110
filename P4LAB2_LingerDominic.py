#Gets integer input from user
num1 = int(input("Please enter an integer:"))
num2 = int(input("Please enter an integer that is larger than the first ineteger:"))
i = 0

#Prints an error message if user enters a smaller integer from their second input
if num2 < num1:
    print("Second integer can't be less than the first.")

#Starts the loop to print out increments of 5 between the two integers the user input
while num1 <= num2:
    i += 1      #loop counter for the second if statement
    print(num1, end=" ")
    num1 = num1 + 5
    
#if statement to print a line break after the integers increments have finished printing
if i > 0:
    print("")
    

