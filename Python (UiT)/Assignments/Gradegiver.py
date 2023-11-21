grades = [int(x) for x in input("Input the grades you wish to grade: ").split()]

best = max(grades)
i = 0

while i < len(grades):
    if grades[i] >= best - 10:
        print(f"Student {i} score is {grades[i]} and grade is A")
    elif grades[i] >= best - 20:
        print(f"Student {i} score is {grades[i]} and grade is B")
    elif grades[i] >= best - 30:
        print(f"Student {i} score is {grades[i]} and grade is C")
    elif grades[i] >= best - 40:
        print(f"Student {i} score is {grades[i]} and grade is D")
    elif grades[i] < best - 40:
        print(f"Student {i} score is {grades[i]} and grade is F")
    i += 1
    