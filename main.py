import math
import os
import datetime
import tkinter as tk
import win32file
import pywintypes
from tkinter import messagebox
from tkinter import filedialog as fd
from tkcalendar import Calendar, DateEntry
from data import border, borderW, BGtitle

cijfers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

window = tk.Tk()

from PeriodiekSysteem import Nr, Symb, Naam, MolM, Dicht, SP, KP, zoek, frmPeriodiek

def enter(key):
    if Nr.get() != '' or Symb.get() != '' or Naam.get() != '' or MolM.get() != '' or Dicht.get() != '' or SP.get() != '' or KP.get() != '':
        zoek()
    if entFormule.get() != '':
        berekenMolM(0, 0)
    if entGetal.get() != '' or entGetal2.get() != '':
        wortel()
    if entReac.get() != '':
        CalcReac(entReac.get())
    if TwfGameEnt1.get() != '' and TwfGameEnt2.get() != '' and TwfGameEnt3.get() != '' and TwfGameEnt4.get() != '':
        twfGame()
    if VLCinp1.get() != '' and VLCinp2.get() != '' and VLCinp3.get() != '' and VLFinp1.get() != '' and VLFinp2.get() != '' and VLFinp3.get() != '' and VLtargEnt.get() != '':
        VLhack()
    if entCPn.get() != '' and entCPr.get() != '':
        CPber()


#periodiek systeem
frmPeriodiek.pack(pady=10)


frameRow2 = tk.Frame(master=window)



#Molaire massa berekenen
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
frameMolM.grid(row=0, column=1, padx=5, sticky='n')

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



#Significantie kiezen
def plus():
    LblCom['text'] = LblCom['text'] + 1
    berekenMolM(0, 0)


def min():
    if not LblCom['text'] == 1:
        LblCom['text'] = LblCom['text'] - 1
    berekenMolM(0, 0)


frmCommas = tk.Frame(master=frameRow2, relief=border, borderwidth=borderW)
frmCommas.grid(row=0, column=2, sticky='n',padx=5)

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



#Wortel herleiden
def clrWortel():
    entMacht.delete(0, tk.END)
    entGetal.delete(0, tk.END)
    entCoef.delete(0, tk.END)
    entMacht2.delete(0, tk.END)
    entGetal2.delete(0, tk.END)
    lblAns.pack_forget()


def wortelDeherl():
    lblAns.pack_forget()

    if entCoef.get() == '':
        entCoef.insert(0, 1)
    if entMacht2.get() == '':
        entMacht2.insert(0, 2)

    try:
        entGetal.delete(0, tk.END)
        entMacht.delete(0, tk.END)

        entGetal.insert(0, int(int(entCoef.get()) ** int(entMacht2.get()) * int(entGetal2.get())))
        entMacht.insert(0, entMacht2.get())
    except:
        clrWortel()


def wortelHerl(getal, macht, aantal, factoren, deler):
    try:
        if entMacht.get() == '':
            entMacht.insert(0, 2)

        if isinstance(int(int(entMacht.get()) + int(entGetal.get())), int):

            getal=int(entGetal.get())
            macht=int(entMacht.get())
            deler = 2
            aantal=0
            factoren=[]
            while(getal % deler == 0):
                getal = getal / deler
                aantal += 1
                if aantal == macht:
                    factoren.append(deler)
                    aantal = 0

            while(deler <= int(math.sqrt(getal))):
                deler += 1
                aantal = 0
                while (getal % deler == 0):
                    getal = getal / deler
                    aantal += 1
                    if aantal == macht:
                        factoren.append(deler)
                        aantal = 0

            entCoef.delete(0, tk.END)
            entMacht2.delete(0, tk.END)
            entGetal2.delete(0, tk.END)
            entMacht.delete(0, tk.END)

            entMacht2.insert(0, macht)
            entMacht.insert(0, macht)

            entGetal2.insert(0, int(int(entGetal.get()) / math.prod(factoren) ** int(macht)))

            entCoef.insert(0, math.prod(factoren))

            if macht == 2:
                if entGetal2.get() == '1':
                    lblAns['text'] = entCoef.get()
                else:
                    if entCoef.get() == '1':
                        lblAns['text'] = '√' + entGetal2.get()
                    else:
                        lblAns['text'] = entCoef.get() + ' √' + entGetal2.get()
            else:
                if entGetal2.get() == '1':
                    lblAns['text'] = entCoef.get()
                else:
                    if entCoef.get() == '1':
                        lblAns['text'] = entMacht2.get() + '√' + entGetal2.get()
                    else:
                        lblAns['text'] = entCoef.get() + ' ' + entMacht2.get() + '√' + entGetal2.get()

            lblAns.pack()



    except:
        return


