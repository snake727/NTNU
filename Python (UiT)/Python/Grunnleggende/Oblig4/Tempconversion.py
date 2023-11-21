from tkinter import *

cTemp = None
fTemp = None

def tempConvert():
    global cTemp
    global fTemp

    try:
        num = cTemp.get()
        fTemp.set((num * 9.0 / 5) + 32)
    except:
        pass

window = Tk()
window.title("Temperature converter")
frame = Frame(window)
frame.pack(fill=BOTH, expand=True)
frame.columnconfigure(1, weight = 1)
frame.rowconfigure(1, weight=1)
cTemp = DoubleVar()
fTemp = DoubleVar()

celsiusInput = Entry(frame, width=10, textvariable=cTemp)
celsiusUnit = Label(frame, text="°C")
isEqual = Label(frame, text="is equal to")
farenheitValue = Label(frame, textvariable=fTemp)
farenheitUnit = Label(frame, text="°F")
conversionButton = Button(frame, text="Convert", command=tempConvert)

celsiusInput.grid(row=0, column=1, padx=10, pady=10)
celsiusUnit.grid(row=0, column=2, padx=10, pady=10, sticky=W)
isEqual.grid(row=1, column=0, padx=10, pady=10, sticky=E)
farenheitValue.grid(row=1, column=1, padx=10, pady=10)
farenheitUnit.grid(row=1, column=2, padx=10, pady=10, sticky=W)
conversionButton.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky=E)

celsiusInput.focus()
window.mainloop()