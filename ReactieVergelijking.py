import tkinter as tk
from data import border, borderW, BGtitle, frameRow3, cijfers, matrix
from tkinter import messagebox
from PeriodiekSysteem import search

def ClrReac():
    entReac.delete(0, tk.END)


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

    if TelAtm(reac) != 'Cringe':
        gelukt = loop(0)
        if not gelukt:
            messagebox.showerror('Sorry man', 'Ik vond het te lang duren, het is niet gelukt')
        print(reac)
        print('')
        entReac.delete(0, tk.END)
        entReac.insert(0, reactostr(reac))


def loop(total):
    total += 1
    if total < 50:
        changes = {}
        global reac
        count = TelAtm(reac)
        for atoom in count[0]:
            delta = int(count[0][atoom] - count[1][atoom])
            if delta != 0:
                if delta < 0:
                    moleculen = lookup(reac, atoom, 0)
                elif delta > 0:
                    moleculen = lookup(reac, atoom, 1)
                delta = abs(delta)
                for molecuul in moleculen:
                    molecstr = str(molecuul[0]) + str(molecuul[1])
                    molecdict = reac[molecuul[0]][molecuul[1]]

                    if delta % reac[molecuul[0]][molecuul[1]][1][atoom] == 0:
                        change = [int(delta / molecdict[1][atoom]), 1]
                    else:
                        change = [delta, molecdict[1][atoom]]

                    if molecstr in changes:
                        listed = False
                        for i, ListedChange in enumerate(changes[molecstr]):
                            if ListedChange[0] == change:
                                changes[molecstr][i][1] -= 1
                                listed = True
                        if not listed:
                            changes[molecstr].append([change, len(molecdict[1]) - 1])
                    else:
                        changes[molecstr] = [[change, len(molecdict[1]) - 1]]

        print(changes)
        if len(changes) > 0:
            changeslist = []
            for x in changes:
                for y in changes[x]:
                    y.append(x)
                    changeslist.append(y)
            changeslist = sorted(changeslist, key=lambda item: item[1])
            print(changeslist)

            change = changeslist[0]
            for numside, side in enumerate(reac):
                for nummolec, molec in enumerate(side):
                    reac[numside][nummolec][0] = reac[numside][nummolec][0] * change[0][1]
            reac[int(change[2][0])][int(change[2][1:])][0] += change[0][0]
            return loop(total)
        return True
    else:
        return False


def lookup(reac, search, side):
    y = []
    for i, x in enumerate(reac[side]):
        if search in x[1]:
            y.append([side, i])
    return y


def TelAtm(reac):
    print(reactostr(reac))
    count = [{}, {}]

    i = 0
    x = reac[i]
    for y in x:
        for z in y[1]:
            if z in count[i]:
                count[i][z] += int(y[1][z]) * int(y[0])
            else:
                count[i][z] = int(y[1][z]) * int(y[0])

    i = 1
    x = reac[i]
    for y in x:
        for z in y[1]:
            if z not in count[0]:
                messagebox.showerror('Slecht', f"'{z}' Komt niet aan beide kanten voor")
                print(('cringe', count))
                return 'Cringe'
            if z in count[i]:
                count[i][z] += int(y[1][z]) * int(y[0])
            else:
                count[i][z] = int(y[1][z]) * int(y[0])

    for x in count[0]:
        if x not in count[1]:
            messagebox.showerror('Slecht', f"'{x}' Komt niet aan beide kanten voor")
            print(('cringe', count))
            return 'Cringe'
    print(count)
    return count


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