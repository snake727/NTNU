while True:
    try:
        #Prompts for input
        inputSeconds = int(input("Enter total amount of seconds: "))

        #Divmod can easily achieve this simply by returning the remainder and quotient by dividing
        m, s = divmod(inputSeconds, 60)
        h, m = divmod(m, 60)

        #String formatting for correct output
        print(f'{h:d}:{m:02d}:{s:02d}')
        break
    except:
        print("Input must be a number!")
    