import pygame
from player.player import Player
from buttons.button import Button
from .level_class import LevelClass
from enemies.spawnerEnemy import SpawnerEnemy


class Level_8(LevelClass):

    def __init__(self):
        self.bg_image = pygame.image.load("./images/level_background/background_l1.png")
        self.menu_button = Button(5, 5, 25, 20, (255, 0, 0), 'MENU', font_size=7)
        self.player = Player()
        self.players_bullets = []
        self.enemy = SpawnerEnemy(200, 52, 40, 10, "PRZECIWNIK", 830, 40, 800)
        #self.enemy_bullets = [] 
        self.state = 'game'
        self.level_name = 'level_8'
        self.is_star_data = False
        self.lost_bullet = False
    
    def draw(self, win):
        win.blit(self.bg_image, (0, 0))
        # enemy
        if self.state != 'won' and self.state != 'collision':
            self.enemy.draw(win, self.player.x, self.player.y)
            #self.enemy_bullets = self.enemy.shot(self.enemy_bullets)
        
        for en in self.enemy.spawned_enemies:
            if en.stick:
                self.player.hp -= 1

        if self.state != 'game':
            self.enemy.spawned_enemies = []
        self.draw_regural_things(win, [self.enemy] + self.enemy.spawned_enemies)