#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Copyright © 2018 Antoine COMBET

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
from __future__ import print_function
from __future__ import nested_scopes
from __future__ import generators
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals

import sys
import platform
import os
import time
from random import random

try:
    from morpion_bot import DumbBot, SmartBot
except ImportError:
    BOTS = False
else:
    BOTS = True

COORD_CONV = {"A1":(0,0), "B1":(0,1), "C1":(0,2),
              "A2":(1,0), "B2":(1,1), "C2":(1,2),
              "A3":(2,0), "B3":(2,1), "C3":(2,2)}
def s_input(prompt):
    if sys.version[0] == '2':
        return raw_input(prompt)
        pass
    else:
       return input(prompt) 

def clear_screen():
    if 'Windows' in platform.platform() :
        os.system("CLS")
    else:
        os.system("clear")

class Morpion(object):
    
    def __init__(self, chars=[" ", "X", "O"]):
        self.grid = [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]
        self.disp_chars = chars
    
    def reinit(self):
        self.grid = [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]
        
    
    def play(self, cell, player):
        if not (0 <= cell[0] and cell[0]<3 and 0<=cell[1] and cell[1]<3):
            return 1
        elif self.grid[cell[0]][cell[1]] != 0:
            return 2
        else:
            self.grid[cell[0]][cell[1]] = player
        return 0
    
    def disp(self):
        clear_screen()
        print("      A   B   C  ")
        i = 1
        for line in self.grid:
            print("    +---+---+---+")
            print("  " + str(i), end=" ")
            i = i + 1
            for cell in line:
                print("| " + self.disp_chars[cell], end=" ")
            print("|")
        print("    +---+---+---+")
    
    def check_win(self):
        A1 = self.grid[0][0]
        B1 = self.grid[0][1]
        C1 = self.grid[0][2]
        A2 = self.grid[1][0]
        B2 = self.grid[1][1]
        C2 = self.grid[1][2]
        A3 = self.grid[2][0]
        B3 = self.grid[2][1]
        C3 = self.grid[2][2]
        if A1 == B1 and A1 == C1:
            return A1
        elif A1 == A2 and A1 == A3:
            return A1
        elif B1 == B2 and B1 == B3:
            return B1
        elif A2 == B2 and A2 == C2:
            return A2
        elif C1 == C2 and C1 == C3:
            return C1
        elif A1 == B2 and A1 == C3:
            return A1
        elif C1 == B2 and C1 == A3:
            return C1
        else:
            full = True
            for line in self.grid:
                for cell in line:
                    if cell == 0:
                        full = False
            if not full:
                return 0
            else:
                return 3
    
def parse(command):
    cmds = []
    inst = ""
    command = command + " "
    for c in command:
        if c == " ":
            cmds.append(inst.upper())
            inst = ""
        else:
            inst = inst + c
    to_pop = []
    for i in range(len(cmds)-1, -1, -1):
        if cmds[i] == '':
            to_pop.append(i)
    for i in to_pop:
        cmds.pop(i)
    return cmds

def run2j(game):
    rep = True
    p1_turn = True
    quited = False
    while not(game.check_win() or quited):
        played = False
        if p1_turn:
            game.disp()
            inp = s_input("Au tour du Joueur 1 (h pour l'aide)\n>>> ")
            cmd = parse(inp)
            if cmd == []:
                cmd = [None]

            if cmd[0] in ["JOUER", "J"] and len(cmd)>=2:
                if cmd[1] in COORD_CONV.keys():
                    result = game.play(COORD_CONV[cmd[1]],1)
                    if result == 2: #case déja utilisée
                        print("Case " + cmd[1] + " déjà occupée")
                        time.sleep(1)
                    
                    else:
                        played = True
                
                
                else:
                    print("coordonnés invalides")
                    time.sleep(1)
                
            
            elif cmd[0] in ["QUITER", "QUIT", "Q"]:
                quited = True
                rep = False
            
            elif cmd[0] in ["REJOUER", "RJ", "R"]:
                quited = True
                rep  = True

            elif cmd[0] == "MAKEHIMWIN" and len(cmd) == 2:
                try:
                    p = int(cmd[1])
                    assert p in [1,2]
                except:
                    print("commande invalide")
                    time.sleep(1)
                    continue
                game.grid = [[p for i in range(3)] for i in range(3)]
                
            elif cmd[0] == "H":
                clear_screen()
                print("Pour jouer une case entrez :\n    jouer <coordonées>\n"+
                      "    j <coordonées>\noù <coordonées> sont les coordonée"+
                      "s de la case telles que A1\nPour relancer la partie, e"+
                      "ntrez:\n    rejouer\n    rj\n    r\nPour afficher ulté"+
                      "rieurement cette aide, entrez:\n    h\nPour quiter, en"+
                      "trez:\n    quiter\n    quit\n    q\n")
                time.sleep(5)
            else:
                print("commande invalide")
                time.sleep(1)

        
        else:
            game.disp()
            inp = s_input("Au tour du Joueur 2 (h pour l'aide)\n>>> ")
            cmd = parse(inp)
            if cmd == []:
                cmd = [None]
            
            if cmd[0] in ["JOUER", "J"] and len(cmd)>=2:
                if cmd[1] in COORD_CONV.keys():
                    result = game.play(COORD_CONV[cmd[1]],2)
                    if result == 2:
                        print("Case " + cmd[1] + " déjà occupée")
                        time.sleep(1)
                    
                    else:
                        played = True
                
                
                else:
                    print("coordonnés invalides")
                    time.sleep(1)
                    
            
            elif cmd[0] in ["QUITER", "QUIT", "Q"]:
                quited = True
                rep = False


            elif cmd[0] == "MAKEHIMWIN" and len(cmd) == 2:
                try:
                    p = int(cmd[1])
                    assert p in [1,2]
                except:
                    print("commande invalide")
                    time.sleep(1)
                    continue
                game.grid = [[p for i in range(3)] for i in range(3)]
                
            elif cmd[0] in ["REJOUER", "RJ", "R"]:
                quited = True
                rep  = True
            
            elif cmd[0] == "H":
                clear_screen()
                print("Pour jouer une case entrez :\n    jouer <coordonées>\n"+
                      "    j <coordonées>\noù <coordonées> sont les coordonée"+
                      "s de la case telles que A1\nPour relancer la partie, e"+
                      "ntrez:\n    rejouer\n    rj\n    r\nPour afficher ulté"+
                      "rieurement cette aide, entrez:\n    h\nPour quiter, en"+
                      "trez:\n    quiter\n    quit\n    q\n")
                time.sleep(5)
            
            else:
                print("commande invalide")
                time.sleep(1)
            
        
        if played:
            p1_turn = not p1_turn
            
    game.disp()
    if not quited:
        if not game.check_win() == 3:
            print('Le joueur ' + str(game.check_win()) + ' a gagné')
        else:
            print('Match nul')
        print()
        srep = s_input("Voulez-vous rejouer ?(o/n)").lower()
        if srep == "n":
            rep = False
        
        else:
            rep = True
            
    if rep:
        clear_screen()
        print('Nouvelle Partie')
        time.sleep(1)
    return rep

