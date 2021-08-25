import pygame
from .enemyRedSmall import EnemyRedSmall
from .bullet import EnemyBullet

class TeleporterEnemy(EnemyRedSmall):

    def __init__(self, x, y, x_start, y_start, name, x_end, y_end, hp):
        self.x = x
        self.y = y
        self.point_x_1 = 0
        self.point_x_2 = 0
        self.point_y_1 = 0
        self.point_y_2 = 120
        self.animation_counter = 0
        self.hp = hp
        self.width = 120
        self.height = 120
        self.x_start = x_start
        self.y_start = y_start
        self.name = name
        self.boom = 0
        self.x_end = x_end
        self.y_end = y_end
        self.go_right = True
        self.enemy1_ship_imgs = []
        self.boom_counter = 31
        for i in range(11):
            self.enemy1_ship_imgs.append(pygame.image.load(f"./images/teleporter_enemy/tel_enemy_{i + 1}.png"))
        
    def shot(self, bullets):
        if self.animation_counter == 0:
            bullets.append(EnemyBullet(self.fire_place_x, self.y + self.height))      
            bullets.append(EnemyBullet(self.x, self.y + self.height))      
            bullets.append(EnemyBullet(self.x + 95, self.y + self.height))      
        return bullets

    def teleport(self):
        self.boom_counter = 0
        self.x_before = self.x
        if self.x < 350:
            self.x += 400
        elif self.x > 350:
            self.x -= 400
        self.x_after = self.x

    