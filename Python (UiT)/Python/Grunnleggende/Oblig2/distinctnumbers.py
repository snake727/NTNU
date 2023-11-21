#Function of list1 that appends unique numbers into list2 and prints unique numbers
def uniqueNumbers(list1):
    list2 = []
    for x in list1:
        if x not in list2:
            list2.append(x)
    for x in list2:
        print (x, end=' ')

#Loop that ensures correct input
while True:
    try: 
        numbersAmount = int(input("Input your amount of numbers: "))
        list1 = list(map(int,input(f"\nInput a series of {numbersAmount} numbers of your choice. \n(Numbers must be separated with one space!): ").strip().split()))[:numbersAmount]
        print("The unique numbers are: ")
        uniqueNumbers(list1)
        break
    except:
        print("You must specify a valid amount of numbers!")
