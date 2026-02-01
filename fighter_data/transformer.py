
import pygame as pyg
import sys

sys.path.insert(0, "../")
from fighter import Fighter

#name, steps, indeces, size, scale, offset, fighter_id, can_transform = data
#return [int(size), int(scale), offset, int(steps), indeces, name, fighter_id, can_transform]

class Transformer(Fighter):
    def __init__(self, x, y, player, flip):
        self.name = "The Transformer"
        self.steps = 28
        self.indeces = [[0, 1, 2, 1], [22,23], [2], [23], [6, 7, 8, 9, 10, 11], [25, 26, 27, 24], [1, 2, 3, 4, 5], [6, 7, 8, 12, 13, 14, 15, 16], [6, 7, 8, 12, 13, 14, 15, 16], [14, 15, 16], [14, 15, 16], [14, 15, 16],[16, 17, 18, 19, 20, 21],[14, 15, 13, 12, 8, 9, 10, 11],[14, 15, 16],[14, 15, 16],[14, 15, 16],[14, 15, 16]  ]
        self.size = 64 
        self.scale = 4
        self.offset = [20, 20]
        self.fighter_id = "TRN"
        self.can_transform = True
        sprite_filename =  'assets/images/fighters/' + self.fighter_id + '.png'
        self.sprite_sheet = pyg.image.load(sprite_filename)
        self.fighter_data = [self.size, self.scale, self.offset, self.steps, self.indeces, self.name, self.fighter_id, self.can_transform, self.sprite_sheet]
        super().__init__ (x, y, player, flip, self.fighter_data) 


        self.stamina_costs = [25, 50, 0]

        ## How much stamina each attack should take for each character:
        #stamina_dict = {'PNR':[30, 50, 20],
        #               'STK': [30, 50, 30],
        #               'BMR': [30, 60, 40],
        #               'TRN': [25, 50, 0],
        #               'VLT': [20, 50, 0]}



    def attack1(self):
        """Primary attack"""
        self.attack_cooldown = 30
        if self.transformed is False:
            attacking_rect = pyg.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
            #pyg.draw.rect(self.surface, (0, 255, 0), attacking_rect)

            if attacking_rect.colliderect(self.target.rect):
                if self.target.blocking is True:
                    self.target.health -= 10
                    self.target.glide_counter = 19
                else:
                    self.target.health -= 17
                    self.target.glide_counter = 18
                    self.target.hit = True
        else:
            if self.health + 7 > 100:
                self.health = 100
            else:
                self.health += 7

    def attack2(self):
        global CRASH_DMG
        self.attack_cooldown = 10
        """Heavy attack"""
        if self.transformed:
            self.misc_attacking = True
            self.glide_counter = 0
            self.attacking_glide = True
            CRASH_DMG = 45
            self.vel_y = -30
        else:
            self.attack_cooldown = 5
            self.glide_counter = 13
            self.attacking_glide = True

            self.misc_attacking = True
            self.transformed = True
            CRASH_DMG = 20

    def attack3(self):
        """sdfds"""
        self.attack_cooldown = 5
        if self.hit is True:
            self.transformed = False
        
        if self.transformed is True:
            self.transformed = False
        else:
            self.transformed = True
            
        
        
    def misc_attack(self, screen_width):
        global CRASH_DMG
        if self.misc_attacking:
            if self.hit is True:
                self.transformed = False
                self.misc_attacking = False
                self.glide_counter = 20

            if self.glide_counter < 20:
                attacking_rect = pyg.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2.5 * self.rect.width, self.rect.height)
                # pyg.draw.rect(self.surface, (0, 255, 0), attacking_rect)
                if attacking_rect.colliderect(self.target.rect):
                    if self.target.blocking is True:
                        self.target.health -= CRASH_DMG * 0.6
                        self.target.glide_counter = 12
                    else:
                        self.target.health -= CRASH_DMG
                        self.target.glide_counter = 7
                        self.target.hit = True
                    self.transformed = False
                    self.misc_attacking = False
                    self.glide_counter = 20
            else:
                self.misc_attacking = False
                self.glide_counter = 20
                self.transformed = False
