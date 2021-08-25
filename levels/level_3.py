import pygame
import json
from player.player import Player
from buttons.button import Button
from enemies.enemyRedSmall import EnemyRedSmall
from .level_class import LevelClass

class Level_3(LevelClass):

    def __init__(self):
        self.bg_image = pygame.image.load("./images/level_background/background_l1.png")
        self.menu_button = Button(5, 5, 25, 20, (255, 0, 0), 'MENU', font_size=7)
        self.player = Player()
        self.players_bullets = []
        self.enemy_1 = EnemyRedSmall(200, 100, 40, 10, "PRZECIWNIK", 230, 40, 200)
        self.enemy_2 = EnemyRedSmall(400, 200, 300, 10, "PRZECIWNIK", 490, 40, 200)
        self.enemy_3 = EnemyRedSmall(600, 300, 600, 10, "PRZECIWNIK", 790, 40, 200)
        self.enemy_bullets = [] 
        self.state = 'game'
        self.level_name = 'level_3'
        self.is_star_data = False
        self.lost_bullet = False
    
    def draw(self, win):
        win.blit(self.bg_image, (0, 0))
        self.check_win_or_lose(win)
        # enemy
        if self.state != 'won' and self.state != 'collision':
            if self.enemy_1.hp > 0:
                self.enemy_1.draw(win)
            else:
                self.enemy_1.y = -200
                self.enemy_1.x = -200
            if self.enemy_2.hp > 0:
                self.enemy_2.draw(win)
            else:
                self.enemy_2.y = -200
                self.enemy_2.x = -200
            if self.enemy_3.hp > 0:
                self.enemy_3.draw(win)
            else:
                self.enemy_3.y = -200
                self.enemy_3.x = -200
            self.enemy_bullets = self.enemy_1.shot(self.enemy_bullets)
            self.enemy_bullets = self.enemy_2.shot(self.enemy_bullets)
            self.enemy_bullets = self.enemy_3.shot(self.enemy_bullets)

        for enemy_bullet in self.enemy_bullets:
            enemy_bullet.draw(win)
            if enemy_bullet.out_of_game():
                self.enemy_bullets.remove(enemy_bullet)
            
            if enemy_bullet.hit(self.player, win):
                self.enemy_bullets.remove(enemy_bullet)
                self.player.hp -= 20
        
        self.draw_regural_things(win, [self.enemy_1, self.enemy_2, self.enemy_3], normal_check_win_or_lose=False)

    def check_win_or_lose(self, win):
        if self.player.hp <= 0:
            #print("PRZEGRANA")
            self.state = 'lose'
            self.menu_button.center_and_draw_big_text('PRZEGRANA')
        if self.enemy_1.hp <= 0 and self.enemy_2.hp <=0 and self.enemy_3.hp <=0:
            #print("WYGRANA")
            self.state = 'won'
            self.menu_button.center_and_draw_big_text('WYGRANA')
            if self.is_star_data == False:
                with open('star_data/data.json') as data:
                    self.star_data = json.loads(data.read())
                
                self.star_data[self.level_name]["star_1"] = True
                if self.player.hp == 200:
                    self.star_data[self.level_name]["star_2"] = True
                if not self.lost_bullet:
                    self.star_data[self.level_name]["star_3"] = True
                self.is_star_data = True
        if self.enemy_1.collision(self.player):
            self.state = 'collision'
            self.player.animation_counter += 1
            if self.player.animation_counter + 1 >= 27:
                self.enemy_1.y -= 300
            self.menu_button.center_and_draw_big_text('PRZEGRANA')
            self.player.boom_after_collision(win)
        if self.enemy_2.collision(self.player):
            self.state = 'collision'
            self.player.animation_counter += 1
            if self.player.animation_counter + 1 >= 27:
                self.enemy_2.y -= 300
            self.menu_button.center_and_draw_big_text('PRZEGRANA')
            self.player.boom_after_collision(win)
        if self.enemy_3.collision(self.player):
            self.state = 'collision'
            self.player.animation_counter += 1
            if self.player.animation_counter + 1 >= 27:
                self.enemy_3.y -= 300
            self.menu_button.center_and_draw_big_text('PRZEGRANA')
            self.player.boom_after_collision(win)