def wortel():
    if entGetal.get() != '':
        wortelHerl(entGetal.get(), entMacht.get(), 0, 0, 0)
    elif entGetal2.get() != '':
        wortelDeherl()


frmWortel = tk.Frame(master=frameRow2, relief=border, borderwidth=borderW)

wortelW = 10

tleWortel = tk.Label(master=frmWortel, text='Wortel herleiden', background=BGtitle)
tleWortel.pack(fill='x')

frmWortelinp = tk.Frame(master=frmWortel,background='gray90')

entMacht = tk.Entry(master=frmWortelinp, width=wortelW)
entGetal = tk.Entry(master=frmWortelinp, width=wortelW)
lblWortel = tk.Label(master=frmWortelinp, text='√', font=('verdana', 25), background='gray90')

entMacht.grid(row=1, column=1, sticky='n', padx=5, pady=5)
entGetal.grid(row=1, column=3, sticky='s', padx=5, pady=5)
lblWortel.grid(row=1, column=2)

frmWortelinp.pack(pady=5)


frmWortelPijltjes = tk.Frame(master=frmWortel)

lblPijltjes = tk.Label(master=frmWortelPijltjes, text='🠕🠗', font=('verdana', 20))
btnWCalc = tk.Button(master=frmWortelPijltjes, text='Bereken', width=12, command= lambda: wortel())
btnWClr = tk.Button(master=frmWortelPijltjes, text='Clear', width=12, command= lambda: clrWortel())

lblPijltjes.grid(row=0, column=1)
btnWCalc.grid(row=0, column=2)
btnWClr.grid(row=0, column=0)

frmWortelPijltjes.pack()

frmWortelout = tk.Frame(master=frmWortel, background='gray90')

entMacht2 = tk.Entry(master=frmWortelout, width=wortelW)
entGetal2 = tk.Entry(master=frmWortelout, width=wortelW)
entCoef = tk.Entry(master=frmWortelout, width=wortelW)
lblWortel2 = tk.Label(master=frmWortelout, text='√', font=('verdana', 25),background='gray90')

entMacht2.grid(row=1, column=1, sticky='n', padx=5, pady=5)
entGetal2.grid(row=1, column=3, sticky='s', padx=5, pady=5)
lblWortel2.grid(row=1, column=2)
entCoef.grid(row=1, column=0, padx=10)

frmWortelout.pack(pady=5)

lblAns = tk.Label(master=frmWortel, background='gray90')

frmWortel.grid(row=0, column=0, sticky='n', padx=5)




frameRow2.pack(pady=5)

frameRow3 = tk.Frame(master=window)



#Reactievergelijking oplossen
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

frmReacTot.grid(row=0, column=0, padx=5)



