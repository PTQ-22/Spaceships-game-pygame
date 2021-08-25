import pygame
from game.hp_bar import HpBar
from .bullet import EnemyBullet
from .missileEnemy import Missile


class Boss(HpBar):

    def __init__(self):
        self.shield = True
        self.shield_img = pygame.image.load(f'./images/shield/shield.png')
        self.x = 100
        self.y = 40
        self.point_x_1 = 126
        self.point_x_2 = 173
        self.point_y_1 = 120
        self.point_y_2 = 160
        self.width = 300
        self.height = 300
        self.boom = 0
        self.animation_counter = 0
        self.missile_counter = 0
        self.missile_shot = False
        self.hp = 550
        self.x_start = 40
        self.y_start = 0
        self.name = "Boss"
        self.x_end = 580
        self.y_end = 30
        self.go_right = True
        self.enemy1_ship_imgs = []
        for i in range(11):
            self.enemy1_ship_imgs.append(pygame.image.load(f"./images/boss/boss_{i + 1}.png"))
        self.engine_1 = Engine(self.x + 25, 600, 0, "SILNIK 1", 790 , 30)
        self.engine_2 = Engine(self.x + 70, 600, 40, "SILNIK 2", 790 , 70)
        self.engine_3 = Engine(self.x + 200, 800, 0, "SILNIK 3", 990 , 30)
        self.engine_4 = Engine(self.x + 245, 800, 40, "SILNIK 4", 990 , 70)
        #self.engine_3 = Engine(self.x + 200, 600, 80, "SILNIK 3", 790 , 110)
        #self.engine_4 = Engine(self.x + 245, 600, 120, "SILNIK 4", 790 , 150)
        self.engines = [self.engine_1, self.engine_2, self.engine_3, self.engine_4]
    
    def draw(self, win):
        self.animation_counter += 1
        if self.animation_counter + 1 >= 27:
            self.animation_counter = 0
            self.missile_counter += 1
            self.missile_shot = True
        win.blit(self.enemy1_ship_imgs[self.animation_counter // 3], (self.x, self.y))
        if self.shield:
            win.blit(self.shield_img, (self.x, self.y))
            for engine in self.engines:
                engine.draw(win)
                if self.go_right:
                    engine.x += 5
                else:
                    engine.x -= 5
                if engine.hp <= 9:
                    self.engines.remove(engine)
                    engine.boom_after_collision(win)
        self.move()
        self.hp_bar(win)

    def move(self):
        if self.x <= 0:
            self.go_right = True
        if self.x >= 700:
            self.go_right = False
        if self.go_right:
            self.x += 5
        else:
            self.x -= 5
        self.fire_place_x = self.x + 145
    
    def shot(self, bullets, player_x):
        if self.animation_counter == 0:
            bullets.append(EnemyBullet(self.fire_place_x, self.y + self.height))      
            bullets.append(EnemyBullet(self.fire_place_x + 15, self.y + self.height))  
            bullets.append(EnemyBullet(self.fire_place_x - 15, self.y + self.height))  
        if self.missile_shot:
            if str(self.missile_counter).endswith("5"):
                bullets.append(Missile(self.x, self.y + 180, player_x))
                bullets.append(Missile(self.x + 290, self.y + 180, player_x))
            self.missile_shot = False
        return bullets

    def collision(self, player):
        if (self.x + self.width) > player.x and self.x < (player.x + player.width):
            if (self.y + self.height - 120) > player.y and (self.y + 120) < (player.y + player.height):
                return True
        if (self.x + self.width - 123) > (player.x + 40) and (self.x + 123) < (player.x + player.width - 40):
            if (self.y + self.height) > player.y and (self.y + 20) < (player.y + player.height):
                return True
        return False

    def BIG_boom_after_collision(self, win):
        if self.boom <= 10:
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

class Engine(HpBar):
    def __init__(self, x, x_start, y_start, name, x_end, y_end):
        self.animation_counter = 0
        self.x = x
        self.y = 130
        self.point_x_1 = 0
        self.point_x_2 = 0
        self.point_y_1 = 0
        self.point_y_2 = 100
        self.hp = 200
        self.width = 30
        self.height = 100
        self.x_start = x_start
        self.y_start = y_start
        self.name = name
        self.x_end = x_end
        self.y_end = y_end
        self.boom = 0
        self.img = []
        for i in range(11):
            self.img.append(pygame.image.load(f'./images/engine/engine_{i + 1}.png'))
    
    def draw(self, win):
        self.animation_counter += 1
        if self.animation_counter + 1 >= 27:
            self.animation_counter = 0 
        win.blit(self.img[self.animation_counter // 3], (self.x, self.y))
        self.hp_bar(win)