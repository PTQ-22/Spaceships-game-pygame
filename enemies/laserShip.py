import pygame
from game.hp_bar import HpBar


class LaserShip(HpBar):
    
    def __init__(self, x, y, x_start, y_start, name, x_end, y_end, hp):
        self.x = x
        self.y = y
        self.point_x_1 = 59
        self.point_x_2 = 112
        self.point_y_1 = 55
        self.point_y_2 = 107
        self.animation_counter = 0
        self.boom = 0
        self.hp = hp
        self.width = 170
        self.height = 170
        self.x_start = x_start
        self.y_start = y_start
        self.name = name
        self.x_end = x_end
        self.y_end = y_end
        self.go_right = True
        self.ship_imgs = []
        self.shot = True
        self.laser = False
        self.x_fire_place = self.x + 67
        self.y_fire_place = self.y + self.height - 50
        self.img_laser = pygame.image.load(f"./images/lasership/laser_1.png")
        for i in range(11):
            self.ship_imgs.append(pygame.image.load(f"./images/lasership/lasership_{i + 1}.png"))
    
    def draw(self, win):
        self.animation_counter += 1
        if self.animation_counter + 1 >= 27:
            self.animation_counter = 0
        win.blit(self.ship_imgs[self.animation_counter // 3], (self.x, self.y))
        self.move()
        self.hp_bar(win)

    def move(self):
        if self.x <= 0:
            self.go_right = True
        if self.x >= 900:
            self.go_right = False
        if self.go_right:
            self.x += 5
        else:
            self.x -= 5
        self.x_fire_place = self.x + 67
        self.y_fire_place = self.y + self.height - 50

    def laser_shot(self):
        if str(self.x).endswith("00"):
            if self.shot:
                self.shot = False
                return True
            else:
                self.shot = True       
                return False
        else:
            if self.shot:
                return True
            else:
                return False
    
    def draw_laser(self, win, player):
        self.x_laser = self.x_fire_place
        self.y_laser = self.y_fire_place
        win.blit(self.img_laser, (self.x_laser, self.y_laser))
        if self.x_laser > player.x and (self.x_laser + 36) < (player.x + player.width):
            if self.y_laser < player.y: 
                return True
        return False

    def collision(self, player):
        if (self.x + self.width) > player.x and self.x < (player.x + player.width):
            if (self.y + self.height - 45) > player.y and (self.y + 55) < (player.y + player.height):
                return True
        if (self.x + self.width - 50) > (player.x + 40) and (self.x + 40) < (player.x + player.width - 50):
            if (self.y + self.height) > player.y and self.y < (player.y + player.height):
                return True
        return False