#24 Game oplosser
def twfGame():
    global twfnummers
    global volgnummers
    global volgacties
    global acties
    twfnummers = [int(TwfGameEnt1.get()), int(TwfGameEnt2.get()), int(TwfGameEnt3.get()), int(TwfGameEnt4.get())]
    acties = ['+', '-', '*', '/']
    plussen = 0
    twfopl = []
    TwfListBox.delete(0, tk.END)
    try:
        TwfListBox['height'] = int(TwfLbHeightEnt.get())
    except:
        TwfListBox['height'] = 10
        TwfLbHeightEnt.delete(0, tk.END)
        TwfLbHeightEnt.insert(0, 10)


    numvolgordes = []
    x = 1000
    while int(x) < 4322:
        x = str(int(x) + 1)
        if '1' in x and '2' in x and '3' in x and '4' in x:
            numvolgordes.append([int(x[0]) - 1, int(x[1]) - 1, int(x[2]) - 1, int(x[3]) - 1])

    actvolgordes = []
    for a in range(4):
        for b in range(4):
            for c in range(4):
                actvolgordes.append([a, b, c])

    for volgnummers in numvolgordes:
        for volgacties in actvolgordes:
            x = ''

            # ((a+b)+c)+d
            if doactie(doactie(doactie(num(0), num(1), 0), num(2), 1), num(3), 2) == 24:
                x = '((' + str(num(0)) + act(0) + str(num(1)) + ')' + act(1) + str(num(2)) + ')' + act(2) + str(num(3))
                if volgacties == [0, 0, 0]:
                    if plussen == 0:
                        plussen = 1
                        twfopl.append(x)
                elif x not in twfopl:
                    twfopl.append(x)

            # (a+b)+(c+d)
            if doactie(doactie(num(0), num(1), 0), doactie(num(2), num(3), 2), 1) == 24:
                x = '(' + str(num(0)) + act(0) + str(num(1)) + ')' + act(1) + '(' + str(num(2)) + act(2) + str(
                    num(3)) + ')'
                if x not in twfopl and volgacties != [0, 0, 0]:
                    twfopl.append(x)

            # (a+(b+c))+d
            if doactie(doactie(num(0), doactie(num(1), num(2), 1), 0), num(3), 2) == 24:
                x = '(' + str(num(0)) + act(0) + '(' + str(num(1)) + act(1) + str(num(2)) + '))' + act(2) + str(num(3))
                if x not in twfopl and volgacties != [0, 0, 0]:
                    twfopl.append(x)

            # a+(b+(c+d))
            if doactie(num(0), doactie(num(1), doactie(num(2), num(3), 2), 1), 0) == 24:
                x = str(num(0)) + act(0) + '(' + str(num(1)) + act(1) + '(' + str(num(2)) + act(2) + str(num(3)) + '))'
                if x not in twfopl and volgacties != [0, 0, 0]:
                    twfopl.append(x)

            # a+((b+c)+d)
            if doactie(num(0), doactie(doactie(num(1), num(2), 1), num(3), 2), 0) == 24:
                x = str(num(0)) + act(0) + '((' + str(num(1)) + act(1) + str(num(2)) + ')' + act(2) + str(num(3)) + ')'
                if x not in twfopl and volgacties != [0, 0, 0]:
                    twfopl.append(x)
    for x in twfopl:
        TwfListBox.insert(tk.END, x)
    TwfListBox.grid(row=1, column=0)
    TwfScrollbar.grid(row=1, column=1, sticky='ns')
    TwfLbHeigtFrm.grid(row=1, column=2, sticky='nesw')


def num(x):
    global twfnummers
    global volgnummers
    return twfnummers[volgnummers[x]]


def act(x):
    global acties
    global volgacties
    return acties[volgacties[x]]


def doactie(a, b, actie):
    global acties
    global volgacties
    actie = acties[volgacties[actie]]
    if actie == '+':
        return a + b
    if actie == '-':
        if a - b < 0:
            return 9999999
        else:
            return a - b
    if actie == '*':
        return a * b
    if actie == '/':
        try:
            return a / b
        except:
            return 9999999


def ClrTwf():
    TwfGameEnt1.delete(0, tk.END)
    TwfGameEnt2.delete(0, tk.END)
    TwfGameEnt3.delete(0, tk.END)
    TwfGameEnt4.delete(0, tk.END)
    TwfListBox.grid_forget()
    TwfScrollbar.grid_forget()
    TwfLbHeigtFrm.grid_forget()


def TwfPlus():
    TwfListBox['height'] = int(TwfLbHeightEnt.get()) + 1
    TwfLbHeightEnt.delete(0, tk.END)
    TwfLbHeightEnt.insert(0, TwfListBox['height'])


def TwfMin():
    if TwfListBox['height'] > 4:
        TwfListBox['height'] = int(TwfLbHeightEnt.get()) - 1
        TwfLbHeightEnt.delete(0, tk.END)
        TwfLbHeightEnt.insert(0, TwfListBox['height'])