def runbot(game, t):
    clear_screen()
    rep = True
    quited = False
    if random() < 0.5:
        p_turn = True
        a = 2
        p = 1
        print("Vous serez le joueur 1, l'ordinateur le joueur 2.")
        time.sleep(1)
    else:
        p_turn = False
        a = 1
        p = 2
        print("Vous serez le joueur 2, l'ordinateur le joueur 1.")
        time.sleep(1)
    if t:
        bot = SmartBot(game, a)
    else:
        bot = DumbBot(game, a)
    while not(game.check_win() or quited):
        played = False
        if p_turn:
            game.disp()
            inp = s_input("Au tour du Joueur "+str(p)+"(h pour l'aide)\n>>> ")
            cmd = parse(inp)
            if cmd == []:
                cmd = [None]

            if cmd[0] in ["JOUER", "J"] and len(cmd)>=2:
                if cmd[1] in COORD_CONV.keys():
                    result = game.play(COORD_CONV[cmd[1]],p)
                    if result == 2: #case déja utilisée
                        print("Case " + cmd[1] + " déjà occupée")
                        time.sleep(1)
                    
                    else:
                        played = True
                
                
                else:
                    print("coordonnés invalides")
                    time.sleep(1)
                
            
            elif cmd[0] in ["QUITER", "QUIT", "Q"]:
                quited = True
                rep = False
            
            elif cmd[0] in ["REJOUER", "RJ", "R"]:
                quited = True
                rep  = True

            elif cmd[0] == "MAKEHIMWIN" and len(cmd) == 2:
                try:
                    k = int(cmd[1])
                    assert k in [1,2]
                except:
                    print("commande invalide")
                    time.sleep(1)
                    continue
                game.grid = [[k for i in range(3)] for i in range(3)]
                
            elif cmd[0] == "H":
                clear_screen()
                print("Pour jouer une case entrez :\n    jouer <coordonées>\n"+
                      "    j <coordonées>\noù <coordonées> sont les coordonée"+
                      "s de la case telles que A1\nPour relancer la partie, e"+
                      "ntrez:\n    rejouer\n    rj\n    r\nPour afficher ulté"+
                      "rieurement cette aide, entrez:\n    h\nPour quiter, en"+
                      "trez:\n    quiter\n    quit\n    q\n")
                time.sleep(5)
            else:
                print("commande invalide")
                time.sleep(1)

        
        else:
            bot.play()
            played = True
            
        
        if played:
            p_turn = not p_turn
            
    game.disp()
    if not quited:
        if not game.check_win() == 3:
            print('Le joueur ' + str(game.check_win()) + ' a gagné')
        else:
            print('Match nul')
        print()
        srep = s_input("Voulez-vous rejouer ?(o/n)").lower()
        if srep == "n":
            rep = False
        
        else:
            rep = True
            
    if rep:
        clear_screen()
        print('Nouvelle Partie')
        time.sleep(1)
    return rep
    

if __name__ == '__main__':
    print("""    Morpion  Copyright © 2018  Antoine COMBET
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions.
    See https://www.gnu.org/licenses/gpl.html for details.""")
    time.sleep(2)
    replay = True
    mor = Morpion()
    while replay:
        clear_screen()
        if not BOTS:
            mode = '0'
        else:
            print("Les Joueurs automatiques sont disponibles.\nPour jouer con"+
                  "tre un autre joueur, entrez 0\nPour jouer contre l'orrdina"+
                  "teur en mode aléatoire, entrez 1\nPour jouer contre un ord"+
                  "inateur 'optimal', entrez 2.")
            mode = s_input(">>>")
        if mode == '0':
            replay = run2j(mor)
        elif mode == '1':
            replay = runbot(mor, 0)
        elif mode == '2':
            replay = runbot(mor, 1)
        else:
            pass
        mor.reinit()
