import pygame
import json
from player.player import Player
from buttons.button import Button
from enemies.boss import Boss

class LevelClass:
    
    def draw_regural_things(self, win, enemies_list, normal_check_win_or_lose=True):
        self.menu_button.draw(win)
        if normal_check_win_or_lose:
            self.check_win_or_lose(win)

        # player
        if self.state != 'lose' and self.state != 'collision':
            self.player.draw(win)

        for player_bullet in self.players_bullets:
            player_bullet.draw(win)
            if player_bullet.out_of_game():
                self.players_bullets.remove(player_bullet)
                self.lost_bullet = True
            
            for enemy in enemies_list:
                if player_bullet.hit(enemy, win):
                    try:
                        self.players_bullets.remove(player_bullet)
                    except ValueError:
                        pass
                    enemy.hp -= 20

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    return -1
            pos = pygame.mouse.get_pos()
            
            if self.state != 'lose':
                self.players_bullets = self.player.get_keyboard_events(event, self.players_bullets)
            
            if event.type == pygame.MOUSEMOTION:
                if self.menu_button.is_mouse(pos):
                    self.menu_button.color = (200, 0, 0)
                else:
                    self.menu_button.color = (255, 0, 0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.menu_button.is_mouse(pos):
                    return 0
        return self

    def check_win_or_lose(self, win):
        if self.player.hp <= 0:
            self.player.boom_after_collision(win)
            #print("PRZEGRANA")
            self.state = 'lose'
            self.menu_button.center_and_draw_big_text('PRZEGRANA')
        elif self.enemy.hp <= 0:
            if type(self.enemy) == Boss:
                self.enemy.BIG_boom_after_collision(win)
            else:
                self.enemy.boom_after_collision(win)
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

        elif self.enemy.collision(self.player):
            self.state = 'collision'
            self.player.animation_counter += 1
            if self.player.animation_counter + 1 >= 27:
                self.enemy.y -= 300
            self.menu_button.center_and_draw_big_text('PRZEGRANA')
            self.player.boom_after_collision(win)
            if type(self.enemy) == Boss:
                self.enemy.BIG_boom_after_collision(win)
            else:
                self.enemy.boom_after_collision(win)
        
    def pass_star_data(self):
        return self.star_data

