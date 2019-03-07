#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Copyright © 2019 Antoine COMBET

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from morpion import *
from tkinter import *

nCanvasHeight = 300
nCanvasWidth = 300
sCanvasBG = 'white'
nPlayer = 1
bWon = False

class GUIMor(Morpion):
    def __init__(self, cCanvas, nCanvasHeight, nCanvasWidth):
        Morpion.__init__(self)
        self.cCanvas=cCanvas
        self.nHeight = nCanvasHeight
        self.nWidth = nCanvasWidth
        
# override display function
    def disp(self):
        self.cCanvas.delete(ALL)
        for i in range(3):
            self.cCanvas.create_line((i*nCanvasWidth)//3 , 0, (i*nCanvasWidth)//3  , nCanvasHeight, width = 3)
            self.cCanvas.create_line(0, (i*nCanvasHeight)//3 , nCanvasWidth, (i*nCanvasHeight)//3 , width = 3)
        for c in range(3):
            for r in range(3):
                if self.grid[r][c] == 1:
                    self.cCanvas.create_line(((c*nCanvasWidth)//3) + 15 , ((r*nCanvasHeight)//3) + 15, (((c + 1)*nCanvasWidth)//3) - 15  , (((r + 1)*nCanvasHeight)//3) - 15, width = 3, fill='red')
                    self.cCanvas.create_line((((c + 1)*nCanvasWidth)//3) - 15  , ((r*nCanvasHeight)//3) + 15,((c*nCanvasWidth)//3) + 15 , (((r + 1)*nCanvasHeight)//3) - 15, width = 3, fill='red')
                elif self.grid[r][c] == -1:
                    self.cCanvas.create_oval(((c*nCanvasWidth)//3) + 15 , ((r*nCanvasHeight)//3) + 15, (((c + 1)*nCanvasWidth)//3) - 15  , (((r + 1)*nCanvasHeight)//3) - 15, width = 3, outline='blue')
        
        
def replay(mGame):
    global nPlayer, bWon
    mGame.reinit()
    nPlayer = 1
    bWon = False
    show()

def show():
    if not bWon:
        mGame.disp()
    else:
        return None

def onCanvasClick(event):
    global nPlayer, bWon
    mGame.cCanvas.delete(ALL)
    show()
    if bWon : return None
    nCol = (3 * event.x)//nCanvasWidth
    nRow = (3 * event.y)//nCanvasHeight
    if mGame.grid[nRow][nCol] == 0:
        mGame.grid[nRow][nCol] = nPlayer
        nPlayer = - nPlayer
    nWinner=mGame.check_win()
    if nWinner in [-1, 1, 3]:
        bWon = True
        if nWinner == -1:
            mGame.cCanvas.delete(ALL)
            mGame.cCanvas.create_text(150, 150, text="Player 2 Won !")
        elif nWinner == 1:
            mGame.cCanvas.delete(ALL)
            mGame.cCanvas.create_text(150, 150, text="Player 1 Won !")
            pass
        elif nWinner == 3:
            mGame.cCanvas.delete(ALL)
            mGame.cCanvas.create_text(150, 150, text="Match Nul!")
    show()

if __name__ == "__main__":
    wApp = Tk()
    cGrid = Canvas(wApp, bg=sCanvasBG, height=nCanvasHeight, width=nCanvasWidth)
    cGrid.grid(row=0, column=0, columnspan=2 ,rowspan=2, padx = 3, pady = 3)
    mGame = GUIMor(cGrid, nCanvasHeight, nCanvasWidth)
    btQuit = Button(wApp, text="Quiter", command=wApp.destroy)
    btQuit.grid(row=2, column=1, padx=3, pady=3, sticky='nswe')
    btQuit = Button(wApp, text="Rejouer", command=lambda: replay(mGame))
    btQuit.grid(row=2, column=0, padx=3, pady=3, sticky='nswe')
    cGrid.bind('<Button>', onCanvasClick)
    wApp.title("Morpion")
    wApp.resizable(False, False)
    show()
    wApp.mainloop()
