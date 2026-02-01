import pygame as pyg
import sys

sys.path.insert(0, "../")
from fighter import Fighter

#name, steps, indeces, size, scale, offset, fighter_id, can_transform = data
#return [int(size), int(scale), offset, int(steps), indeces, name, fighter_id, can_transform]

class Bomber(Fighter):
    def __init__(self, x, y, player, flip):
        self.name = "The Bomber"
        self.steps = 39
        self.indeces = [[28,29,30,31,32,33], [13,14], [15], [22,23], [22,23,24,25,26,26,26,26,27], [35,36,37,38], [16,16,17,18], [3,3,4,4,4,5,5,5,5,6,6,6,6,7,8,9,10,11,10,10], [1,1,1,2,2,2,2]]
        self.size = 64 
        self.scale = 5
        self.offset = [20, 20]
        self.fighter_id = "BMR"
        self.can_transform = False
        sprite_filename =  'assets/images/fighters/' + self.fighter_id + '.png'
        self.sprite_sheet = pyg.image.load(sprite_filename)
        self.fighter_data = [self.size, self.scale, self.offset, self.steps, self.indeces, self.name, self.fighter_id, self.can_transform, self.sprite_sheet]
        super().__init__ (x, y, player, flip, self.fighter_data) 


        self.stamina_costs = [30, 60, 40]

        ## How much stamina each attack should take for each character:
        #stamina_dict = {'PNR':[30, 50, 20],
        #               'STK': [30, 50, 30],
        #               'BMR': [30, 60, 40],
        #               'TRN': [25, 50, 0],
        #               'VLT': [20, 50, 0]}


    def attack1(self):
        """Primary attack"""
        self.attack_cooldown = 30
        attacking_rect = pyg.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
        # pyg.draw.rect(self.surface, (0, 255, 0), attacking_rect)

        if attacking_rect.colliderect(self.target.rect):
            if self.target.blocking is True:
                self.target.health -= 5
                self.target.glide_counter = 19
            else:
                self.target.health -= 10
                self.target.glide_counter = 18
                self.target.hit = True

    def attack2(self):
        self.attack_cooldown = 50
        """Heavy attack"""
        attacking_rect = pyg.Rect(self.rect.centerx - 3 * self.rect.width, self.rect.y - 150, 7.5 * self.rect.width, self.rect.height * 2)
        #pyg.draw.rect(self.surface, (0, 255, 0), attacking_rect)
        self.health -= 30
        if attacking_rect.colliderect(self.target.rect):
            if self.target.blocking is True:
                self.target.health -= 30
                self.target.glide_counter = 12
            else:
                self.target.health -= 55
                self.target.glide_counter = 7
            
                self.target.hit = True

    def attack3(self):
        """sdfds"""
        """ CHANGE THINGS TO SELF.PROJECTILE.VEL_Y ETCC"""
        self.misc_attacking = True
        self.attack_cooldown = 40
        self.projectile_scale = (64, 64)
        self.projectile_dmg = 18

        self.projectile_vel_y = 0
        self.projectile_dy = -60

        self.projectile_img = pyg.image.load("assets/images/misc/bomb.png").convert_alpha()
        self.projectile_img = pyg.transform.scale(self.projectile_img, self.projectile_scale)

        if self.flip is True:
            self.projectile_rect = self.projectile_img.get_rect(center = [self.rect.x, self.rect.y+50])
            self.projecitle_flipped = True
            self.projectile_speed = -20
        else:
            self.projectile_rect = self.projectile_img.get_rect(center = [self.rect.x+170, self.rect.y+50])
            self.projecitle_flipped = False
            self.projectile_speed = 20

    def misc_attack(self, screen_width):
        """sfds"""
        if self.projectile_rect is None:
            return

        if self.projectile_rect.colliderect(self.target.rect):
            # if bomb hits opponent
            print("HITTTT")
            # Resets 
            #self.projectile_rect = self.projectile.get_rect(center = [self.rect.x+230, self.rect.y+50])
            # Damage
            if self.target.blocking is True:
                self.target.health -= self.projectile_dmg * 0.3
            else:
                self.target.health -= self.projectile_dmg
                self.target.hit = True
        
            self.misc_attacking = False
            self.projectile_rect = None
            return
        # If bomb goes offscreen
        if self.projectile_rect.left  + self.projectile_speed  < 0:
            self.projectile_speed = -self.projectile_rect.left
            self.projectile_rect.x += self.projectile_speed
            
        elif self.projectile_rect.right + self.projectile_speed > 1000:
            self.projectile_speed = 1000 - self.projectile_rect.right
            self.projectile_rect.x += self.projectile_speed
       


        # movement
        if self.projectile_rect.y + self.projectile_dy > 490:
            self.projectile_dy = 0
            
        else:
            self.projectile_vel_y += 1
            self.projectile_dy += self.projectile_vel_y

            if self.projectile_flipped is True:
                # Changes direction of sprite depending on player direction
                self.projectile_rect.x += -self.projectile_speed
                self.projectile_img = pyg.transform.rotate(self.projectile_img, 180)
            
            else:
                self.projectile_rect.x += self.projectile_speed
            
        self.projectile_rect.y += self.projectile_dy
        # Draws sprite
        self.surface.blit(self.projectile_img, self.projectile_rect)

