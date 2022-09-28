import tkinter as tk
from tkinter import messagebox
from data import border, borderW, BGtitle, frameRow4
import math

def CPber():
    cp = variable.get()
    if cp == 'nCr/nPr':
        messagebox.showerror('Noob', 'Vul nCr/nPr in')
        return
    try:
        n = int(entCPn.get())
        r = int(entCPr.get())
    except:
        messagebox.showerror('Doe het goed', 'n of r is fout ingevoerd')
        return
    if cp == 'nCr':
        ans = math.factorial(n)/(math.factorial(n-r)*math.factorial(r))
    else:
        ans = math.factorial(n) / math.factorial(n - r)
    entCPans.delete(0, tk.END)
    entCPans.insert(0, str(int(ans)))


def CPclr():
    global variable
    variable.set('nCr/nPr')
    entCPn.delete(0, tk.END)
    entCPr.delete(0, tk.END)
    entCPans.delete(0, tk.END)



frmCP = tk.Frame(master=frameRow4, relief=border, borderwidth=borderW)

lblCP = tk.Label(master=frmCP, text='nCr/nPr', background=BGtitle)

frmCPEnt = tk.Frame(master=frmCP)

width = 10

entCPn = tk.Entry(master=frmCPEnt, width=width)
entCPr = tk.Entry(master=frmCPEnt, width=width)

variable = tk.StringVar(frmCPEnt)
variable.set('nCr/nPr')
dropCP = tk.OptionMenu(frmCPEnt, variable, 'nCr', 'nPr')

entCPn.grid(row=1, column=0, sticky='ew')
dropCP.grid(row=1, column=1)
entCPr.grid(row=1, column=2, sticky='ew')

btnCPber = tk.Button(master=frmCPEnt, text='Bereken', width=width, command= lambda: CPber())
entCPans = tk.Entry(master=frmCPEnt, width=width)
btnCPclr = tk.Button(master=frmCPEnt, text='Clear', width=width, command= lambda: CPclr())

btnCPber.grid(row=2, column=0, pady=5)
entCPans.grid(row=2, column=1, pady=5, sticky='ew')
btnCPclr.grid(row=2, column=2, pady=5)

lblCP.pack(fill='x')
frmCPEnt.pack()