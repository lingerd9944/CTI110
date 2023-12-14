# Define your function here.
def days_in_feb(year):
    if (year % 100 == 0 and year % 400 == 0) or (year % 100 !=0 and year % 4 == 0):
        days = 29
    else:
        days = 28
    return days
    
if __name__ == '__main__':
    choice = input("Would you like to know how many days February has in any given year? 'Yes' or 'No'?")
    while choice == 'Yes':
        year = int(input('\nPlease enter a year: \n'))
        print(year, 'has', days_in_feb(year), 'days in February.')
        choice = input("Would you like to continue? 'Yes' or 'No'?")
    