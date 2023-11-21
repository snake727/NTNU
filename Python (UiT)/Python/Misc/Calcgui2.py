from tkinter import *

operand1 = None
operand2 = None
result = None
log1 = []

def calculate():
    global operand1
    global operand2
    global result
    global log1

    log1 = []
    op1 = operand1.get()
    op2 = operand2.get()
    op = operator.get()
    sum1 = op1 + op2
    sum2 = op1 - op2
    sum3 = op1 * op2
    sum4 = op1 / op2

    try:
        if op == "+":
            log1.append(f"{op1} + {op2} = {sum1}")
            print(f"{op1} + {op2} = {sum1}")
            result.set(sum1)
        elif op == "-":
            log1.append(f"{op1} - {op2} = {sum2}")
            print(f"{op1} - {op2} = {sum2}")
            result.set(sum2)
        elif op == "*":
            log1.append(f"{op1} * {op2} = {sum3}")
            print(f"{op1} * {op2} = {sum3}")
            result.set(sum3)
        elif op == "/":
            log1.append(f"{op1} / {op2} = {sum4}")
            print(f"{op1} / {op2} = {sum4}")
            result.set(sum4)
    except:
        pass

def get_log():
    return log1

def get_last_logged():
    return log1[-1]

def clear_log():
    logtextbox.delete(2.0, 'end')

window = Tk()
window.title("Calculator")
frame = Frame(window)
frame.pack(fill=BOTH, expand=True)
frame.columnconfigure(1, weight = 1)
frame.rowconfigure(1, weight=1)
operand1 = DoubleVar()
operand2 = DoubleVar()
operator = StringVar()
result = DoubleVar()

operand1_input = Entry(frame, width=10, textvariable=operand1)
operand1_text = Label(frame, text="Operand 1")

operand2_input = Entry(frame, width=10, textvariable=operand2)
operand2_text = Label(frame, text="Operand 2")

operator_input = Entry(frame, width=5, textvariable=operator)
operator_text = Label(frame, text="Operator")

resultValue = Label(frame, textvariable=result)
result_text = Label(frame, text="Result")

calculateButton = Button(frame, text="Calculate", command=calculate)
clearlogButton = Button(frame, text="Clear Log", command=clear_log)
quitButton = Button(frame, text="Quit", command=quit)
logtextbox = Text(frame, height=5, width=10)
logtextbox.insert('end', "Log:")
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