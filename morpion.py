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
    
    def __init__(self):
        self.grid = [[0 for i in range(3)] for i in range(3)]
        self.disp_chars = [" ", "X", "O"]
    
    def reinit(self):
        self.grid = [[0 for i in range(3)] for i in range(3)]
        pass
    
    def play(self, cell, player):
        pass
    
    def disp(self):
        for line in self.grid:
            print("+---+---+---+")
            print("|   |   |   |")
            for cell in line:
                print("| " + self.disp_chars[cell], end=" ")
            print("|")
            print("|   |   |   |")
        print("+---+---+---+")
        pass
    
    def check_win(self):
        pass
    
    
def run(mor):
    mor.disp()
    pass
