import pygame as pyg
import sys

sys.path.insert(0, "../")
from fighter import Fighter

#name, steps, indeces, size, scale, offset, fighter_id, can_transform = data
#return [int(size), int(scale), offset, int(steps), indeces, name, fighter_id, can_transform]

class Puncher(Fighter):
    def __init__(self, x, y, player, flip):
        self.name = "The Puncher"
        self.steps = 36
        self.indeces =  [[1, 11, 12], [0,1],[24], [9,10], [29, 30, 31, 32, 33, 34], [25,26,27],[5,6, 7], [3, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 1],[35]]
        self.size = 64 
        self.scale = 4
        self.offset = [20, 22]
        self.fighter_id = "PNR"
        self.can_transform = False
        sprite_filename =  'assets/images/fighters/' + self.fighter_id + '.png'
        self.sprite_sheet = pyg.image.load(sprite_filename)
        self.fighter_data = [self.size, self.scale, self.offset, self.steps, self.indeces, self.name, self.fighter_id, self.can_transform, self.sprite_sheet]
        super().__init__ (x, y, player, flip, self.fighter_data) 
        



