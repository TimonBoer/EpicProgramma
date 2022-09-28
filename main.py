import math
import os
import datetime
import tkinter as tk
import win32file
import pywintypes
from tkinter import messagebox
from tkinter import filedialog as fd
from tkcalendar import Calendar, DateEntry
from data import border, borderW, BGtitle, window, frameRow2, frameRow3



from PeriodiekSysteem import Nr, Symb, Naam, MolM, Dicht, SP, KP, zoek, frmPeriodiek
frmPeriodiek.pack(pady=10)

from MolaireMassa import frameMolM, entFormule, berekenMolM
frameMolM.grid(row=0, column=1, padx=5, sticky='n')

from MolaireMassa import frmCommas
frmCommas.grid(row=0, column=2, sticky='n',padx=5)

from WortelHerleiden import frmWortel, entGetal, entGetal2, wortel
frmWortel.grid(row=0, column=0, sticky='n', padx=5)

from ReactieVergelijking import frmReacTot, entReac, CalcReac
frmReacTot.grid(row=0, column=0, padx=5)

from TwentyFourGame import frm24Game, TwfGameEnt1, TwfGameEnt2, TwfGameEnt3, TwfGameEnt4, twfGame
frm24Game.grid(row=0, column=1, padx=5)

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

frameRow2.pack(pady=5)


#Reactievergelijking oplossen




#24 Game oplosser




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