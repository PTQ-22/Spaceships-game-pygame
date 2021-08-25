import pygame
from random import randint
from .enemyRedSmall import EnemyRedSmall
from .bullet import EnemyBullet


class MissileEnemy(EnemyRedSmall):

    def __init__(self, x, y, x_start, y_start, name, x_end, y_end, hp):
        self.x = x
        self.y = y
        self.point_x_1 = 49
        self.point_x_2 = 74
        self.point_y_1 = 38
        self.point_y_2 = 63
        self.animation_counter = 0
        self.boom = 0
        self.hp = hp
        self.width = 120
        self.height = 120
        self.x_start = x_start
        self.y_start = y_start
        self.name = name
        self.x_end = x_end
        self.y_end = y_end
        self.go_right = True
        self.enemy1_ship_imgs = []
        for i in range(11):
            self.enemy1_ship_imgs.append(pygame.image.load(f"./images/missile_enemy/missile_player_{i + 1}.png"))
    
    def shot(self, bullets, player_x):
        if self.animation_counter == 0:
            bullets.append(Missile(self.fire_place_x, self.y + self.height, player_x))      
        return bullets


class Missile(EnemyBullet):

    def __init__(self, x, y, player_x):
        self.img = pygame.image.load("./images/missile/missile_5.png")
        self.x = x
        self.y = y
        self.x_track_pos = player_x + 50

    def move(self):
        self.y += 10
        if self.x > self.x_track_pos + 3:
            self.x -= 10
        elif self.x < self.x_track_pos - 3:
            self.x += 10
        else:
            self.x += 0
    
    def draw_hit(self, win):
        
        pygame.draw.circle(win, (255, 255, 0), (self.x, self.y), 3)

        pygame.draw.circle(win, (255, 100, 0), (self.x, self.y), 6)  
        pygame.draw.circle(win, (255, 255, 0), (self.x, self.y), 3)                    
        pygame.draw.circle(win, (255, 0, 0), (self.x, self.y), 35)
        pygame.draw.circle(win, (255, 100, 0), (self.x, self.y), 6)  
        pygame.draw.circle(win, (255, 255, 0), (self.x, self.y), 3)
                        
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), 40)
        pygame.draw.circle(win, (255, 0, 0), (self.x, self.y), 35)
        pygame.draw.circle(win, (255, 100, 0), (self.x, self.y), 6)  
        pygame.draw.circle(win, (255, 255, 0), (self.x, self.y), 3) 