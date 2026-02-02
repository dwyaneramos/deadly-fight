import pygame as pyg
import sys

sys.path.insert(0, "../")
from fighter import Fighter

#name, steps, indeces, size, scale, offset, fighter_id, can_transform = data
#return [int(size), int(scale), offset, int(steps), indeces, name, fighter_id, can_transform]

class Volt(Fighter):
    def __init__(self, x, y, player, flip):
        self.name = "The Volt"
        self.steps = 48
        self.indeces = [[0,1,2,3,4,5,6], [12,13], [46,47], [15,16], [17, 18, 19, 20, 21, 22], [39, 40, 41, 42, 43], [7, 8, 9, 10, 11], [44, 45], [23, 24, 25, 26, 27]]
        self.size = 64 
        self.scale = 4
        self.offset = [20, 16]
        self.fighter_id = "VLT"
        self.can_transform = False
        sprite_filename =  'assets/images/fighters/' + self.fighter_id + '.png'
        self.sprite_sheet = pyg.image.load(sprite_filename)
        self.fighter_data = [self.size, self.scale, self.offset, self.steps, self.indeces, self.name, self.fighter_id, self.can_transform, self.sprite_sheet]
        super().__init__ (x, y, player, flip, self.fighter_data) 


        self.stamina_costs = [20, 50, 0]

        ## How much stamina each attack should take for each character:
        #stamina_dict = {'PNR':[30, 50, 20],
        #               'STK': [30, 50, 30],
        #               'BMR': [30, 60, 40],
        #               'TRN': [25, 50, 0],
        #               'VLT': [20, 50, 0]}



    def attack1(self):
            """Primary attack"""
            self.attack_cooldown = 0
            attacking_rect = pyg.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 3 * self.rect.width, self.rect.height)
            # pyg.draw.rect(self.surface, (0, 255, 0), attacking_rect)

            if attacking_rect.colliderect(self.target.rect):
                if self.target.blocking is True:
                    self.target.health -= 11
                    self.target.glide_counter = 19
                    self.target.meter -= 8
                else:
                    self.target.health -= 7
                    self.target.glide_counter = 19
                    self.target.hit = True
                    self.target.meter -= 16


    def attack2(self):
        self.attack_cooldown = 50
        """Heavy attack"""
        if self.projectile_fired is False:
            self.projectile_fired = True

            self.projectile_img = pyg.image.load("assets/images/misc/lightning.png").convert_alpha()
            self.projectile_scale = (200, 100)
            self.projectile_img = pyg.transform.scale(self.projectile_img, self.projectile_scale)
            
            self.projectile_dmg = 13
            if self.flip is True:
                self.projectile_rect = self.projectile_img.get_rect(center = [self.rect.x - 50, self.rect.y+50])
                self.projecitle_flipped = True
                self.projectile_speed = -17
            else:
                self.projectile_rect = self.projectile_img.get_rect(center = [self.rect.x+170, self.rect.y+50])
                self.projecitle_flipped = False
                self.projectile_speed = 17
            
            

            

    def attack3(self):
        """sdfds"""
        self.meter += 5
        self.health -= 1.5


    def on_projectile_hit(self, target, blocking, dmg):
        """update fighters when hit"""
        if blocking is True:
            target.health -= dmg * 0.3
            target.meter -= 35
        else:
            target.meter -= 50
            target.health -= dmg
            target.hit = True



