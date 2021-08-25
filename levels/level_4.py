import pygame
from player.player import Player
from buttons.button import Button
from enemies.laserShip import LaserShip
from .level_class import LevelClass


class Level_4(LevelClass):

    def __init__(self):
        self.bg_image = pygame.image.load("./images/level_background/background_l1.png")
        self.menu_button = Button(5, 5, 25, 20, (255, 0, 0), 'MENU', font_size=7)
        self.player = Player()
        self.players_bullets = []
        self.enemy = LaserShip(500, 100, 40, 10, "STATEK LASEROWY", 430, 40, 400)
        self.enemy_bullets = [] 
        self.state = 'game'
        self.is_star_data = False
        self.lost_bullet = False
        self.level_name = 'level_4'
    
    def draw(self, win):
        win.blit(self.bg_image, (0, 0))
        self.draw_regural_things(win, [self.enemy])
        # enemy
        if self.state != 'won' and self.state != 'collision':
            if self.enemy.laser_shot():
                if self.enemy.draw_laser(win, self.player):
                    self.player.hp -= 20
            self.enemy.draw(win)        
