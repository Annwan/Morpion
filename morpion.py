#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Copyright (C) 2018 Konganwan

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
            return 0 
    
def parse(command):
    cmds = []
    inst = ""
    command = command + " "
    for c in command:
        if c == " ":
            cmds.append(inst)
            inst = ""
        else:
            inst = inst + c
    cmds.append(inst)
    to_pop = []
    for i in range(len(cmds)-1, -1, -1):
        if cmds[i] == '':
            to_pop.append(i)
    for i in to_pop:
        cmds.pop(i)
    return cmds
def run(game):
#    turn = 0
    game.disp()
    pass
