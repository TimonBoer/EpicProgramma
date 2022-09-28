import tkinter as tk
from data import border, borderW, BGtitle, frameRow3, cijfers, matrix
from tkinter import messagebox
from PeriodiekSysteem import search

def ClrReac():
    entReac.delete(0, tk.END)


def CalcReac(reactie):
    reacMol = [0, '']
    reac = [[], []]
    reacLoR = 0
    for letter in reactie:
        if letter in cijfers:
            if reacMol[1] == '':
                reacMol[0] = int(str(reacMol[0]) + str(letter))
            else:
                reacMol[1] = reacMol[1] + str(letter)

        elif letter.isalpha():
            reacMol[1] = reacMol[1] + letter

        elif letter == '+':
            if reacMol[0] == 0:
                reacMol[0] = 1
            reac[reacLoR].append(reacMol)
            reacMol = [0, '']

        elif letter == '-' or letter == '=':
            if reacMol[0] == 0:
                reacMol[0] = 1
            reac[reacLoR].append(reacMol)
            reacMol = [0, '']
            reacLoR = 1

    if reacMol[0] == 0:
        reacMol[0] = 1
    reac[reacLoR].append(reacMol)
    print(reac[0])
    print(reac[1])



def FormSplit(form):
    formule = []
    symbool = ''
    for nummer, letter in enumerate(form):
        if letter != ' ':
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
    list, x = FormCheck(formule)
    if list == None:
        return
    dict = {}
    for i in range(0, len(list), 2):
        if list[i] in dict:
            dict[list[i]] = dict[list[i]] + list[i+1]
        else:
            dict[list[i]] = list[i+1]
    return dict, x


def FormCheckLp(formule, item, formuleStr):
    if item < len(formule):
        row = search(1, formule[item], 0)
        if row == None:
            messagebox.showerror('Geen geldige formule', '\'' + str(formule[item]) + '\'' + ' bestaat niet')
            formule = []
            return
        else:
            formule[item] = matrix[row][1]
            if formule[item + 1] == 1:
                formuleStr = formuleStr + formule[item]
            else:
                formuleStr = formuleStr + formule[item] + str(formule[item + 1])
            return FormCheckLp(formule, item + 2, formuleStr)
    else:
        return formule, formuleStr


def FormCheck(formule):
    if formule[0] == '':
        del formule[0:1]
        FormCheck(formule)
    else:
        return FormCheckLp(formule, 0, '')


frmReacTot = tk.Frame(master=frameRow3, relief=border, borderwidth=borderW)

lblReacTitle = tk.Label(master=frmReacTot, text='Reactievergelijking oplossen', background=BGtitle)

entReac = tk.Entry(master=frmReacTot)

lblReacTitle.pack(fill='x')

entReac.pack(pady=5, fill='x')

frmReacBut = tk.Frame(master=frmReacTot)

ReacButClr = tk.Button(master=frmReacBut, text='Clear', width=12, command= lambda: ClrReac())
ReacButCalc = tk.Button(master=frmReacBut, text='Los op', width=12, command= lambda: CalcReac(entReac.get()))

ReacButClr.grid(row=0, column=0, sticky='ew')
ReacButCalc.grid(row=0, column=1, sticky='ew')

frmReacBut.pack()

