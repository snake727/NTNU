#Loop which ensures valid input to be evaluated
#Loop will break when all conditions have been met, and evaluation is complete
while True:
    try:  
        inputNumber = int(input("Input positive number with three digits: "))
        while inputNumber < 100 or inputNumber > 999: 
            print("Number must be a positive three digit number!")
            inputNumber = int(input("Input positive number with three digits: "))
        firstNumber = inputNumber // 100
        secondNumber = inputNumber % 10
        if firstNumber == secondNumber:
            print(f"{inputNumber} is a palindrome!")
        else:
            print(f"{inputNumber} is not a palindrome!")
        break
    except:
        print("Please input a valid number!")
