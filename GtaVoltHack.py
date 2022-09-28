import tkinter as tk
from data import border, borderW, BGtitle, frameRow3

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