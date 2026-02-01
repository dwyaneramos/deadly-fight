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


        self.stamina_costs = [30, 50, 20]

        ## How much stamina each attack should take for each character:
        #stamina_dict = {'PNR':[30, 50, 20],
        #               'STK': [30, 50, 30],
        #               'BMR': [30, 60, 40],
        #               'TRN': [25, 50, 0],
        #               'VLT': [20, 50, 0]}




    def attack1(self):
        """Primary attack"""
        self.attack_cooldown = 3
        attacking_rect = pyg.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
        # pyg.draw.rect(self.surface, (0, 255, 0), attacking_rect)

        if attacking_rect.colliderect(self.target.rect):
            if self.target.blocking is True:
                self.target.health -= 7
                self.target.glide_counter = 19
            else:
                self.target.health -= 12
                self.target.glide_counter = 18
                self.target.hit = True

    def attack2(self):
        self.attack_cooldown = 50
        """Heavy attack"""
        attacking_rect = pyg.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 3 * self.rect.width, self.rect.height)
        # pyg.draw.rect(self.surface, (0, 255, 0), attacking_rect)

        if attacking_rect.colliderect(self.target.rect):
            if self.target.blocking is True:
                self.target.health -= 30
                self.target.glide_counter = 12
            else:
                self.target.health -= 43
                self.target.glide_counter = 7
                
                self.target.hit = True

    def attack3(self):
        """sdfds"""
        self.attack_cooldown = 5
        self.glide_counter = 6
        self.attacking_glide = True

    def misc_attack(self, screen_width):
        """d"""
        pass
    
        



