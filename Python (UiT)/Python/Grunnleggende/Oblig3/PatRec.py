def isConsecutiveFour():
    amount = int(input("Input the amount of numbers: "))
    lst = list(map(int,input("Input the numbers: ").strip().split()))[:amount]
    size = len(lst)

    for i in range(size - 3):
        if lst[i] == lst[i + 1] and lst[i + 1] and lst[i + 1] == lst[i + 3]:
             print("The number series has consecutive fours!")
    

isConsecutiveFour()