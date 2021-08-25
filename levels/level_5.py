import pygame
from player.player import Player
from buttons.button import Button
from enemies.missileEnemy import MissileEnemy
from .level_class import LevelClass


class Level_5(LevelClass):

    def __init__(self):
        self.bg_image = pygame.image.load("./images/level_background/background_l1.png")
        self.menu_button = Button(5, 5, 25, 20, (255, 0, 0), 'MENU', font_size=7)
        self.player = Player()
        self.players_bullets = []
        self.enemy = MissileEnemy(200, 100, 40, 10, "PRZECIWNIK", 430, 40, 400)
        self.enemy_bullets = [] 
        self.state = 'game'
        self.level_name = 'level_5'
        self.is_star_data = False
        self.lost_bullet = False
    
    def draw(self, win):
        win.blit(self.bg_image, (0, 0))
        # enemy
        if self.state != 'won' and self.state != 'collision':
            self.enemy.draw(win)                                      # draw enemy
            self.enemy_bullets = self.enemy.shot(self.enemy_bullets, self.player.x)  # enemy shotting

        for enemy_bullet in self.enemy_bullets:
            enemy_bullet.draw(win)
            if enemy_bullet.out_of_game():
                self.enemy_bullets.remove(enemy_bullet)
            
            if enemy_bullet.hit(self.player, win):                           # player get hit
                self.enemy_bullets.remove(enemy_bullet)
                self.player.hp -= 40
        
        self.draw_regural_things(win, [self.enemy])
