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
from random import randint
class Bot(object):
    def __init__(self, game, pid):
        self.game = game
        self.pid = pid
        pass
    
    def choose(self):
        return 0,0

    def play(self):
        return self.game.play(self.choose(), self.pid)
    
    

class SmartBot(Bot):
    def __init__(self, game, pid):
        Bot.__init__(self, game, pid)
        self.turn = 0
    
    def block_opp(self):
        A1 = self.game.grid[0][0]
        B1 = self.game.grid[0][1]
        C1 = self.game.grid[0][2]
        A2 = self.game.grid[1][0]
        B2 = self.game.grid[1][1]
        C2 = self.game.grid[1][2]
        A3 = self.game.grid[2][0]
        B3 = self.game.grid[2][1]
        C3 = self.game.grid[2][2]
        if (A1 == A2 and A1 != 0 or C1 == B2 and C1 != 0 or B2 == B3 and B2 != 0) and A3 == 0:
            return 2, 0
        elif (A1 == A3 and A1 != 0 or B2 == C2 and B2 != 0) and A2 == 0:
            return 1, 0
        elif (A2 == A3 and A2 != 0 or B2 == C3 and B2 != 0 or B1 == C1 and B1 != 0) and A1 == 0:
            return 0, 0
        elif (A3 == C3 and A3 != 0 or B1 == B2 and B1 != 0) and B3 == 0:
            return 2, 1
        elif (B1 == B3 and B1 != 0 or A2 == C2 and A2 != 0 or C1 == A3 and C1 != 0 or A1 == C3 and A1 != 0) and B2 == 0:
            return 1, 1
        elif (B2 == B3 and B2 != 0 or C1 == A1 and A1 != 0) and B1 == 0:
            return 0, 1
        elif (C1 == C2 and C1 != 0 or A3 == B3 and A3 != 0 or A1 == B2 and A1 != 0) and C3 == 0: 
            return 2, 2
        elif (C1 == C3 and C1 != 0 or A2 == B2 and A2 != 0) and C2 == 0:
            return 1, 2
        elif (C2 == C3 and C2 != 0 or B2 == A3 and B2 != 0 or A1 == B1 and B1 != 0) and C1 == 0:
            return 0, 2
        else:
            return None, None
        
        
    def choose(self):
        if self.turn == 0 and self.pid == 1:
            self.turn += 1
            return 0,0
        elif self.turn == 0 and self.pid == 2 and self.game.grid[1][1] != 0:
            self.turn += 1
            return 0,0
        elif self.turn == 0 and self.pid == 2:
            self.turn += 1
            return 1,1
        else:
            self.turn += 1
            p = self.block_opp()
            if p[0] is None:
                found = False
                while not found:
                    row = randint(0,2)
                    col = randint(0,2)
                    if self.game.grid[row][col] == 0:
                        found = True
                return row, col
            else:
                return p
        

class DumbBot(Bot):
    def __init__(self, game, pid):
        Bot.__init__(self, game, pid)
        
    def choose(self):
        found = False
        while not found:
            row = randint(0,2)
            col = randint(0,2)
            if self.game.grid[row][col] == 0:
                found = True
        return row, col