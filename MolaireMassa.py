import tkinter as tk
from tkinter import messagebox
from PeriodiekSysteem import search
from data import border, borderW, BGtitle, matrix, frameRow2

def ClrMolM():
    entMolM.delete(0, tk.END)
    entFormule.delete(0, tk.END)
    ClrLVMM()


def ClrLVMM():

    LVMMSymb.delete(0, tk.END)
    LVMMSymb['height'] = 1
    LVMMSymb.grid_forget()

    LVMMNr.delete(0, tk.END)
    LVMMNr['height'] = 1
    LVMMNr.grid_forget()

    LVMMMolM.delete(0, tk.END)
    LVMMMolM['height'] = 1
    LVMMMolM.grid_forget()

    LVMMTMolM.delete(0, tk.END)
    LVMMTMolM['height'] = 1
    LVMMTMolM.grid_forget()


def CheckLp(formule, item, MolMas, formuleStr):
    if item < len(formule):
        row = search(1, formule[item], 0)
        if row == None:
            messagebox.showerror('Geen geldige formule', '\'' + str(formule[item]) + '\'' + ' bestaat niet')
            formule = []
            ClrLVMM()
            return
        else:
            formule[item] = matrix[row][1]
            if formule[item + 1] == 1:
                formuleStr = formuleStr + formule[item]
            else:
                formuleStr = formuleStr + formule[item] + str(formule[item + 1])
            LVMMSymb['height'] += 1
            LVMMSymb.insert(item+1, matrix[row][1])
            LVMMNr['height'] += 1
            LVMMNr.insert(item+1, formule[item+1])
            LVMMMolM['height'] += 1
            LVMMMolM.insert(item+1, round(matrix[row][3], LblCom['text']))
            LVMMTMolM['height'] += 1
            LVMMTMolM.insert(item+1, round(formule[item+1]*matrix[row][3], LblCom['text']))
            MolMas = MolMas + matrix[row][3] * formule[item + 1]
            CheckLp(formule, item + 2, MolMas, formuleStr)
    else:
        entFormule.delete(0, tk.END)
        entFormule.insert(0, formuleStr)

        entMolM.delete(0, tk.END)
        entMolM.insert(0, round(MolMas, LblCom['text']))

        LVMMSymb.grid(row=0, column=0)
        LVMMNr.grid(row=0, column=1)
        LVMMMolM.grid(row=0, column=2)
        LVMMTMolM.grid(row=0, column=3)


def MolMFormCheck(formule):
    if formule[0] == '':
        del formule[0:1]
        MolMFormCheck(formule)
    else:
        CheckLp(formule, 0, 0, '')


def berekenMolM(formule, MolMas):
    ClrLVMM()
    entMolM.delete(0, tk.END)
    if not entFormule.get() == '':
        LVMMSymb.insert(0, 'Atoom')
        LVMMNr.insert(0, 'Exp')
        LVMMMolM.insert(0, 'MolM')
        LVMMTMolM.insert(0, 'MolM*Exp')
        formule = []
        symbool = ''
        for nummer, letter in enumerate(entFormule.get()):
            if letter.isupper():
                if symbool == '':
                    symbool = letter
                else:
                    try:
                        formule.append(int(symbool))
                    except:
                        formule.append(symbool)
                        formule.append(1)
                    symbool = letter
            else:
                try:
                    letter = int(letter)
                    if isinstance(symbool, int):
                        symbool = int(str(symbool) + str(letter))
                    else:
                        formule.append(symbool)
                        symbool = letter
                except:
                    if isinstance(symbool, str):
                        symbool = str(symbool) + str(letter)
                    else:
                        formule.append(symbool)
                        symbool = letter
        if isinstance(symbool, int):
            formule.append(symbool)
        else:
            formule.append(symbool)
            formule.append(1)
        MolMFormCheck(formule)


frameMolM = tk.Frame(master=frameRow2, relief=border, borderwidth=borderW)


lblFormule = tk.Label(master=frameMolM, text='Formule:')
entFormule = tk.Entry(master=frameMolM, width=48)
titleMolM = tk.Label(master=frameMolM, text='Molare massa berekenen',background=BGtitle)
titleWhite = tk.Label(master=frameMolM, background=BGtitle)

frameLV = tk.Frame(master=frameMolM)

LVMMSymb = tk.Listbox(master=frameLV, width=7, height=0)
LVMMNr = tk.Listbox(master=frameLV, width=7, height=0)
LVMMMolM = tk.Listbox(master=frameLV, width=16, height=0)
LVMMTMolM = tk.Listbox(master=frameLV, width=16, height=0)

entMolM = tk.Entry(master=frameLV, width=15)
lblMolM = tk.Label(master=frameLV, text='Totaal (g/mol):', width=14, anchor='e')
MolMGray1 = tk.Label(master=frameLV, width=5)
MolMGray2 = tk.Label(master=frameLV, width=5)

titleWhite.grid(row=0, column=0, sticky='ew')
titleMolM.grid(row=0,column=1, sticky='ew')
frameLV.grid(row=2, column=1)
entMolM.grid(row=1, column=3)
lblMolM.grid(row=1, column=2)
MolMGray1.grid(row=1, column=0, sticky='ew')
MolMGray2.grid(row=1, column=1, sticky='ew')

frmBtnMolM = tk.Frame(master=frameMolM)

buttonMolM = tk.Button(master=frmBtnMolM, text='Bereken', width=15, command=lambda: berekenMolM(0, 0))
buttonMolMClr = tk.Button(master=frmBtnMolM, text='Clear', width=15, command=lambda: ClrMolM())

lblFormule.grid(row=1, column=0, pady=5, sticky='e')
entFormule.grid(row=1, column=1)

frmBtnMolM.grid(row=3, column=1, pady=5)

buttonMolM.grid(row=0, column=1, padx=5)
buttonMolMClr.grid(row=0, column=0, padx=5)

def plus():
    LblCom['text'] = LblCom['text'] + 1
    berekenMolM(0, 0)


def min():
    if not LblCom['text'] == 1:
        LblCom['text'] = LblCom['text'] - 1
    berekenMolM(0, 0)


frmCommas = tk.Frame(master=frameRow2, relief=border, borderwidth=borderW)


frmComBtn = tk.Frame(master=frmCommas)

lblCommas = tk.Label(master=frmCommas, text='Decimalen',background=BGtitle)
BtnComPlus = tk.Button(master=frmComBtn, text='+', width=5, command=lambda: plus())
BtnComMin = tk.Button(master=frmComBtn, text='-', width=5, command=lambda: min())
LblCom = tk.Label(master=frmComBtn, text=3, width=5, background='white')

BtnComPlus.grid(row=0, column=2)
BtnComMin.grid(row=0, column=0)
LblCom.grid(row=0, column=1, sticky='ns')

lblCommas.pack(fill='x')
frmComBtn.pack()