frm24Game = tk.Frame(master=frameRow3, relief=border, borderwidth=borderW)

lbl24Game = tk.Label(master=frm24Game, text='24 game oplosser', background=BGtitle)
lbl24Game.pack(fill='x')

TwfGameInputFrm = tk.Frame(master=frm24Game)

TwfGameEntriesFrame = tk.Frame(master=TwfGameInputFrm)

TwfGameEnt1 = tk.Entry(master=TwfGameEntriesFrame, width=5)
TwfGameEnt2 = tk.Entry(master=TwfGameEntriesFrame, width=5)
TwfGameEnt3 = tk.Entry(master=TwfGameEntriesFrame, width=5)
TwfGameEnt4 = tk.Entry(master=TwfGameEntriesFrame, width=5)

TwfGameEnt1.grid(row=0, column=0)
TwfGameEnt2.grid(row=0, column=1)
TwfGameEnt3.grid(row=0, column=2)
TwfGameEnt4.grid(row=0, column=3)

TwfGameEntriesFrame.grid(row=0, column=0, padx=5)

TwfGameButClr = tk.Button(master=TwfGameInputFrm, text='Clear', command= lambda: ClrTwf())
TwfGameButInp = tk.Button(master=TwfGameInputFrm, text='Los op', command= lambda: twfGame())

TwfGameButClr.grid(row=0, column=1)
TwfGameButInp.grid(row=0, column=2)

TwfGameInputFrm.pack(pady=5)

TwfListBox = tk.Listbox(master=TwfGameInputFrm)
TwfScrollbar = tk.Scrollbar(master=TwfGameInputFrm)

TwfListBox.config(yscrollcommand = TwfScrollbar.set)
TwfScrollbar.config(command = TwfListBox.yview)

TwfLbHeigtFrm = tk.Frame(master=TwfGameInputFrm)
TwfLbHeightButPlus = tk.Button(master=TwfLbHeigtFrm, text = '+', command= lambda: TwfPlus())
TwfLbHeightButMin = tk.Button(master=TwfLbHeigtFrm, text = '-', command=lambda: TwfMin())
TwfLbHeightEnt = tk.Entry(master=TwfLbHeigtFrm, justify = 'center', width=5)

TwfLbHeightButPlus.pack(side=tk.TOP, fill=tk.X)
TwfLbHeightEnt.pack(side=tk.TOP, fill=tk.X)
TwfLbHeightButMin.pack(side=tk.TOP, fill=tk.X)

frm24Game.grid(row=0, column=1, padx=5)



#Gta voltlab hack
def VLhack():
    try:
        cijfers = [int(VLCinp1.get()), int(VLCinp2.get()), int(VLCinp3.get())]
        factoren = [int(VLFinp1.get()), int(VLFinp2.get()), int(VLFinp3.get())]
        target = int(VLtargEnt.get())
        VLlistbox.delete(0, tk.END)

        x = 123
        volgordes = []
        while x < 322:
            if '1' in str(x) and '2' in str(x) and '3' in str(x):
                volgordes.append([int(str(x)[0]) - 1, int(str(x)[1]) - 1, int(str(x)[2]) - 1])
            x += 1

        oplossingen = []
        for x in volgordes:
            if cijfers[0] * factoren[x[0]] + cijfers[1] * factoren[x[1]] + cijfers[2] * factoren[x[2]] == target:
                x = str(cijfers[0]) + '*' + str(factoren[x[0]]) + '   ' + str(cijfers[1]) + '*' + str(
                    factoren[x[1]]) + '   ' + str(cijfers[2]) + '*' + str(factoren[x[2]])
                if x not in oplossingen:
                    oplossingen.append(x)
                    VLlistbox.insert(tk.END, x)
        VLlistbox['height'] = len(oplossingen)
        VLlistbox.pack()
    except:
        return


