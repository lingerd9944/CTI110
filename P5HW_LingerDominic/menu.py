#Menu
#12/2/23
#CTI-110 P5HW
#Dominic Linger

print('Welcome to Math Quiz')

def menu():  #Making a menu function to display menu at start, when each question is complete, and if user enters character other than '1', '2', or '3'
    print('\nMAIN MENU')
    print('--------------------')
    print('1. Adding Random Numbers')
    print('2. Subtracting Random Numbers')
    print('3. Exit')
    selection = input('Please choose one of the menu options: ') #Gets user input to decide if they want to add, subtract, or exit
    if selection != '1' and selection != '2' and selection != '3':  #filters all others inputs besides '1', '2', and '3'
        print("\nSorry, that is not one of the options. Please select '1', '2', or '3'.") #prints to let user know what to enter
        selection = menu() #recalls function to loop until user enters proper input 
    return selection