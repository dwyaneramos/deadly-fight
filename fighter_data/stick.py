import pygame as pyg
import sys

sys.path.insert(0, "../")
from fighter import Fighter

class Stick(Fighter):
    def __init__(self, x, y, player, flip):
        self.name = "The Stick"
        self.steps = 67
        self.indeces = [[0,16,17,18,19,20,21,22,23,24,25,26], [0,1,2,3],[5],[27,28],[11,12,13,14,15],[6,7,8,9],[36,37,38,39,40],[29,30,31,32,33,34], [44, 45, 46],[62, 63,64 ,65,66], [62, 63,64 ,65,66],  [48], [27,28], [41, 42, 43, 11,12,13,14,15], [62, 63,64 ,65,66], [49,50,51,52], [53,54,55,56,57], [61,59,60,61,59,60,61,58]]
        self.size = 64 
        self.scale = 4
        self.offset = [20, 18]
        self.fighter_id = "STK"
        self.can_transform = True
        sprite_filename =  'assets/images/fighters/' + self.fighter_id + '.png'
        self.sprite_sheet = pyg.image.load(sprite_filename)
        self.fighter_data = [self.size, self.scale, self.offset, self.steps, self.indeces, self.name, self.fighter_id, self.can_transform, self.sprite_sheet]
        super().__init__ (x, y, player, flip, self.fighter_data) 

        self.stamina_costs = [30, 50, 30]

    def attack1(self):
        """Primary attack"""
        DMG = 10
        self.attack_cooldown = 20
        if self.transformed:
            DMG = 12
            self.attack_cooldown = 14

        
        attacking_rect = pyg.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
        if attacking_rect.colliderect(self.target.rect):
            if self.target.blocking is True:
                self.target.health -= DMG * 0.5
                self.target.glide_counter = 19
            else:
                self.target.health -= DMG
                self.target.hit = True
                self.target.glide_counter = 18
        

    def attack2(self):
        """Heavy attack"""
        self.attack_cooldown = 35
        
        if self.transformed is False:
            # Normal Heavy Attack
            DMG = 30
            attacking_rect = pyg.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
            # pyg.draw.rect(self.surface, (0, 255, 0), attacking_rect)
            if attacking_rect.colliderect(self.target.rect):
                if self.target.blocking is True:
                    self.target.health -= DMG * 0.5
                    self.target.glide_counter = 16
                else:
                    self.target.health -= DMG
                    self.target.glide_counter = 7
                
                    self.target.hit = True
        else:
        # Transformed Heavy Attack / Teleport
            key = pyg.key.get_pressed()
            if key[pyg.K_s] and self.player == 1 or key[pyg.K_DOWN] and self.player == 2:
                # keep-away teleport
                if self.flip:
                    # When player is on the right side of the screen
                    self.rect.x = 900
                else:
                    # When player is on the left side of the screen 
                    self.rect.x = 0
            else:
                # charging teleport
                if self.flip:
                    # When player is on the right side of the screen
                    self.rect.x = self.target.rect.x + 150
                else:
                    # When player is on the left side of the screen 
                    self.rect.x = self.target.rect.x - 150

    def attack3(self):
        if self.transformed is False:
            self.transformed = True
            self.health += 40
            self.name = 'The Stick Avatar'
            self.attack_cooldown = 100
        else:
            if self.projectile_fired is False:
                self.projectile_fired = True
                self.projectile_img = pyg.image.load('assets/images/misc/purple-projectile.png').convert_alpha()
                self.projectile_rect = self.projectile_img.get_rect(center = [self.rect.x, self.rect.y+50])

                if self.flip:
                    self.projectile_flipped = True
                else:
                    self.projectile_flipped = False


    def update_meter(self):
        if self.meter < 0:
            self.meter = 0
        if self.meter > 100:
            self.meter = 100
        
        # Additional 'if' check to prevent it going over
        if self.meter < 100:
            if self.transformed:
                self.meter += 0.55
            else:
                self.meter += 0.35

