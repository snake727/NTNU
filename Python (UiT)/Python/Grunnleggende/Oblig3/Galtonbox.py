import random as r

def galton(slots, balls):
    slots = [0] * (slots)
    for i in range(balls):
        pattern = ""
        position = 0
        for j in range(0, slots - 1):
            turn = r.randint(0, 1)
            if turn == 1:
                position += 1
                pattern += "L"
            else:
                pattern += "R"
        slots[position] = slots[position] + 1
        print(pattern)
    return slots

result = galton(int(input("Input amount of slots: ")),int(input("Input amount of balls that run through: ")))

for v in reversed(range(1, max(result)+1)):
   print(''.join('0' if x >= v else ' ' for x in result))