def VLclr():
    VLCinp1.delete(0, tk.END)
    VLCinp2.delete(0, tk.END)
    VLCinp3.delete(0, tk.END)

    VLFinp1.delete(0, tk.END)
    VLFinp2.delete(0, tk.END)
    VLFinp3.delete(0, tk.END)

    VLtargEnt.delete(0, tk.END)

    VLlistbox.pack_forget()


VLFrame = tk.Frame(master=frameRow3, relief=border, borderwidth=borderW)

VLlbl = tk.Label(master=VLFrame, text='GTA VoltLab Hack', background=BGtitle)
VLlbl.pack(fill='x')

VLinpFrame = tk.Frame(master=VLFrame)

VLCijferLbl = tk.Label(master=VLinpFrame, text='Cijfers:')
VLmidLbl = tk.Label(master=VLinpFrame, width = 10)
VLFactorLbl = tk.Label(master=VLinpFrame, text='Factoren:')

VLCijferLbl.grid(row=0, column=0)
VLmidLbl.grid(row=0, column=1)
VLFactorLbl.grid(row=0, column=2)

w = 5
VLCinp1 = tk.Entry(master=VLinpFrame, width=w)
VLCinp2 = tk.Entry(master=VLinpFrame, width=w)
VLCinp3 = tk.Entry(master=VLinpFrame, width=w)

VLFinp1 = tk.Entry(master=VLinpFrame, width=w)
VLFinp2 = tk.Entry(master=VLinpFrame, width=w)
VLFinp3 = tk.Entry(master=VLinpFrame, width=w)

VLCinp1.grid(row=1, column=0, padx=5)
VLCinp2.grid(row=2, column=0, padx=5)
VLCinp3.grid(row=3, column=0, padx=5)

VLFinp1.grid(row=1, column=2, padx=5)
VLFinp2.grid(row=2, column=2, padx=5)
VLFinp3.grid(row=3, column=2, padx=5)

VLtargLbl = tk.Label(master=VLinpFrame, text='Target:')
VLtargEnt = tk.Entry(master=VLinpFrame, width=w)

VLtargLbl.grid(row=4, column=0, sticky='e')
VLtargEnt.grid(row=4, column=1)

VLinpFrame.pack()

VLbutFrm = tk.Frame(master=VLFrame)

VLbutClr = tk.Button(master=VLbutFrm, text='Clear', width=10, command=lambda: VLclr())
VLbutLosOp = tk.Button(master=VLbutFrm, text='Los op', width=10, command=lambda: VLhack())

VLbutClr.grid(row=0, column=0)
VLbutLosOp.grid(row=0, column=1)

VLbutFrm.pack(pady=5)

VLlistbox = tk.Listbox(master=VLFrame, justify='center')

VLFrame.grid(row=0, column=2)



#File date changer
def FTcfile():
    global FTpath
    FTpath = fd.askopenfilename()
    FTbutFile['text'] = os.path.split(FTpath)[1]


def FTcom():
    if os.path.isfile(FTpath):
        try:
            if FTTimeHEnt.get() == '':
                FTTimeHEnt.insert(0, '12')
            elif int(FTTimeHEnt.get()) > 23:
                FTTimeHEnt.delete(0, tk.END)
                FTTimeHEnt.insert(0, '23')
            elif int(FTTimeHEnt.get()) < 0:
                FTTimeHEnt.delete(0, tk.END)
                FTTimeHEnt.insert(0, '0')
            try:
                if FTTimeMEnt.get() == '':
                    FTTimeMEnt.insert(0, '0')
                elif int(FTTimeMEnt.get()) > 59:
                    FTTimeMEnt.delete(0, tk.END)
                    FTTimeMEnt.insert(0, '59')
                elif int(FTTimeMEnt.get()) < 0:
                    FTTimeMEnt.delete(0, tk.END)
                    FTTimeMEnt.insert(0, '0')
                try:
                    if FTTimeSEnt.get() == '':
                        FTTimeSEnt.insert(0, '0')
                    elif int(FTTimeSEnt.get()) > 59:
                        FTTimeSEnt.delete(0, tk.END)
                        FTTimeSEnt.insert(0, '59')
                    elif int(FTTimeSEnt.get()) < 0:
                        FTTimeSEnt.delete(0, tk.END)
                        FTTimeSEnt.insert(0, '0')
                except:
                    messagebox.showerror('Verkeerd ingevuld', 'De seconde is verkeerd ingevuld')
                    return
            except:
                messagebox.showerror('Verkeerd ingevuld', 'De minuut is verkeerd ingevuld')
                return
        except:
            messagebox.showerror('Verkeerd ingevuld', 'Het uur is verkeerd ingevuld')
            return
        date = datetime.datetime.combine(cal.get_date(), datetime.time(int(FTTimeHEnt.get()), int(FTTimeMEnt.get()), int(FTTimeSEnt.get())))
        print(int(date.timestamp()))
        changeFileCreateTime(FTpath, int(date.timestamp()))
        os.utime(FTpath, (date.timestamp(), date.timestamp()))
        messagebox.showinfo('Gelukt', f'De tijd van {os.path.split(FTpath)[1]} is veranderd naar {str(date)}')


