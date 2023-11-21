#Function for reversing number
def reverse(inputNumber):
    return int(str(inputNumber)[::-1])

#Function that compares reversed number with inputnumber and determines palindrome
def isPalindrome(inputNumber):
    if reverseNumber == inputNumber:
        (print("Number is a palindrome!")) 
    else:
        print("Number is not a palindrome!")

#Loop for ensuring correct input
while True:
    try:
        inputNumber = int(input("Type in a number: "))
        reverseNumber = reverse(inputNumber)
        isPalindrome(inputNumber)
        break
    except:
        print("Must be a positive number!")

