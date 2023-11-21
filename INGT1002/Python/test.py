import numpy as np

# definer diff-ligningen som skal løses
def f(x,y):
    return 2 * x * y

# inputs: antall steg n, steglengde h, initialverdi x0, initialverdi y0
def forbedret_euler(n, h, x0, y0):

    x = np.linspace() # array med x-verdier
    y = np.zeros() # array for å lagre y-verdier
    
    # initialisering
    y[0] = y0
    
    for i in range(n):
        y_pred = y[i] + h * f(x[i], y[i])
        y[i+1] = y[i] + h/2 * ( f(x[i], y[i]) + f(x[i+1], y_pred) )
       
    return np.round(y, 4)

svar_1 = forbedret_euler()
svar_2 = forbedret_euler()