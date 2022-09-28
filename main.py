from data import window, frameRow2, frameRow3, frameRow4

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

from GtaVoltHack import VLFrame, VLCinp1, VLCinp2, VLCinp3, VLFinp1, VLFinp2, VLFinp3, VLtargEnt, VLhack
VLFrame.grid(row=0, column=2)

from FileDateChanger import FTFrame
FTFrame.grid(row=0, column=3)

from nCrnPr import frmCP, entCPn, entCPr, CPber
frmCP.grid(row=0, column=0, padx=5)

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
frameRow3.pack(pady=5)
frameRow4.pack(pady=5)

window.bind('<Return>', enter)

window.mainloop()