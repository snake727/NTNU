#Prompts the user for input and then stores values for later
year = int(input("Enter the year you wish to check: "))
month = int(input("Enter the number of the month in said year you wish to check: "))
days = int()

#Determines whether a year is a leap year or not
isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) 

#Nested if, elif and else statement to output correct answer
if month == 1:
    print("There are 31 days in month number", month, "in the year", year)
elif month == 2:
    if isLeapYear:
        print ("There are 29 days in month number", month, "in the year", year,)
    else:
        print ("There are 28 days in month number", month, "in the year", year,)
elif month == 3:
    print("There are 31 days in month number", month, "in the year", year)
elif month == 4:
    print("There are 30 days in month number", month, "in the year", year)
elif month == 5:
    print("There are 31 days in month number", month, "in the year", year)
elif month == 6:
    print("There are 30 days in month number", month, "in the year", year)
elif month == 7:
    print("There are 31 days in month number", month, "in the year", year)
elif month == 8:
    print("There are 31 days in month number", month, "in the year", year)
elif month == 9:
    print("There are 30 days in month number", month, "in the year", year)
elif month == 10:
    print("There are 31 days in month number", month, "in the year", year)
elif month == 11:
    print("There are 30 days in month number", month, "in the year", year)
elif month == 12:
    print("There are 31 days in month number", month, "in the year", year)
