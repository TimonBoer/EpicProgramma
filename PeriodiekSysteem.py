import tkinter as tk
from data import border, borderW, BGtitle, matrix

def clear():
    Nr.delete(0, tk.END)
    Symb.delete(0, tk.END)
    Naam.delete(0, tk.END)
    MolM.delete(0, tk.END)
    Dicht.delete(0, tk.END)
    SP.delete(0, tk.END)
    KP.delete(0, tk.END)


def fill(row):
    if not row == None:
        clear()
        if not row > 121:
            Nr.insert(0, matrix[row][0])
        Symb.insert(0, matrix[row][1])
        Naam.insert(0, matrix[row][2])
        MolM.insert(0, matrix[row][3])
        Dicht.insert(0, matrix[row][4])
        SP.insert(0, matrix[row][5])
        KP.insert(0, matrix[row][6])


def search(column, zoekwoord, nummer):
    if isinstance(zoekwoord, int) or isinstance(zoekwoord, float):
        nummer = 0
        for row, text in enumerate(matrix):
            if not isinstance(matrix[row][column], str):
                if float(abs(matrix[row][column] - zoekwoord)) < float(abs(matrix[nummer][column] - zoekwoord)):
                    nummer = row
        row = nummer
        return row
    else:
        for row, text in enumerate(matrix):
            if matrix[row][column].lower() == zoekwoord.lower():
                return row


def zoek():
    if Nr.get() != '':
        try:
            fill(int(Nr.get()) - 1)
        except:
            return
    elif Symb.get() != '':
        fill(search(1, Symb.get(), 0))
    elif Naam.get() != '':
        fill(search(2, Naam.get(), 0))
    elif MolM.get() != '':
        try:
            fill(search(3, float(MolM.get()), 0))
        except:
            return
    elif Dicht.get() != '':
        try:
            fill(search(4, float(Dicht.get()), 0))
        except:
            return
    elif SP.get() != '':
        try:
            fill(search(5, float(SP.get()), 0))
        except:
            return
    elif KP.get() != '':
        try:
            fill(search(6, float(KP.get()), 0))
        except:
            return


frmPeriodiek = tk.Frame(relief=border, borderwidth=borderW)

PerTitle = tk.Label(text='Periodiek Systeem', background=BGtitle,master=frmPeriodiek)
PerTitle.pack(fill='x')

framePerio = tk.Frame(master=frmPeriodiek)
framePerio.pack()

frame = tk.Frame(master=framePerio)
frame.pack()

velden = ['Nummer', 'Symbool', 'Naam', 'Molaire massa\n(g/mol)', 'Dichteid\n(g/cm3)', 'Smeltpunt\n(℃)', 'Kookpunt\n(℃)']
for item, text in enumerate(velden):
    label = tk.Label(master=frame, text=text)
    label.grid(row=0, column=item, sticky='s')

Nr = tk.Entry(master=frame)
Symb = tk.Entry(master=frame)
Naam = tk.Entry(master=frame)
MolM = tk.Entry(master=frame)
Dicht = tk.Entry(master=frame)
SP = tk.Entry(master=frame)
KP = tk.Entry(master=frame)

column = 0
Nr.grid(row=1, column=column)
column += 1
Symb.grid(row=1, column=column)
column += 1
Naam.grid(row=1, column=column)
column += 1
MolM.grid(row=1, column=column)
column += 1
Dicht.grid(row=1, column=column)
column += 1
SP.grid(row=1, column=column)
column += 1
KP.grid(row=1, column=column)

frameB = tk.Frame(master=framePerio)
frameB.pack(pady=5)

searchB = tk.Button(master=frameB, text='Zoek', command=lambda: zoek(), width=12)
clearB = tk.Button(master=frameB, text='Clear', command=lambda: clear(), width=12)

searchB.grid(row=0, column=1, padx=5)
clearB.grid(row=0, column=0, padx=5)


