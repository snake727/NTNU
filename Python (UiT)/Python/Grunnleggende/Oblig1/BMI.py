#Prompts user for input
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in centimeters: "))

#Calculates BMI
bmi = weight / ((height / 100) ** 2)

#Outputs BMI
print("Your BMI is", bmi)