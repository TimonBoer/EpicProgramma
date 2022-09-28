import tkinter as tk
from tkinter import messagebox
import datetime
import win32file
import pywintypes
from tkcalendar import DateEntry
from data import border, borderW, BGtitle, frameRow3
import os
from tkinter import filedialog as fd

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