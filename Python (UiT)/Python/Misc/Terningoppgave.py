import random
from collections import Counter

def dice():
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    total = roll1 + roll2
    return total

def main():
    list1 = []
    for i in range(0, 1000):
        list1.append(dice())
    
    occurences = dict((elem, list1.count(elem)) for elem in set(list1))
    print("Total Simulated Expected")
    print("       Percent   Percent")
    for i in range(2,12):
        actual_percent = float(occurences.get(i) / 10)
        for j in range(1,7):
            if j == i:
                break
            else:
                theoretical_percent = float((j / 36)*100)


        theoretical_percent = "{:.2f}".format(theoretical_percent)
        actual_percent = "{:.2f}".format(actual_percent)

        print(f"{i}_______{actual_percent}_______{theoretical_percent}")

main()
    
