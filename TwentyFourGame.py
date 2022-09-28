import tkinter as tk
from data import border, borderW, BGtitle, frameRow3

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