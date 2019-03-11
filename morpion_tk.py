#!/usr/bin/python3
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
from morpion import Morpion
import tkinter as tk


# Constantes
nCanvasHeight = 300
nCanvasWidth = 300
sCanvasBG = 'white'
nPlayer = 1
bWon = False


# Classe héritant du morpion texte pour pouvoir réutiliser les parties logiques
class GUIMor(Morpion):
    def __init__(self, cCanvas):
        Morpion.__init__(self)
        #Pointeur vers le Canvas
        self.cCanvas=cCanvas
        
# Réécriture de la methode d'affichage
    def disp(self):
        self.cCanvas.delete(tk.ALL)
        # La grille
        for i in range(3):
            self.cCanvas.create_line((i*nCanvasWidth)//3 , 0,
                                     (i*nCanvasWidth)//3, nCanvasHeight,
                                     width = 3)
            self.cCanvas.create_line(0, (i*nCanvasHeight)//3 , nCanvasWidth,
                                     (i*nCanvasHeight)//3 , width = 3)
        # Le contenu des cases
        for c in range(3):
            for r in range(3):
                if self.grid[r][c] == 1: # Les "X"
                    self.cCanvas.create_line(((c*nCanvasWidth)//3) + 15,
                                             ((r*nCanvasHeight)//3) + 15,
                                             (((c + 1)*nCanvasWidth)//3) - 15,
                                             (((r + 1)*nCanvasHeight)//3) - 15,
                                             width = 3, fill='red')
                    self.cCanvas.create_line((((c + 1)*nCanvasWidth)//3) - 15,
                                             ((r*nCanvasHeight)//3) + 15,
                                             ((c*nCanvasWidth)//3) + 15 ,
                                             (((r + 1)*nCanvasHeight)//3) - 15,
                                             width = 3, fill='red')
                elif self.grid[r][c] == -1: # Les "O"
                    self.cCanvas.create_oval(((c*nCanvasWidth)//3) + 15,
                                             ((r*nCanvasHeight)//3) + 15,
                                             (((c + 1)*nCanvasWidth)//3) - 15,
                                             (((r + 1)*nCanvasHeight)//3) - 15,
                                             width = 3, outline='blue')
        
        
def replay(mGame):
    # Réinitialise le jeu
    global nPlayer, bWon
    mGame.reinit()
    nPlayer = 1
    bWon = False
    show()

def show():
    # N'affiche que si la partie n'est pas gagnée 
    # (pour laisser le message affiché)
    if not bWon:
        mGame.cCanvas.delete(tk.ALL)
        mGame.disp()
    else:
        return None

# Fonction appelée lord d'un clic sur le canvas
def onCanvasClick(event):
    global nPlayer, bWon
    
    if bWon : return None # La partie est gagnée, rien à faire
    
    nCol = (3 * event.x)//nCanvasWidth #  Transformation de souris(x, y)
    nRow = (3 * event.y)//nCanvasHeight # en tableau[ligne][colone]
    
    if mGame.grid[nRow][nCol] == 0: #     Si la case cliquée est vide
        mGame.play((nRow,nCol),nPlayer) # Joue la case
        nPlayer = - nPlayer #             Et change le joueur
        
    nWinner=mGame.check_win() # Vérifie les victoire
    
    if nWinner in [-1, 1, 3]: # Si quelqu'un à gagné (1 ou -1) ou si il y a 
#                               match nul (3)
        bWon = True # Marque la partie comme finie
        
        # Et affiche le message adapté
        if nWinner == -1:
            mGame.cCanvas.delete(tk.ALL)
            mGame.cCanvas.create_text(150, 150, text="Player 2 Won !")
        elif nWinner == 1:
            mGame.cCanvas.delete(tk.ALL)
            mGame.cCanvas.create_text(150, 150, text="Player 1 Won !")
            pass
        elif nWinner == 3:
            mGame.cCanvas.delete(tk.ALL)
            mGame.cCanvas.create_text(150, 150, text="Match Nul!")
    
    # Met à jour l'affichage
    show()


# Ne s'execute que si le script est lancé directement
if __name__ == "__main__":
    # Creation de la fenetre
    wApp = tk.Tk()
    # Creation du canvas et grid dans wApp
    cGrid = tk.Canvas(wApp, bg=sCanvasBG, height=nCanvasHeight,
                      width=nCanvasWidth)
    cGrid.grid(row=0, column=0, columnspan=2 ,rowspan=2, padx = 3, pady = 3)
    # Instanciation du moteur de jeu
    mGame = GUIMor(cGrid)
    # Les boutons
    btQuit = tk.Button(wApp, text="Quiter", command=wApp.destroy)
    btQuit.grid(row=2, column=1, padx=3, pady=3, sticky='nswe')
    btQuit = tk.Button(wApp, text="Rejouer", command=lambda: replay(mGame))
    btQuit.grid(row=2, column=0, padx=3, pady=3, sticky='nswe')
    cGrid.bind('<Button>', onCanvasClick)
    wApp.title("Morpion")
    wApp.resizable(False, False)
    show()
    wApp.mainloop()
