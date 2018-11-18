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
