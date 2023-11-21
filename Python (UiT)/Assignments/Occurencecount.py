numbers = [int(x) for x in input("Input numbers: ").split()]

occurrences = {}

for i in numbers:
    if i in occurrences:
        occurrences[i] += 1
    else:
        occurrences[i] = 1

for key,value in occurrences.items():
    if occurrences[i] > 1:
        print("{0} occurs {1} times".format(key, value))
    else:
        print("{0} occurs {1} time".format(key, value))