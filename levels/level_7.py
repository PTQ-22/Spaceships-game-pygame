import pygame
from player.player import Player
from buttons.button import Button
from enemies.boss import Boss
from .level_class import LevelClass
from enemies.bullet import EnemyBullet
from enemies.missileEnemy import Missile

class Level_7(LevelClass):

    def __init__(self):
        self.bg_image = pygame.image.load("./images/level_background/background_l7.png")
        self.menu_button = Button(5, 5, 25, 20, (255, 0, 0), 'MENU', font_size=7)
        self.player = Player()
        self.players_bullets = []
        self.enemy = Boss()
        self.enemy_bullets = [] 
        self.state = 'game'
        self.level_name = 'level_7'
        self.is_star_data = False
        self.lost_bullet = False
    
    def draw(self, win):
        win.blit(self.bg_image, (0, 0))
        self.menu_button.draw(win)
        self.check_win_or_lose(win)

        # enemy
        if self.state != 'won' and self.state != 'collision':
            self.enemy.draw(win)
            self.enemy_bullets = self.enemy.shot(self.enemy_bullets, self.player.x)
        
        if self.enemy.engines == []:
            self.enemy.shield = False

        for enemy_bullet in self.enemy_bullets:
            enemy_bullet.draw(win)
            if enemy_bullet.out_of_game():
                self.enemy_bullets.remove(enemy_bullet)
            
            if enemy_bullet.hit(self.player, win):
                self.enemy_bullets.remove(enemy_bullet)
                if type(enemy_bullet) == EnemyBullet:
                    self.player.hp -= 20
                elif type(enemy_bullet) == Missile:
                    self.player.hp -= 40

        # player
        if self.state != 'lose' and self.state != 'collision':
            self.player.draw(win)

        for player_bullet in self.players_bullets:
            player_bullet.draw(win)
            if player_bullet.out_of_game():
                self.players_bullets.remove(player_bullet)
                self.lost_bullet = True
            
            for enemy in [self.enemy.engine_1, self.enemy.engine_2, self.enemy.engine_3, self.enemy.engine_4]:
                if player_bullet.hit(enemy, win):
                    try:
                        self.players_bullets.remove(player_bullet)
                    except ValueError:
                        pass
                    enemy.hp -= 20
            if player_bullet.hit(self.enemy, win):
                try:
                    self.players_bullets.remove(player_bullet)
                except ValueError:
                    pass
                if not self.enemy.shield:
                    self.enemy.hp -= 20