def changeFileCreateTime(path, ctime):
    # path: your file path
    # ctime: Unix timestamp

    # open file and get the handle of file
    # API: http://timgolden.me.uk/pywin32-docs/win32file__CreateFile_meth.html
    handle = win32file.CreateFile(
        path,                          # file path
        win32file.GENERIC_WRITE,       # must opened with GENERIC_WRITE access
        0,
        None,
        win32file.OPEN_EXISTING,
        0,
        0
    )

    # create a PyTime object
    # API: http://timgolden.me.uk/pywin32-docs/pywintypes__Time_meth.html
    PyTime = pywintypes.Time(ctime)

    # reset the create time of file
    # API: http://timgolden.me.uk/pywin32-docs/win32file__SetFileTime_meth.html
    win32file.SetFileTime(
        handle,
        PyTime
    )


def FTclr():
    global FTpath
    FTpath = ''
    FTbutFile['text'] = 'Selecteer bestand'
    FTTimeHEnt.delete(0, tk.END)
    FTTimeMEnt.delete(0, tk.END)
    FTTimeSEnt.delete(0, tk.END)


FTFrame = tk.Frame(master=frameRow3, relief=border, borderwidth=borderW)

FTlbl = tk.Label(master=FTFrame, text='Bestand tijd veranderen', background=BGtitle)
FTlbl.pack(fill='x')

FTbutFile = tk.Button(master=FTFrame, text='Selecteer bestand', command=lambda: FTcfile())
FTbutFile.pack(pady=5)

cal = DateEntry(master=FTFrame, date_pattern='dd/mm/yyyy')
cal.pack(pady=5)

FTTimeFrame = tk.Frame(master=FTFrame)
FTTimeHEnt = tk.Entry(master=FTTimeFrame, width = 5)
FTTimeLbl1 = tk.Label(master=FTTimeFrame, text=':')
FTTimeMEnt = tk.Entry(master=FTTimeFrame, width = 5)
FTTimeLbl2 = tk.Label(master=FTTimeFrame, text=':')
FTTimeSEnt = tk.Entry(master=FTTimeFrame, width=5)

FTTimeHEnt.grid(row=0, column=0)
FTTimeLbl1.grid(row=0, column=1)
FTTimeMEnt.grid(row=0, column=2)
FTTimeLbl2.grid(row=0, column=3)
FTTimeSEnt.grid(row=0, column=4)

FTTimeFrame.pack()

FTbutFrm = tk.Frame(master=FTFrame)

FTbutEnter = tk.Button(master=FTbutFrm, text='Enter', width=7, command=lambda:FTcom())
FTbutClr = tk.Button(master=FTbutFrm, text='Clear', width=7, command=lambda:FTclr())

FTbutEnter.grid(row=0, column=0, sticky=tk.EW)
FTbutClr.grid(row=0, column=1, sticky=tk.EW)

FTbutFrm.pack(pady=5)

FTFrame.grid(row=0, column=3)



frameRow3.pack(pady=5)

frameRow4 = tk.Frame()



#nCr/nPr
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

frmCP.grid(row=0, column=0, padx=5)


frameRow4.pack(pady=5)

window.bind('<Return>', enter)

window.mainloop()