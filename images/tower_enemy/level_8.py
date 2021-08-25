import pygame
from player.player import Player
from buttons.button import Button
from enemies.towerEnemy import TowerEnemy
from .level_class import LevelClass

class Level_8(LevelClass):

    def __init__(self):
        self.bg_image = pygame.image.load("./images/level_background/background_l8.png")
        self.menu_button = Button(5, 5, 25, 20, (255, 0, 0), 'MENU', font_size=7)
        self.player = Player()
        self.players_bullets = []
        self.enemy = TowerEnemy(200, 50, 40, 10, "PRZECIWNIK", 830, 40, 800)
        self.enemy_bullets = [] 
        self.state = 'game'
        self.level_name = 'level_8'
        self.is_star_data = False
        self.lost_bullet = False
    
    def draw(self, win):
        win.blit(self.bg_image, (0, 0))
        # enemy

        if self.state != 'won' and self.state != 'collision':
            self.enemy.draw(win)
            #self.enemy_bullets = self.enemy.shot(self.enemy_bullets)
        self.enemy.scan_for_player(self.player)
        for enemy_bullet in self.enemy_bullets:
            enemy_bullet.draw(win)
            if enemy_bullet.out_of_game():
                self.enemy_bullets.remove(enemy_bullet)
            
            if enemy_bullet.hit(self.player, win):
                self.enemy_bullets.remove(enemy_bullet)
                self.player.hp -= 20
        self.draw_regural_things(win, [self.enemy])