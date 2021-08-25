import pygame
from player.player import Player
from buttons.button import Button
from .level_class import LevelClass
from .level_3 import Level_3
from enemies.surprise_enemy import SurpriseEnemy
from enemies.laserShip import LaserShip
from enemies.enemyRedSmall import EnemyRedSmall
from enemies.missileEnemy import MissileEnemy


class Level_9(Level_3):

    def __init__(self):
        self.bg_image = pygame.image.load("./images/level_background/background_l1.png")
        self.menu_button = Button(5, 5, 25, 20, (255, 0, 0), 'MENU', font_size=7)
        self.player = Player()
        self.players_bullets = []
        self.enemy = SurpriseEnemy()
        self.enemies = [self.enemy]
        self.enemy_bullets = [] 
        self.state = 'surprise'
        self.level_name = 'level_9'
        self.is_star_data = False
        self.lost_bullet = False
    
    def check_collision_state_surprise(self, win):
        if self.enemy.collision(self.player):
            self.state = 'collision'
            self.player.animation_counter += 1
            if self.player.animation_counter + 1 >= 27:
                self.enemy.y -= 300
            self.menu_button.center_and_draw_big_text('PRZEGRANA')
            self.player.boom_after_collision(win)

    def draw(self, win):
        win.blit(self.bg_image, (0, 0))

        # enemy
        if self.state == 'surprise':
            self.check_collision_state_surprise(win)
            self.enemy.draw(win)
            self.enemy_bullets = self.enemy.shot(self.enemy_bullets)
            if self.enemy.hp <= 0:
                self.state = "game"
                self.enemy.BIG_boom_after_collision(win)
                del self.enemy
                self.enemies = []
                self.enemy_1 = MissileEnemy(200, 100, 40, 10, "PRZECIWNIK", 230, 40, 200)
                self.enemy_2 = LaserShip(400, 200, 300, 10, "STATEK LASEROWY", 690, 40, 400)
                self.enemy_3 = EnemyRedSmall(600, 300, 800, 10, "PRZECIWNIK", 990, 40, 200)
                self.enemies = [self.enemy_1, self.enemy_2, self.enemy_3]

        elif self.state == "game":
            self.check_win_or_lose(win)
            if self.enemy_1.hp > 0:
                self.enemy_1.draw(win)
            else:
                self.enemy_1.y = -200
                self.enemy_1.x = -200
            if self.enemy_2.hp > 0:
                if self.enemy_2.laser_shot():
                    if self.enemy_2.draw_laser(win, self.player):
                        self.player.hp -= 20
                self.enemy_2.draw(win)
            else:
                self.enemy_2.y = -200
                self.enemy_2.x = -200
            if self.enemy_3.hp > 0:
                self.enemy_3.draw(win)
            else:
                self.enemy_3.y = -200
                self.enemy_3.x = -200
            
            self.enemy_bullets = self.enemy_1.shot(self.enemy_bullets, self.player.x)
            self.enemy_bullets = self.enemy_3.shot(self.enemy_bullets)

        for enemy_bullet in self.enemy_bullets:
            enemy_bullet.draw(win)
            if enemy_bullet.out_of_game():
                self.enemy_bullets.remove(enemy_bullet)
            
            if enemy_bullet.hit(self.player, win):
                self.enemy_bullets.remove(enemy_bullet)
                self.player.hp -= 20

        self.draw_regural_things(win, self.enemies, normal_check_win_or_lose=False)

    
    