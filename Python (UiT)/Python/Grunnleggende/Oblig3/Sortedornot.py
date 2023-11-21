#Defines function that sorts list
def isSorted(lst):
    for i in range(len(lst) - 1):
        currentMin = min(lst[i : ])
        currentMinIndex = i + lst[i : ].index(currentMin)
        
        if currentMinIndex != i:
            lst[currentMinIndex], lst[i] = lst[i], currentMin
    return lst

#Defines function that uses previous function in order to compare them using a copy of original list
def main():
        numbersAmount = int(input("Input your amount of numbers: "))
        lst = list(map(int,input(f"\nInput a series of {numbersAmount} numbers of your choice. \n(Numbers must be separated with one space!): ").strip().split()))[:numbersAmount]
        originalLst = lst[:]

        isSorted(lst)

        if lst == originalLst:
            print("List is already sorted!")
        else:
            print("List is not sorted!")
 
main()