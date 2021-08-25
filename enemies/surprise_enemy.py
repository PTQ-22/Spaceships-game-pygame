import pygame
from game.hp_bar import HpBar
from enemies.bullet import EnemyBullet

class SurpriseEnemy(HpBar):

    def __init__(self):
        self.x = 200
        self.y = 52
        self.point_x_1 = 125
        self.point_x_2 = 275
        self.point_y_1 = 100
        self.point_y_2 = 310
        self.boom = 0
        self.animation_counter = 0
        self.hp = 800
        self.width = 400
        self.height = 400
        self.x_start = 40
        self.y_start = 10
        self.name = "PRZECIWNIK"
        self.x_end = 830
        self.y_end = 40
        self.go_right = True
        self.enemy1_ship_img = pygame.image.load("./images/surprise_enemy/surprise_enemy.png")
    
    def draw(self, win):
        self.animation_counter += 1
        if self.animation_counter + 1 >= 27:
            self.animation_counter = 0
        win.blit(self.enemy1_ship_img, (self.x, self.y))
        self.move()
        self.hp_bar(win)

    def move(self):
        if self.x <= 200:
            self.go_right = True
        if self.x >= 450:
            self.go_right = False
        if self.go_right:
            self.x += 3
        else:
            self.x -= 3
        self.fire_place_x = self.x + 200

    def shot(self, bullets):
        if self.animation_counter == 0 or self.animation_counter == 10 or self.animation_counter == 20:
            bullets.append(EnemyBullet(self.fire_place_x, self.y + self.height))      
        return bullets
    
    def collision(self, player):
        if (self.x + self.width) > player.x and self.x < (player.x + player.width):
            if (self.y + self.point_y_2) > player.y and (self.y) < (player.y + player.height):
                return True
        if (self.x + self.point_x_2) > (player.x + 40) and (self.x + self.point_x_1) < (player.x + player.width - 40):
            if (self.y + self.height) > player.y and (self.y) < (player.y + player.height):
                return True
        return False

    def BIG_boom_after_collision(self, win):
        if self.boom <= 100:
            pygame.draw.circle(win, (255, 255, 0), (self.x + 150, self.y + 150), 80)

            pygame.draw.circle(win, (255, 100, 0), (self.x + 150, self.y + 150), 100)  
            pygame.draw.circle(win, (255, 255, 0), (self.x + 150, self.y + 150), 80)
                
            pygame.draw.circle(win, (255, 0, 0), (self.x + 150, self.y + 150), 120)
            pygame.draw.circle(win, (255, 100, 0), (self.x + 150, self.y + 150), 100)  
            pygame.draw.circle(win, (255, 255, 0), (self.x + 150, self.y + 150), 80)
                    
            pygame.draw.circle(win, (0, 0, 0), (self.x + 150, self.y + 150), 150)
            pygame.draw.circle(win, (255, 0, 0), (self.x + 150, self.y + 150), 120)
            pygame.draw.circle(win, (255, 100, 0), (self.x + 150, self.y + 150), 100)  
            pygame.draw.circle(win, (255, 255, 0), (self.x + 150, self.y + 150), 80) 
            self.boom += 1