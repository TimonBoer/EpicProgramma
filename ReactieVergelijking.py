import tkinter as tk
import numpy as np
from data import border, borderW, BGtitle, frameRow3, cijfers, matrix
from tkinter import messagebox
from PeriodiekSysteem import search

def ClrReac():
    entReac.delete(0, tk.END)
    ReacLbx.delete(0, tk.END)
    ReacLbx['height'] = 0
    ReacLbx.grid_forget()


def CalcReac(reactie):
    global reac
    reacMol = [1, '']
    reac = [[], []]
    reacLoR = 0
    for letter in reactie:
        if letter in cijfers:
            if reacMol[1] != '':
                reacMol[1] = reacMol[1] + str(letter)

        elif letter.isalpha():
            reacMol[1] = reacMol[1] + letter

        elif letter == '+':
            reac[reacLoR].append(reacMol)
            reacMol = [1, '']

        elif letter == '-' or letter == '=':
            reac[reacLoR].append(reacMol)
            reacMol = [1, '']
            reacLoR = 1

    reac[reacLoR].append(reacMol)


    for i, x in enumerate(reac):
        for mi, mx in enumerate(x):
            form = FormSplit(mx[1])
            if form == None:
                return
            reac[i][mi].append(form[1])
            reac[i][mi][1] = form[0]

    entReac.delete(0, tk.END)
    entReac.insert(0, reactostr(reac))

    reacnum = checkreac(reac)

    maxdif = 0.001
    if reacnum != 'cringe':
        newreacnum = 'cringe'
        reacflt = []
        for x in reacnum:
            if abs(round(x) - x) > maxdif:
                reacflt.append(x)

        for product in range(1, 100):
            goed = True
            for x in reacflt:
                y = x * product
                if abs(round(y) - y) > maxdif:
                    goed = False

            if goed:
                newreacnum = []
                for x in reacnum:
                    newreacnum.append(int(round(x * product)))
                break

        newi = 0
        atomen = {}
        for side, x in enumerate(reac):
            for i, molec in enumerate(x):
                reac[side][i][0] = newreacnum[newi]
                if side == 0:
                    for atoom in molec[1]:
                        if atoom in atomen:
                            atomen[atoom] += molec[1][atoom] * newreacnum[newi]
                        else:
                            atomen[atoom] = molec[1][atoom] * newreacnum[newi]
                newi += 1

        print(atomen)
        entReac.delete(0, tk.END)
        entReac.insert(0, reactostr(reac))

        ReacLbx.delete(0, tk.END)
        ReacLbx['height'] = len(atomen)
        for i, atoom in enumerate(atomen):
            ReacLbx.insert(i, f"{atoom} = {atomen[atoom]}")
        ReacLbx.grid(row=2, sticky='ew')


def checkreac(reac):
    count = [[], []]
    for side, x in enumerate(reac):
        for y in x:
            for z in y[1]:
                if z not in count[side]:
                    if side == 1:
                        if z not in count[0]:
                            messagebox.showerror('Slecht', f"'{z}' Komt niet aan beide kanten voor")
                            return 'cringe'
                    count[side].append(z)
    for x in count[0]:
        if x not in count[1]:
            messagebox.showerror('Slecht', f"'{x}' Komt niet aan beide kanten voor")
            return 'cringe'

    A = []
    B = []
    for atoom in count[0]:
        equation = []
        for side, x in enumerate(reac):
            for y in x:
                if atoom in y[1]:
                    equation.append(y[1][atoom]*((side*2-1)*-1))
                else:
                    equation.append(0)
        A.append(equation[1:])
        B.append(equation[0]*-1)


    A = np.array(A)
    B = np.array(B)

    x = np.linalg.lstsq(A, B, rcond=None)
    ans = [1]
    for y in x[0]:
        ans.append(float(y))
    return ans


def reactostr(reac):
    reacstr = ''
    for i, x in enumerate(reac):
        for mi, mx in enumerate(x):
            if mx[0] == 1:
                reacstr += mx[2]
            else:
                reacstr += str(mx[0]) + mx[2]

            if mi != len(x) - 1:
                reacstr += ' + '
        if i == 0:
            reacstr += ' -> '
    return reacstr


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
        return None
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
            return None, None
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
        return FormCheck(formule)
    else:
        return FormCheckLp(formule, 0, '')


frmReacTot = tk.Frame(master=frameRow3, relief=border, borderwidth=borderW)

lblReacTitle = tk.Label(master=frmReacTot, text='Reactievergelijking oplossen', background=BGtitle, width=38)

entReac = tk.Entry(master=frmReacTot, justify=tk.CENTER)

lblReacTitle.grid(row=0, sticky='ew')

entReac.grid(row=1, pady=5, sticky='ew')


ReacLbx = tk.Listbox(master=frmReacTot, height=1, justify=tk.CENTER)


frmReacBut = tk.Frame(master=frmReacTot)

ReacButClr = tk.Button(master=frmReacBut, text='Clear', width=12, command= lambda: ClrReac())
ReacButCalc = tk.Button(master=frmReacBut, text='Los op', width=12, command= lambda: CalcReac(entReac.get()))

ReacButClr.grid(row=0, column=0, sticky='ew')
ReacButCalc.grid(row=0, column=1, sticky='ew')

frmReacBut.grid(row=3)