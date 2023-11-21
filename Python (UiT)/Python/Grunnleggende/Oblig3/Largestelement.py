matrix = [] # Create an empty list

numberOfRows = int(input("Enter the amount of rows: "))
numberOfColumns = int(input("Enter the number of columns: "))
 
#Loops generation of rows based on number of columns
for x in range(numberOfColumns):
    matrix.append([int(y) for y in input("Input a row of numbers with one space inbetween: ").split()])

#Function for finding the biggest number and its coordinates (Requires list and number of rows)
def locatelargest(list, rows):
    maxNum = max(map(max, list))
    matrix_dim = len(matrix[0])
    item_index = 0

    for rows in list:
        for i in rows:
            if i == maxNum:
                break
            item_index += 1
        if i == maxNum:
            break

    maxCoords = (int(item_index / matrix_dim), item_index % matrix_dim)
    print(f"Note: Only returns location of first occurrence!\nThe location of the largest element is at {maxCoords}")

locatelargest(matrix, numberOfRows)