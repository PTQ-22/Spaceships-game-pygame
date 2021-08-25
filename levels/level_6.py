import pygame
from random import randint
from .level_class import LevelClass
from buttons.button import Button
from enemies.teleporterEnemy import TeleporterEnemy
from player.player import Player


class Level_6(LevelClass):

    def __init__(self):
        self.bg_image = pygame.image.load("./images/level_background/background_l6.png")
        self.menu_button = Button(5, 5, 25, 20, (255, 0, 0), 'MENU', font_size=7)
        self.player = Player()
        self.players_bullets = []
        self.enemy = TeleporterEnemy(200, 100, 40, 10, "PRZECIWNIK", 630, 40, 600)
        self.enemy_bullets = [] 
        self.state = 'game'
        self.level_name = 'level_6'
        self.is_star_data = False
        self.lost_bullet = False

    def draw(self, win):
        win.blit(self.bg_image, (0, 0))

        for enemy_bullet in self.enemy_bullets:
            enemy_bullet.draw(win)
            if enemy_bullet.out_of_game():
                try:
                    self.enemy_bullets.remove(enemy_bullet)
                except ValueError:
                    pass
            
            if enemy_bullet.hit(self.player, win):          
                try:                 # player get hit
                    self.enemy_bullets.remove(enemy_bullet)
                except ValueError:
                    pass
                self.player.hp -= 20
        if self.enemy.animation_counter == 2:
            r = randint(6, 8)
            if r == 7:
                self.enemy.teleport()
                
        if self.enemy.boom_counter < 10:
            self.enemy.boom_counter += 1
            pygame.draw.circle(win, (16, 30, 80), (self.enemy.x_before + 50, self.enemy.y + 50), 70)
            pygame.draw.circle(win, (16, 255, 226), (self.enemy.x_before + 50, self.enemy.y + 50), 60)
            pygame.draw.circle(win, (16, 30, 80), (self.enemy.x_after + 50, self.enemy.y + 50), 70)
            pygame.draw.circle(win, (16, 255, 226), (self.enemy.x_after + 50, self.enemy.y + 50), 60)

        if self.state != 'won' and self.state != 'collision':
            self.enemy.draw(win)                                      # draw enemy
            self.enemy_bullets = self.enemy.shot(self.enemy_bullets)  # enemy shotting
        
        self.draw_regural_things(win, [self.enemy])