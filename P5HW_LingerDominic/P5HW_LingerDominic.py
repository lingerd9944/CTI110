
import random  
import menu 

def compare(num3, i):  
    user_num = int(input('Enter answer: '))
    while user_num != num3: 
        if user_num > num3:
            print('Sorry, guess is too high.')
        if user_num < num3:
            print('Sorry, guess is too low')
        user_num = int(input('Try again: '))
        i += 1 
    return i 

def math(num1, num2, selection):   
    print(' ', num1)
    if selection == '1': 
        print('+', num2)
        num3 = num1 + num2  
    else: 
        print('-', num2)  
        num3 = num1 - num2 
    return num3  

i = 1  

nottrue = input('Enter a number') + 3

print('Welcome to Math Quiz')
selection = menu.menu()  

while selection == '1' or selection == '2':   
    num1 = random.randint(1, 1000)  
    num2 = random.randint(1, 1000)
    j = compare(math(num1, num2, selection), i)  
        
    print('Congratulations!!! Your answer is correct.') 
    print('Number of guesses:', j)  
    selection = menu.menu() 

if selection == '3': 
    print('\nThank you for playing...')
    print('Bye!!')


