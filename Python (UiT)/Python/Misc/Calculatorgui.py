from tkinter import *

class Calculator:
    def __init__(self, log = 0):
        self.log = [log]

    def calculate(self, operand1, operand2, operator):
        sum1 = operand1 + operand2
        sum2 = operand1 - operand2
        sum3 = operand1 * operand2
        sum4 = operand1 / operand2

        if operator == "+":
            self.log.append(f"{operand1} + {operand2} = {sum1}")
            print(f"{operand1} + {operand2} = {sum1}")
            return sum1
        elif operator == "-":
            self.log.append(f"{operand1} - {operand2} = {sum2}")
            print(f"{operand1} - {operand2} = {sum2}")
            return sum2
        elif operator == "*":
            self.log.append(f"{operand1} * {operand2} = {sum3}")
            print(f"{operand1} * {operand2} = {sum3}")
            return sum3
        elif operator == "/":
            self.log.append(f"{operand1} / {operand2} = {sum4}")
            print(f"{operand1} / {operand2} = {sum4}")
            return sum4


    def get_log(self):
        print(self.log)

    def get_last_logged(self):
        print(self.log[-1])
    
    def clear_log(self):
        self.log *= 0

#def main():
#    calculator = Calculator()
#    calculator.calculate(1,2,'+')
#    calculator.calculate(2,2,'*')
#    calculator.calculate(16,2,'/')
#    print(calculator.get_log())
#    print(calculator.get_last_logged())

calculator1 = Calculator()

window = Tk()
window.title("Calculator")
frame = Frame(window)
frame.pack(fill=BOTH, expand=True)
frame.columnconfigure(1, weight = 1)
frame.rowconfigure(1, weight=1)
operand1 = float(5)
operand2 = float(2)
operator = str()
result = float(1)

operand1_input = Entry(frame, width=10, textvariable=operand1)
operand1_text = Label(frame, text="Operand 1")

operand2_input = Entry(frame, width=10, textvariable=operand2)
operand2_text = Label(frame, text="Operand 2")

operator_input = Entry(frame, width=5, textvariable=operator)
operator_text = Label(frame, text="Operator")

resultValue = Label(frame, textvariable=result)
result_text = Label(frame, text="Result")

calculateButton = Button(frame, text="Calculate", command=calculator1.calculate(operand1,operand2,operator))
clearlogButton = Button(frame, text="Clear Log", command=calculator1.clear_log)
quitButton = Button(frame, text="Quit", command=quit)
logtextbox = Text(frame, height=5, width=15)
logtextbox.config(state='disabled')

operand1_input.grid(row=0, column=2, padx=5, pady=5)
operand1_text.grid(row = 0, column=1, padx=5, pady=5, sticky=E)
operator_input.grid(row=1, column=2, padx=5, pady=5)
operator_text.grid(row=1, column=1, padx=5, pady=5, sticky=E)
operand2_input.grid(row=2, column=2, padx=5, pady=5)
operand2_text.grid(row=2, column=1, padx=5, pady=5, sticky=E)
resultValue.grid(row=3, column=2, padx=5,pady=5)
result_text.grid(row=3, column=1, padx=5, pady=5)
calculateButton.grid(row=4,column=0,columnspan=1,padx=1,pady=1,sticky=E)
clearlogButton.grid(row=4,column=1,columnspan=1,padx=1,pady=1, sticky=E)
quitButton.grid(row=4,column=2, columnspan=1,padx=5,pady=5)
logtextbox.grid(row=5,column=0,sticky=S)
operand1_input.focus()
window.mainloop()




