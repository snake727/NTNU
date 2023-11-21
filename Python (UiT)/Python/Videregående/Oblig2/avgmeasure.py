from datetime import datetime, timedelta 


def fileToDictionary(file):
    filename = open(file, "r") # Open the file
    carInfo = {}

    for line in filename:
        (key, val) = line.split(",")
        carInfo[str(key)] = val
    
    return carInfo

def listSpeeders(filename_a, filename_b, speed_limit, distance):
    dict1 = fileToDictionary(filename_a)
    dict2 = fileToDictionary(filename_b)

    d1 = Counter(dict1)
    d2 = Counter(dict2)
    d3 = d2 - d1
    
    print(d3)

listSpeeders("C:/box_a.txt", "C:/box_b.txt", 60, 5)

