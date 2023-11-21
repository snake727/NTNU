#Defines value
number = int(input("Input the number you wish to calculate (Must be less than 1000): "))

#Executes while loop to ensure that input is valid
while number < 0 or number > 999:
    print("Number is not valid!")
    number = int(input("Input the number you wish to calculate (Must be less than 1000): "))

#Proceeds with calculations on valid number
number1, number2, number3 = (number // 100), ((number // 10) % 10), (number % 10)
print("The combined value of all numbers =", number1 + number2 + number3)