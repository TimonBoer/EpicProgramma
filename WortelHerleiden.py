import tkinter as tk
import math
from data import border, borderW, BGtitle, frameRow2

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

