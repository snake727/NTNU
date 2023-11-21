file = open("C:/USCapitals.txt", "r")
capitals = {}

for line in file:
    (key, val) = line.split(",")
    capitals[str(key)] = val

selection = (input(str("Input a state you wish to know the capital of: ")))

if selection in capitals:
    print(capitals[selection])
else:
    print(f'{selection} is not found in the dictionary')
