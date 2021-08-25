import pygame
from game.hp_bar import HpBar


class SpawnerEnemy(HpBar):

    def __init__(self, x, y, x_start, y_start, name, x_end, y_end, hp):
        self.x = x
        self.y = y
        self.point_x_1 = 75
        self.point_x_2 = 275
        self.point_y_1 = 0
        self.point_y_2 = 73
        self.boom = 0
        self.animation_counter = 0
        self.hp = hp
        self.width = 350
        self.height = 250
        self.x_start = x_start
        self.y_start = y_start
        self.name = name
        self.x_end = x_end
        self.y_end = y_end
        self.go_right = True
        self.spawned_enemies = []
        self.spawn_counter = 0
        self.angle_counter = 0
        self.disc_right_down_img = pygame.image.load("./images/spawner_enemy/disc_right_down.png")

        self.enemy1_ship_img = pygame.image.load("./images/spawner_enemy/spawner_enemy.png")

    def draw_disc(self, win):
        if self.angle_counter == 360:
            self.angle_counter = 0
        self.angle_counter += 5
        rotated_img = pygame.transform.rotate(self.disc_right_down_img, self.angle_counter)
        new_rect = rotated_img.get_rect(center = self.disc_right_down_img.get_rect(topleft = (self.x + 75, self.y + 50)).center)
        win.blit(rotated_img, new_rect.topleft) #(self.x + self.width / 2, self.y + self.height / 2))
    
    def draw(self, win, player_x, player_y):
        self.animation_counter += 1
        if self.animation_counter + 1 >= 27:
            self.animation_counter = 0
            self.spawn_counter += 1
        win.blit(self.enemy1_ship_img, (self.x, self.y))
        self.move()
        self.hp_bar(win)

        for en in self.spawned_enemies:
            en.draw(win, player_x, player_y, self.animation_counter)
            if en.hp <= 0:
                self.spawned_enemies.remove(en)
                en.draw_boom(win)
                
            if en.drop:
                if self.go_right:
                    if en.side == 'left':
                        en.x -= 3
                    elif en.side == 'right':
                        en.x += 8
                else:
                    if en.side == 'left':
                        en.x -= 8
                    elif en.side == 'right':
                        en.x += 3 
        self.spawn_enemies()
        self.draw_disc(win)

    def spawn_enemies(self):
        if self.spawn_counter == 4:
            self.spawn_counter = 0
            self.spawned_enemies.append(SpawnedEnemy(self.x - 50, self.y, 'left'))
            self.spawned_enemies.append(SpawnedEnemy(self.x + self.width, self.y, 'right'))    

    def move(self):
        if self.x <= 200:
            self.go_right = True
        if self.x >= 450:
            self.go_right = False
        if self.go_right:
            self.x += 3
        else:
            self.x -= 3
        self.fire_place_x = self.x + 47

    def collision(self, player):
        if (self.x + self.width) > player.x and self.x < (player.x + player.width):
            if (self.y + self.point_y_2) > player.y and (self.y) < (player.y + player.height):
                return True
        if (self.x + self.point_x_2) > (player.x + 40) and (self.x + self.point_x_1) < (player.x + player.width - 40):
            if (self.y + self.height) > player.y and (self.y) < (player.y + player.height):
                return True
        return False


class SpawnedEnemy:

    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side
        self.hp = 60
        self.drop = True
        self.counter = 0
        self.width = 50
        self.height = 50
        self.point_x_1 = 0
        self.point_x_2 = 50
        self.point_y_1 = 0
        self.point_y_2 = 50
        self.stick = False
        self.angle_counter = 0
        self.spawned_img = pygame.image.load("./images/spawner_enemy/spawned_1.png")
        self.small_disc_img = pygame.image.load("./images/spawner_enemy/small_disc.png")

    def move(self, player_x, player_y):
        if self.counter <= 20:
            self.counter += 1
        else:
            self.drop = False
            if not self.stick:
                if (self.y >= player_y and self.y < player_y + 100):
                    if (self.x < (player_x + 74) and (self.x + self.width) > (player_x + 49)):
                        self.stick = True
                else:
                    self.y += 5
            else: 
                self.x = player_x + 25
                self.y = player_y + 20
            if self.x > player_x + 50:
                self.x -= 10
            elif self.x < player_x - 50:
                self.x += 10
            else:
                self.x += 0

    def draw(self, win, player_x, player_y, counter):
       # pygame.draw.rect(win, (0, 100, 100), (self.x, self.y, self.width, self.height))
        #win.blit(self.spawned_imgs[counter // 3], (self.x, self.y))
        if self.drop:
            if self.side == 'left':
                win.blit(pygame.transform.rotate(self.spawned_img, -90), (self.x, self.y))
            else:
                win.blit(pygame.transform.rotate(self.spawned_img, 90), (self.x, self.y))
        else:
            win.blit(self.spawned_img, (self.x, self.y))
                
        self.move(player_x, player_y)
        if self.angle_counter == 360:
            self.angle_counter = 0
        self.angle_counter += 5
        if not self.drop:
            rotated_img = pygame.transform.rotate(self.small_disc_img, self.angle_counter)
            new_rect = rotated_img.get_rect(center = self.small_disc_img.get_rect(topleft = (self.x - 12, self.y + 25)).center)
            new_rect_2 = rotated_img.get_rect(center = self.small_disc_img.get_rect(topleft = (self.x + 37, self.y + 25)).center)
            win.blit(rotated_img, new_rect.topleft)
            win.blit(rotated_img, new_rect_2.topleft) #(self.x + self.width / 2, self.y + self.height / 2))
    
    def draw_boom(self, win):
            pygame.draw.circle(win, (255, 255, 0), (self.x, self.y), 20)

            pygame.draw.circle(win, (255, 100, 0), (self.x, self.y), 40)  
            pygame.draw.circle(win, (255, 255, 0), (self.x, self.y), 20)
                
            pygame.draw.circle(win, (255, 0, 0), (self.x, self.y), 60)
            pygame.draw.circle(win, (255, 100, 0), (self.x, self.y), 40)  
            pygame.draw.circle(win, (255, 255, 0), (self.x, self.y), 20)
                    
            pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), 80)
            pygame.draw.circle(win, (255, 0, 0), (self.x, self.y), 60)
            pygame.draw.circle(win, (255, 100, 0), (self.x, self.y), 40)  
            pygame.draw.circle(win, (255, 255, 0), (self.x, self.y), 20) 