import random

numOfBalls = int(input("Input the number of balls you wish to drop: "))
numOfSlots = int(input("Input the amount of slots you wish to use: "))
numOfSteps = int(numOfSlots - 1)

slots = [] #List for slots and stored data

for i in range(numOfSlots):
    slots.append(i * 0)

if (numOfSlots % 2 == 0):
    numOfSteps -= 1

for i in range(numOfBalls):
    pattern = str()
    position = (numOfSlots // 2)
    if (numOfSlots % 2 == 0):
        r = random.randint(0,1)
        if r == 0:
            position -= 1   #Left
            pattern += "L"
        else:
            pattern += "R"

    prev_p = -1
    for j in range(numOfSteps):
        p = random.randint(0,1)
        if p == 0:
            if p == prev_p:
                position -= 1 #Left
            pattern += "L"
        else:
            if p == prev_p:
                position += 1 #Right
            pattern += "R"
        if p != prev_p:
            prev_p = p
        else:
            prev_p = -1
    slots[position] += 1
    print(pattern)

for v in reversed(range(1, max(slots)+1)):
   print(''.join('0' if x >= v else ' ' for x in slots))