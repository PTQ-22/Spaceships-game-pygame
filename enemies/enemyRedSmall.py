import pygame
from game.hp_bar import HpBar
from .bullet import EnemyBullet


class EnemyRedSmall(HpBar):
    def __init__(self, x, y, x_start, y_start, name, x_end, y_end, hp):
        self.x = x
        self.y = y
        self.point_x_1 = 49
        self.point_x_2 = 74
        self.point_y_1 = 38
        self.point_y_2 = 63
        self.boom = 0
        self.animation_counter = 0
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
            self.enemy1_ship_imgs.append(pygame.image.load(f"./images/red_enemy/enemy1_{i + 1}.png"))
    
    def draw(self, win):
        self.animation_counter += 1
        if self.animation_counter + 1 >= 27:
            self.animation_counter = 0
        win.blit(self.enemy1_ship_imgs[self.animation_counter // 3], (self.x, self.y))
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
        self.fire_place_x = self.x + 47

    
    def shot(self, bullets):
        if self.animation_counter == 0:
            bullets.append(EnemyBullet(self.fire_place_x, self.y + self.height))      
        return bullets

    def collision(self, player):
        if (self.x + self.width) > player.x and self.x < (player.x + player.width):
            if (self.y + self.height - 45) > player.y and (self.y + 55) < (player.y + player.height):
                return True
        if (self.x + self.width - 40) > (player.x + 40) and (self.x + 40) < (player.x + player.width - 40):
            if (self.y + self.height) > player.y and self.y < (player.y + player.height):
                return True
        return False
