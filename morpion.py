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
import platform
import os
import time

COORD_CONV = {"A1":(0,0), "B1":(0,1), "C1":(0,2),
              "A2":(1,0), "B2":(1,1), "C2":(1,2),
              "A3":(2,0), "B3":(2,1), "C3":(2,2)}

def clear_screen():
    if platform.platform() == 'Windows':
        os.system("CLS")
    else:
        os.system("clear")

class Morpion(object):
    
    def __init__(self, chars=[" ", "X", "O"]):
        self.grid = [[0 for i in range(3)] for i in range(3)]
        self.disp_chars = chars
    
    def reinit(self):
        self.grid = [[0 for i in range(3)] for i in range(3)]
        
    
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
        if (self.grid[0][0] == self.grid[1][0] == self.grid[2][0] or
            self.grid[0][0] == self.grid[0][1] == self.grid[0][2] or
            self.grid[0][0] == self.grid[1][1] == self.grid[2][2]):
            return self.grid[0][0]
        elif (self.grid[0][1] == self.grid[1][1] == self.grid[2][1] or
              self.grid[1][0] == self.grid[1][1] == self.grid[1][2] or
              self.grid[0][2] == self.grid[1][1] == self.grid[2][0]):
            return self.grid[1][1]
        elif (self.grid[2][0] == self.grid[2][1] == self.grid[2][2] or
              self.grid[0][2] == self.grid[1][2] == self.grid[2][2]):      
            return self.grid[2][2]
        else:
            full = True
            for line in self.grid:
                for cell in line:
                    if cell == 0:
                        full == False
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

def run(game):
    rep = True
    p1_turn = True
    quited = False
    while not(game.check_win() or quited):
        played = False
        if p1_turn:
            game.disp()
            inp = input("Au tour du Joueur 1\n>>> ")
            cmd = parse(inp)
            if cmd == []:
                cmd = [None]
            
            if cmd[0] in ["JOUER", "J"] and len(cmd)>=2:
                if cmd[1] in COORD_CONV.keys():
                    result = game.play(COORD_CONV[cmd[1]],1)
                    if result == 2: #case déja utilisée
                        print("Case " + cmd[1] + " déjà occupée")
                        time.sleep(2)
                    
                    else:
                        played = True
                
                
                else:
                    print("coordonnés invalides")
                    time.sleep(2)
                
            
            elif cmd[0] in ["QUITER", "QUIT", "Q"]:
                quited = True
                rep = False
            
            elif cmd[0] in ["REJOUER", "RJ", "R"]:
                quited = True
                rep  = True
            
            else:
                print("commande invalide")
                time.sleep(2)
            
        
        else:
            game.disp()
            inp = input("Au tour du Joueur 2\n>>> ")
            cmd = parse(inp)
            if cmd == []:
                cmd = [None]
            
            if cmd[0] in ["JOUER", "J"] and len(cmd)>=2:
                if cmd[1] in COORD_CONV.keys():
                    result = game.play(COORD_CONV[cmd[1]],2)
                    if result == 2:
                        print("Case " + cmd[1] + " déjà occupée")
                        time.sleep(2)
                    
                    else:
                        played = True
                
                
                else:
                    print("coordonnés invalides")
                    time.sleep(2)
                    
            
            elif cmd[0] in ["QUITER", "QUIT", "Q"]:
                quited = True
                rep = False
            
            elif cmd[0] in ["REJOUER", "RJ", "R"]:
                quited = True
                rep  = True
            
            else:
                print("commande invalide")
                time.sleep(2)
            
        
        if played:
            p1_turn = not p1_turn
            
    if not quited:
        srep = input("Voulez-vous rejouer ?(o/n)").lower()
        if srep == "n":
            rep = False
        
        else:
            rep = True
            
    
    return rep
    
