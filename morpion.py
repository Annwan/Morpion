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
        return 0
    
    def disp(self):
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
        return 0
    
def parse(command):
    return 0

def run(game):
    game.disp()
    pass
