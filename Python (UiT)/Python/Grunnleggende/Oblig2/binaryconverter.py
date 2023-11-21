#Loop for ensuring the input is within given parameters
while True:
    try:
        decimalNumber = int(input("Input a decimal number between 0 and 15:" ))
        if decimalNumber < 1 or decimalNumber > 15:
            raise ValueError #This will print the error message and restart the loop
        break
    except ValueError:
        print("The number must be in the range of 1-15.")

#Creates a function for the conversion of number to binary
def binaryConvert(decimalNumber):
    if decimalNumber >= 1:
        binaryConvert(decimalNumber // 2)
        print(decimalNumber % 2, end = '')

#Calls function to output binary
binaryConvert(decimalNumber)