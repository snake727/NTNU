#Function of list1 that appends unique numbers into list2 and prints unique numbers
def uniqueNumbers(list1):
    list2 = []
    for x in list1:
        if x not in list2:
            list2.append(x)
    for x in list2:
        print (x, end=' ')


list1 = [int(x) for x in input("Input numbers: ").split()]
print("The unique numbers are: ")
uniqueNumbers(list1)

